# class Quadratic:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __add__(self, other):

#         return Quadratic(
#             self.a + other.a,
#             self.b + other.b,
#             self.c + other.c
#         )

#     def __str__(self):
      
#         return f"{self.a}x² + {self.b}x + {self.c}"


# q1 = Quadratic(1, 2, 3)   
# q2 = Quadratic(2, 3, 4)   

# q3 = q1 + q2
# print(q3)


from multipledispatch import dispatch

class Calculator:

  
    @dispatch(int, int)
    def product(self, a, b):
        result = a * b
        print(f"Product of two integers: {result}")

    
    @dispatch(int, int, int)
    def product(self, a, b, c):
        result = a * b * c
        print(f"Product of three integers: {result}")


    @dispatch(float, float, float)
    def product(self, a, b, c):
        result = a * b * c
        print(f"Product of three floats: {result}")


# Example usage
calc = Calculator()
calc.product(2, 3)         
calc.product(2, 3, 4)     
calc.product(2.2, 3.4, 2.3)  
