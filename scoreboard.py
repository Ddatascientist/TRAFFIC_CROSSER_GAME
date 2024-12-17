from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scores = 0
        self.write_on_screen()

    def write_on_screen(self):
        self.hideturtle()
        self.penup()
        self.goto(-280, 180)
        self.write(arg=f"score: {self.scores}", align="left", font=('courier', 12, "bold"))

    def gameover(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=('courier', 15, "bold"))

    def score_count(self):
        self.scores += 50
        self.reset()
        self.write_on_screen()
