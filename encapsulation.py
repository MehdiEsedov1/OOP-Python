#Public
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def showInfos(self):
        print(self.name, " ", self.surname)

student1 = Student("Jasur", "Eynullayev")

#Protected
class Person:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

class Teacher(Person):
    def get_old(self):
        self._age += 1

    def show_infos(self):
        print(self._name, self._surname, self._age)

teacher1 = Teacher("Amil","Babayev", 50)

teacher1.get_old()
teacher1.show_infos()

#Private
class Car:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        self.__year = year

car = Car("BMW","2025")
car.set_name("Mercedes")
car_name = car.get_name()

print(car_name)