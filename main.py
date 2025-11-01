from student import Student, InvalidStudentDataError
from manager import StudentManager
from colorama import Fore

manager = StudentManager()

def main_menu():
    while True:
        print(Fore.BLUE + "\n===== Student Management CLI =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Find Student by ID")
        print("4. Search Students by Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Sort Students")
        print("8. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            try:
                student = Student(
                    id=int(input("Enter ID: ")),
                    name=input("Enter Name: "),
                    age=int(input("Enter Age: ")),
                    course=input("Enter Course: "),
                    grade=float(input("Enter Grade (0.0 - 4.0): ")),
                    email=input("Enter Email: "),
                    phone=input("Enter Phone: ")
                )
                manager.add_student(student)
            except (ValueError, InvalidStudentDataError) as e:
                print(Fore.RED + f"❌ Error: {e}")

        elif choice == "2":
            students = manager.list_students()
            if not students:
                print(Fore.YELLOW + "⚠️  No students found.")
            else:
                for s in students:
                    print(s)

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            manager.find_student_by_id(student_id)

        elif choice == "4":
            name = input("Enter name to search: ").strip()
            if name:
                manager.find_students_by_name(name)
            else:
                print(Fore.RED + "❌ Name cannot be empty.")

        elif choice == "5":
            student_id = int(input("Enter Student ID to update: "))
            print("Enter new values (leave blank to skip):")
            updates = {}
            for field in ["name", "age", "course", "grade", "email", "phone"]:
                val = input(f"{field.capitalize()}: ").strip()
                if val:
                    if field in ["age"]:
                        val = int(val)
                    elif field in ["grade"]:
                        val = float(val)
                    updates[field] = val
            manager.update_student(student_id, **updates)

        elif choice == "6":
            student_id = int(input("Enter Student ID to delete: "))
            manager.delete_student(student_id)

        elif choice == "7":
            key = input("Enter field to sort by (id, name, age, grade): ").strip().lower()
            if key:
                manager.sort_students(key)
            else:
                print(Fore.RED + "❌ Sort key cannot be empty.")

        elif choice == "8":
            print(Fore.GREEN + "✅ Exiting program. Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main_menu()