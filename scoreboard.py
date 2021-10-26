from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-255, 275)
        self.count_score()


    def count_score(self):
        self.clear()
        self.write(f"Level:{self.score}", align="center", font=("Courier", 15, "normal"))
        self.score += 1
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("game over", align="center", font=("Courier", 15, "normal"))

