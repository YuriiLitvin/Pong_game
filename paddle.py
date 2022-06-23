from turtle import Turtle
WIDTH = 1
HEIGHT = 5
# X_POS = 350
# Y_POS = 0


class Paddle:

    def __init__(self, position):
        self.position = position
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.turtlesize(WIDTH, HEIGHT)
        self.paddle.setpos(position)
        self.paddle.setheading(90)

    def up(self):
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)
