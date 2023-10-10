from turtle import Turtle
MOVE = False
ALIGN = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.color("white")
        self.write(f"Score: {self.score}", MOVE, ALIGN, FONT)
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", MOVE, ALIGN, FONT)

    def over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"GAME OVER!", MOVE, ALIGN, FONT)
