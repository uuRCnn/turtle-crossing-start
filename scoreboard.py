from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)

    def level_göster(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def level_artır(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(-55, 0)
        self.write("GAME OVER", font=FONT)
