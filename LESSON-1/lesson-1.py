class Student():
    name = "Priya"
    age = 12
    grade = "6th A"
    house = "Sapphire"
    class_teacher = "Kiran"

    def __init__(self):
        print("Making a new student")
    
    def change_age(self):
        self.age = int(input("Please enter your age"))
    
    def display(self):
        print("Deatils of the student")
        print(self.name)
        print(self.age)
        print(self.grade)
        print(self.house)
        print(self.class_teacher)

Varnika = Student()
Priya = Student()

Priya.change_age()
Priya.display()
