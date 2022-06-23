from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        step = 10
        x_cor = self.xcor()
        y_cor = self.ycor()
        x_cor += step * 1.3
        y_cor += step
        self.setpos(x_cor, y_cor)
