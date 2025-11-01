from colorama import Fore, Style, init
import logging
from typing import List, Optional
from student import Student, InvalidStudentDataError
from file_hander import FileHandler

init(autoreset=True)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class StudentManager:
    def __init__(self) -> None:
        self.students: List[Student] = FileHandler.load_from_file()
        print(f"Loaded {len(self.students)} students from data.json")


    def add_student(self, student:Student) -> None:
        if any(s.id == student.id for s in self.students):
            raise ValueError(f"Student with the id already exists.")
        self.students.append(student)
        FileHandler.save_to_file(self.students)
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


    def update_student(self, student_id: int, **kwargs)->None:
        student = self.find_student_by_id(student_id)
        if not student:
            print(Fore.RED + f"❌ Cannot update. Student with ID {student_id} not found.")
            logging.warning(f"Update failed. Student with ID {student_id} not found.")
            return

        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
                FileHandler.save_to_file(self.students)
                print(Fore.CYAN + f"🔄 Updated {key} to '{value}' for {student.name}")
                logging.info(f"Updated {key} for student ID {student_id} to '{value}'")
            else:
                print(Fore.YELLOW + f"⚠️  Invalid field: {key}")
                logging.warning(f"Attempted to update invalid field '{key}' for student ID {student_id}")


    def delete_student(self, student_id: int)->None:
        student = self.find_student_by_id(student_id)
        if not student:
            print(Fore.RED + f"❌ Cannot delete. Student with ID {student_id} not found.")
            logging.warning(f"Delete failed. Student with ID {student_id} not found.")
            return

        self.students.remove(student)
        FileHandler.save_to_file(self.students)
        print(Fore.MAGENTA + f"🗑️  Deleted student: {student.name} (ID: {student.id})")
        logging.info(f"Deleted student: {student.name} (ID: {student.id})")