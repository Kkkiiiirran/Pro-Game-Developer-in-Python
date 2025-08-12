'''
def greet():
    print("Hello to you")
    print("My Name is JARVIS")
    print("May I know your name: ")
    userName = input()


#How to call the function
greet()
'''

#How to make a class

class Student():
    #properties/ attributes
    name = ""
    age = 12
    schoolclass = "6th A"
    house = "Sapphire"
    classteacher = "Poonam Ma'am"
    school = "abc"

    #constructor
    def __init__(self):
        print("Making a new student")

    #Another Function
    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print ("Please enter the name of the student")
        self.name = input()

    #Another Function
    def show_Details(self):
        print("The details of student are:")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)
    
#Student class definition  is over
#Making 2 objects/ instances of Student class
Varnika = Student()
Surabhi = Student()

Surabhi.change_details()
Surabhi.show_Details()


    
    