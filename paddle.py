from turtle import Turtle
WIDTH = 1
HEIGHT = 5


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(WIDTH, HEIGHT)
        self.setpos(position)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
