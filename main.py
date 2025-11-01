from student import Student
from manager import StudentManager

manager = StudentManager()

s1 = Student(1, "Alice", 22, "CSE", 3.8, "alice@example.com", "+880123456789")
s2 = Student(2, "Bob", 23, "EEE", 3.5, "bob@example.com", "+880198765432")


manager.add_student(s1)
manager.add_student(s2)

print("All Students:")
for s in manager.list_students():
    print(s)

print("\nSearch by ID 1:")
found = manager.find_student_by_id(5)
print(found if found else "Not found")
