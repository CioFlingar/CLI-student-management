class InvalidStudentDataError(Exception):
    """Raised when a student has invalid data."""
    pass


class Student:
    def __init__(self, id: int, name: str, age: int, course: str, grade: float, email: str, phone: str) -> None:

        if not name.strip():
            raise InvalidStudentDataError("Name cannot be empty.")
        if age <= 0:
            raise InvalidStudentDataError("Age can not be under 0.")
        if not (0.0 <= grade <= 4.0):
            raise InvalidStudentDataError("Grade needs to be between the range of 0.0 to 4.0.")
        if "@" not in email:
            raise InvalidStudentDataError("Your email is not valid.")
        if not (10<= len(phone) <= 15):
            raise InvalidStudentDataError("Use a 10 to 15 digit valid phone number.")


        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        self.email = email
        self.phone = phone

    def __repr__(self)-> str:
        return f"Student(id={self.id}, name='{self.name}', age={self.age}, course='{self.course}', grade={self.grade}, email='{self.email}', phone='{self.phone}')"
