from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 2
        self.x_move = 2

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move = - self.y_move

    def change_direction(self):
        self.x_move = - self.x_move

    def origin(self):
        self.goto(0, 0)
        self.change_direction()
