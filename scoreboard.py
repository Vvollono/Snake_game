from turtle import Turtle

X = 0
Y = 280
FONT = ("Calibri", 13, "bold")
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(X, Y)
        self.write(f"Score:{self.point}", False, align=ALIGN, font=FONT)

    def score(self):
        self.point += 1
        self.clear()
        self.write(f"Score:{self.point}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=ALIGN, font=FONT)
