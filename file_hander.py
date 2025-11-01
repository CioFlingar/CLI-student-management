import json
import os
from typing import List
from student import Student, InvalidStudentDataError

class FileHandler:
    FILE_PATH = "data.json"

    @staticmethod
    def save_to_file(students: List[Student])->None:
        data = [student.__dict__ for student in  students]
        with open(FileHandler.FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file()->List[Student]:
        if not os.path.exists(FileHandler.FILE_PATH):
            return []

        with open(FileHandler.FILE_PATH, 'r') as file:
            try:
                data = json.load(file)
                return[
                    Student(**item) for item in data
                ]
            except(json.JSONDecodeError, InvalidStudentDataError):
                return[]
