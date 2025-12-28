








class A:
    def __init__(self):
        self.color = "red"

class B(A):
    def __init__(self):
        super().__init__()
        self.age = 20


obj = B()
print(obj.color)