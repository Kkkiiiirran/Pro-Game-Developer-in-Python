import pgzrun
import random


WIDTH = 300
HEIGHT = 300

def draw():
    w = 100
    h = 100
    r = 255
    g = 0
    b = random.randint(120,255)

    for i in range(30):
        rect = Rect((0, 0), (w, h))  
        rect.center = (100, 100) 
        screen.draw.rect(rect, (r, g, b))
        w-=10
        h-=10
        r-=5
        g+=5

    
pgzrun.go()

# import pgzrun
# import random

# WIDTH = 300
# HEIGHT = 300

# def draw():
#     w = 300
#     h = 100
#     radius = 100
#     r = 255
#     g = 0
#     b = random.randint(120,255)
#     for i in range(20):
#         # rect = Circle((0,0), 50,(w, h))
#         # rect.center = 150,150
#         screen.draw.circle((150,150), radius,(r,g,b))

#         r-=10
#         g+=10

#         radius-=2
#         # w-=10
#         # h+=10

# pgzrun.go()


