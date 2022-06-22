from turtle import Turtle
STARTING_POSITIONS = [(550, -20), (550, 0), (550, 20)]


class Paddle:

    def __init__(self):
        self.parts = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.setheading(90)
        new_part.goto(position)
        self.parts.append(new_part)

    def up(self):
        for part in self.parts:
            part.forward(10)

    def down(self):
        for part in self.parts:
            part.backward(10)

