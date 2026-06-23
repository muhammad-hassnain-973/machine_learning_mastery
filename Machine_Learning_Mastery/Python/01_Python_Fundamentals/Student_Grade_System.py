students = {}


def add_student():
    student_id = input("Enter Student id: ").strip()
    if student_id in students:
        print("Student with this ID already exists")
        return

    name = input("Enter name of Student: ").strip()
    smester = input("Enter your smester: ").strip()
    students[student_id] = {
        "Name": name,
        "grade": {},
        "smester": smester,
    }
    print(f"Student {name} added successfully")


def record_grades():
    student_id = input("Enter student id: ").strip()
    if student_id not in students:
        print(f"Student with ID {student_id} does not exist")
        return

    subject = input("Enter your Subject: ").strip()
    try:
        grade = float(input("Enter your Grade: "))
        if grade < 0 or grade > 100:
            print("Error: Grade should be between 0 and 100")
            return
        students[student_id]["grade"][subject] = grade
    except ValueError:
        print("Please enter a valid number for grade")


def view_report_card():
    student_id = input("Enter student id: ").strip()
    if student_id not in students:
        print(f"Student with ID {student_id} does not exist")
        return
    student = students[student_id]
    print(f"Report Card for {student['Name']} (Smester: {student['smester']})")
    if not student["grade"]:
        print("No grades recorded yet.")
        return

    for subject, grade in student["grade"].items():
        print(f" - {subject}: {grade}")

    avg = sum(student["grade"].values()) / len(student["grade"])
    print(f"Average Grade: {avg:.2f}")


def main():
    while True:
        print("=" * 20)
        print("Student Grade System")
        print("=" * 20)
        print("1. Add New Student")
        print("2. Record/Update Grades")
        print("3. View Student Report Card")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            record_grades()
        elif choice == "3":
            view_report_card()
        elif choice == "4":
            print("Exiting the Student Grade System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()