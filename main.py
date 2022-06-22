from turtle import Screen
from paddle import Paddle


screen = Screen()
paddle = Paddle()

screen.setup(width=1200, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")





screen.exitonclick()
