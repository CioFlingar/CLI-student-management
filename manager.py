from colorama import Fore, Style, init
import logging
from typing import List, Optional
from student import Student, InvalidStudentDataError

init(autoreset=True)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class StudentManager:
    def __init__(self) -> None:
        self.students: List[Student] = []

    def add_student(self, student:Student) -> None:
        if any(s.id == student.id for s in self.students):
            raise ValueError(f"Student with the id already exists.")
        self.students.append(student)
        print(Fore.GREEN + f"✅ Student added: {student.name} (ID: {student.id})")
        logging.info(f"Added student: {student.name} (Id: {student.id})")

    def list_students(self) -> List[Student]:
        return self.students

    def find_student_by_id(self, student_id: int) -> Optional[Student]:
        for student in self.students:
            if student_id == student.id:
                print(Fore.GREEN + f"✅ Found student: {student.name}")
                logging.info(f"Found student with ID {student_id}")
                return student

        print(Fore.YELLOW + f"⚠️  No student found with ID {student_id}")
        logging.warning(f"Student with ID {student_id} not found.")
        return None


    def update_student(self):
        pass

    def delete_student(self):
        pass