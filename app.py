import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import datetime

# ------------------ DATABASE FUNCTIONS ------------------
def get_connection():
    conn = sqlite3.connect("Students.db", check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        class TEXT,
        email TEXT,
        reg_date DATE
    )
    """)
    conn.commit()

init_db()

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="EduPulse | Student Management",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for "Mind Blowing" Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4F46E5;
        color: white;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #3730A3; border: none; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413380.png", width=100)
    st.title("EduPulse CRM")
    st.markdown("---")
    menu = st.radio(
        "Navigation",
        ["📊 Dashboard", "➕ Add Student", "📋 Student Directory", "⚙ Settings"],
        index=0
    )
    st.markdown("---")
    st.info("System Status: Online 🟢")

# ------------------ HELPERS ------------------
def load_data():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Students", conn)
    return df

# =================================================
# 📊 DASHBOARD (New Feature)
# =================================================
if menu == "📊 Dashboard":
    st.title("🚀 Institutional Insights")
    df = load_data()
    
    if not df.empty:
        # Metrics
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Students", len(df))
        with c2:
            st.metric("Avg. Age", round(df['age'].mean(), 1))
        with c3:
            st.metric("Unique Classes", len(df['class'].unique()))
        
        st.markdown("---")
        
        # Charts
        col_left, col_right = st.columns(2)
        with col_left:
            fig = px.bar(df, x='class', title="Students per Class", color='class', template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)
        with col_right:
            fig2 = px.histogram(df, x='age', title="Age Distribution", nbins=10, color_discrete_sequence=['#4F46E5'])
            st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No data available to show analytics.")

# =================================================
# ➕ ADD STUDENT
# =================================================
elif menu == "➕ Add Student":
    st.title("📝 Register New Student")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="Yahya Iqbal")
            age = st.slider("Age", 5, 60, 18)
        with col2:
            class_name = st.selectbox("Class/Batch", ["Science", "Commerce", "Arts", "IT", "Engineering"])
            email = st.text_input("Email Address", placeholder="example@mail.com")
        
        if st.button("Confirm Registration"):
            if name and email:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Students (name, age, class, email, reg_date) VALUES (?, ?, ?, ?, ?)",
                    (name, age, class_name, email, datetime.now().date())
                )
                conn.commit()
                st.balloons()
                st.success(f"Successfully Registered {name}!")
            else:
                st.error("Please fill mandatory fields.")

# =================================================
# 📋 STUDENT DIRECTORY (View/Update/Delete combined)
# =================================================
elif menu == "📋 Student Directory":
    st.title("🔍 Student Records")
    df = load_data()
    
    # Search Box
    search = st.text_input("Search student by name...", "")
    if search:
        df = df[df['name'].str.contains(search, case=False)]

    # Data Display
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Export to CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Records as CSV", data=csv, file_name="students.csv", mime="text/csv")
    
    st.markdown("---")
    
    # Manage Records Section
    st.subheader("🛠 Modify Records")
    tab1, tab2 = st.tabs(["Update Student", "Remove Student"])
    
    with tab1:
        if not df.empty:
            id_list = df['id'].tolist()
            selected_id = st.selectbox("Select ID to Edit", id_list)
            
            # Form to update
            current_row = df[df['id'] == selected_id].iloc[0]
            new_name = st.text_input("Update Name", value=current_row['name'])
            new_email = st.text_input("Update Email", value=current_row['email'])
            
            if st.button("Save Changes"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE Students SET name=?, email=? WHERE id=?", (new_name, new_email, selected_id))
                conn.commit()
                st.rerun()
        
    with tab2:
        if not df.empty:
            del_id = st.selectbox("Select ID to Delete", df['id'].tolist(), key="del_box")
            if st.button("❗ Permanent Delete", type="primary"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Students WHERE id=?", (del_id,))
                conn.commit()
                st.toast("Record deleted!")
                st.rerun()

# ------------------ FOOTER ------------------
st.sidebar.markdown("""
<div style='position: fixed; bottom: 10px; left: 10px;'>
    Made with ❤️ by Yahya Iqbal
</div>
""", unsafe_allow_html=True)
