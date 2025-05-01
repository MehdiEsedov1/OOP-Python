class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"

    def showInfos(self):
        print("Name: ",self.name, "/n", "Surname: ", self.surname,"/n", "Age: ", self.age)

student = Student("Jasur", "Eynullayev",20)
student.age = 21

student.showInfos()
print(student)

#Empty class
class Person:
  pass