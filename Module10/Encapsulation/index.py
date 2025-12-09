from module8.student import student_1


class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

student_1=Student("Daris",15)

print("Name:",student_1.get_name())

student_1.set_name("Blin")

print("Name:",student_1.get_age())
student_1.set_age("16")
print("Age:",student_1.get_age())