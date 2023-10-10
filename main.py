from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
score = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.again()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        flag = False
        score.over()
    elif snake.head.ycor() > 290 or snake.head.ycor() < -290:
        flag = False
        score.over()
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            flag = False
            score.over()
screen.exitonclick()

# # turtle_1 = Turtle(shape="square")
# # turtle_1.color("white")
# # turtle_1.penup()
# # turtle_1.goto(x=-40, y=0)
# # turtle_2 = Turtle(shape="square")
# # turtle_2.color("white")
# # turtle_2.penup()
# # turtle_2.goto(x=-20, y=0)
# # turtle_3 = Turtle(shape="square")
# # turtle_3.color("white")
# # turtle_3.penup()
# list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(list[::-1])