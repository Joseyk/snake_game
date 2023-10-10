from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed("fastest")
        x = random.randrange(-280, 280)
        y = random.randrange(-280, 280)
        self.goto(x, y)
        self.again()

    def again(self):
        x = random.randrange(-280, 280)
        y = random.randrange(-280, 280)
        self.goto(x, y)
