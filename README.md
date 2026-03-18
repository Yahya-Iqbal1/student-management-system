# EduPulse — Student Management System 🎓

> *A full-featured Student Management System with 2 versions — Console & Web App*

---

## 💡 What is this?

A complete Student Management System built with Python that allows institutions to manage student records efficiently. Available in two versions: a simple console app and a powerful web-based dashboard built with Streamlit.

---

## ✨ Features

### 🖥️ Version 1 — Console App (`student_management.py`)
- **Add Student** — Name, age, class & email
- **View All Students** — Display all records in table format
- **Update Student** — Edit any student's details by ID
- **Delete Student** — Remove student record by ID
- **SQLite3 Database** — All data stored locally

### 🚀 Version 2 — Web Dashboard (`app.py`) — EduPulse CRM
- **📊 Dashboard** — Institutional analytics & insights
  - Total students, Average age, Unique classes metrics
  - **Bar Chart** — Students per class (Plotly)
  - **Histogram** — Age distribution chart (Plotly)
- **➕ Add Student** — Clean registration form with age slider
- **📋 Student Directory** — Full records browser
  - Search students by name (live filter)
  - View all records in interactive table
  - **Export to CSV** — Download all records
  - **Update Student** — Edit name & email
  - **Delete Student** — Permanent record removal
- **Beautiful UI** — Custom CSS, purple theme, card design
- **One-click Launch** — `run_app.bat` to start instantly

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core language |
| SQLite3 | Local database |
| Streamlit | Web app framework |
| Pandas | Data handling & CSV export |
| Plotly Express | Interactive charts & graphs |
| datetime | Registration date tracking |
| CSS | Custom styling for web UI |

---

## 📁 Project Structure

```
student-management-system/
│
├── app.py                  # Streamlit web app (EduPulse CRM)
├── student_management.py   # Console version
├── run_app.bat             # One-click launcher for web app
├── run_app.spec            # PyInstaller spec file
└── Students.db             # SQLite database (auto-created)
```

---

## 🚀 How to Run

### Console Version:
```bash
python student_management.py
```

### Web App Version:

**1. Install required libraries:**
```bash
pip install streamlit pandas plotly
```

**2. Run the app:**
```bash
streamlit run app.py
```

**OR simply double-click `run_app.bat`** ✅

---

## 🖥️ Console Menu

```
--- Students Management System ---
1- Add Student
2- View Student
3- Update Student
4- Delete Student
5- Exit
```

---

## 📸 Web App Sections

| Section | Description |
|---------|-------------|
| Dashboard | Analytics with charts |
| Add Student | Registration form |
| Student Directory | View, search, update, delete |
| Settings | System configuration |

---

## 👨‍💻 Developer

**M. Yahya Iqbal**  
Software Engineering Student — Aligarh Institute of Technology, Karachi  
📧 muhammadyahyaiqbal1@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/yahya-iqbal) | [GitHub](https://github.com/Yahya-Iqbal1) | [Portfolio](https://yahya-iqbal.netlify.app)

---

> *Made with ❤️ by Yahya Iqbal*
