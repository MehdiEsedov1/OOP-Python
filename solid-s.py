#Bad example
class Student1:
    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        print(f"{self.name} saved to database")

    def print_details(self):
        print(f"Student: {self.name}")

#Good example
class Student2:
    def __init__(self, name):
        self.name = name

class StudentRepository:
    def save(self, student):
        print(f"{student.name} saved to database")

class StudentPrinter:
    def print(self, student):
        print(f"Student: {student.name}")
