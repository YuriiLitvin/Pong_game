from turtle import Screen
from paddle import Paddle


screen = Screen()
paddle = Paddle()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

# screen.listen()
# screen.onkey(paddle.up, "Up")
# screen.onkey(paddle.down, "Down")





screen.exitonclick()
