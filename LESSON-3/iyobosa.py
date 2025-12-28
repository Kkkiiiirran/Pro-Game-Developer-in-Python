import pgzrun
import pygame

WIDTH = 700
HEIGHT = 700

j = False

circles = []

def on_mouse_move(pos):
    circles.append(pos)

# def update(pos):
#     circles.append(pos)


def draw():
    global k
    screen.fill("white")
    for pos in circles:
        screen.draw.filled_circle((pos), 6, "black")

def update():
    pass



pgzrun.go()