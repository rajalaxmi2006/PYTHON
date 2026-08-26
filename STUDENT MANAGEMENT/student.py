import csv
import os

FILE_NAME = "student.csv"

#  create a csv file if doesn't exist
def create_file():
    if not  os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file :
            writer = csv.writer(file)
            writer.writerow(["Student_ID","Name", "Age", "Course", "Phone"])

#  add student
def add_student():
    student_id=input("Enter Student ID: ").strip()
    name=input("Enter Name :").strip()
    age= input("Enter Age :").strip()
    course=input("Enter Course :").strip()
    phone=input("Enter Phone : ").strip()

    # check duplicate id
    with open (FILE_NAME, "r" , newline='') as file :
        reader = csv.DictReader(file)

        for row in reader:
            if row["Student_ID"]== student_id:
                print("Student ID already exist!!")
                return

    with open (FILE_NAME , "a" , newline="") as file :
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course, phone])

    print("Student added successfully!")
            
# view students
def view_students():
    with open (FILE_NAME, "r" , newline="") as file :
        reader = csv.DictReader(file)

        students = list(reader)

    if not students :
        print("No student record found")
        return

    print(f"{'ID : <12'} {'Name: <20'} {'Age:<8'} {'Course:<15'} {'Phone :<15'}") 

    for student in students:
        print(
            f"{student['Student_ID']:<12}"
            f"{student['Name']:<12}"
            f"{student['Age']:<12}"
            f"{student['Course']:<12}"
            f"{student['Phone']:<12}"
        )

# main menu 
def main():

    create_file()

    while True:

        print("\n")
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add student")
        print("2. View student")
        print("3. Exit")

        choice = input("Enter your choice :").strip()

        if choice == "1" :
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()