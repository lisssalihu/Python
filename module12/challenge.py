# BMI Calculator - OOP me pyetje për person tjetër

class Person:
    def __init__(self, name, surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_category(self):
        pass  # Polimorfizëm


class Student(Person):
    def get_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Nën peshë"
        elif bmi < 25:
            return "Peshë normale"
        elif bmi < 30:
            return "Mbipeshë"
        else:
            return "Obezitet"


class Adult(Person):
    def get_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Nën peshë"
        elif bmi < 25:
            return "Peshë normale"
        elif bmi < 30:
            return "Mbipeshë"
        else:
            return "Obezitet"


# MAIN PROGRAM
while True:
    print("\n=== BMI CALCULATOR ===")

    person_type = input("A je Student apo Adult? (s/a): ").lower()

    name = input("Emri: ")
    surname = input("Mbiemri: ")
    age = int(input("Mosha: "))
    weight = float(input("Pesha (kg): "))
    height = float(input("Gjatësia (m): "))

    if person_type == "s":
        person = Student(name, surname, age, weight, height)
    else:
        person = Adult(name, surname, age, weight, height)

    print("\n--- REZULTATI ---")
    print("Emri:", person.name, person.surname)
    print("Mosha:", person.age)
    print("BMI:", round(person.calculate_bmi(), 2))
    print("Kategoria:", person.get_category())

    again = input("\nA don me bo edhe ni person tjetër? (po/jo): ").lower()
    if again != "po":
        print("Programi u mbyll. Faleminderit!")
        break
