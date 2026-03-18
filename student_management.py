import sqlite3
conn = sqlite3.connect("Students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
class TEXT,
email TEXT)""")
conn.commit()
while True:
    print("\n--- Students Management System ---")
    print("1- Add Student")
    print("2- View Student")
    print("3- Update Student")
    print("4- Delete Student")
    print("5- Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        class_name = input("Enter class: ")
        email = input("Enter student email: ")
        cursor.execute(
            "INSERT INTO Students (name,age,class,email)VALUES(?,?,?,?)",(name,age,class_name,email))
        conn.commit()
        print("Student add successfully")
    elif choice == 2:
        cursor.execute(
            "SELECT * FROM Students")
        data = cursor.fetchall()
        if not data:
            print("No Student Found")
        else:
            print("\nID | NAME | AGE | CLASS | EMAIL")
            print("-"*40)
            for row in data:
                print(row)
    elif choice == 3:
        student_id = int(input("Enter student id to update: "))
        name = input("Enter student new name: ")
        age = int(input("Enter student new age: "))
        class_name = input("Enter student new Class: ")
        email = input("Enter student new email: ")
        cursor.execute(
            """UPDATE Students
SET name=?,age=?,class=?,email=? WHERE id=?""",(name,age,class_name,email,student_id))
        conn.commit()
        print("Student update successfully")
    elif choice == 4:
        student_id = int(input("Enter student id to delete: "))

        cursor.execute("DELETE FROM Students WHERE id=?", (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print(" Student ID not found")
        else:
            print(" Student delete successfully")

    elif choice == 5:
        print("Program close by")
        break
    else:
        print("invalid choice")
conn.close()
            
                  
    

