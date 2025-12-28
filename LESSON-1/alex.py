class Student:

    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    
    def display(self):
        print(self.name)
        print(self)



# instance of the class
obj1 = Student("alex", 16)
obj2 = Student("david", 26)
obj2.display()
