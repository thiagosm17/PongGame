from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", False, "center", font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", font=('Courier', 30, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
