from turtle import Turtle
STARTING_POSITIONS = [(550, -20), (550, 0), (550, 20)]


class Paddle:

    def __init__(self):
        # self.parts = []
        self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.penup()
        paddle.turtlesize(stretch_wid=20, stretch_len=100)
        paddle.setpos(350, 0)
        paddle.setheading(90)
        # return paddle

    def up(self):
        for part in self.parts:
            part.forward(10)

    def down(self):
        for part in self.parts:
            part.backward(10)

