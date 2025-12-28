# polymorphism -> multiple forms

# compile time 
# method overloading
# operator overloading


# class A:
#     def __init__(self):
#         self.age = 10
#         self.name = "hello"

#     def display(self, a, b):
#         return a + self.age

#     def display(self, b):
#         return b + self.name 

# obj1 = A()
# obj1.display(10, 10)
# print(obj1.display("gey"))

    

# 3x + 4
# -5x + 3
# -2x + 7

class A:
    def __init__(self, xterm, constant):
        self.a = xterm
        self.b = constant

    def __str__(self):
        return (f"{self.a}x + {self.b}")

    def __add__(self, other):
        return A(
            self.a + other.a, self.b + other.b

        )

ob1 = A(3, 4)
ob2 = A(-5, 2)
print(ob1 + ob2)
    


        






# runtime
