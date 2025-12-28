# class
# objects
# properties
# methods --> functions
# __init__()
# self

# class --> blueprint of the entity
# pen = turtle.Turtle()
# pen.color()
# pen.goto()





# blueprint of an entity
# object --> instance of a class
# properties
# methods
class Animal:
    # 
    def __init__(self):
        self.legs = 4 
        self.fur = True 
        self.ears = True
    
    def bark(self):
        print("dog barks")
    
    def swim(self):
        print("I can swim")


dog = Animal()
print(dog.legs)

bird = Animal()
bird.legs = 2

print(bird.legs)

bird.swim()
    

