from turtle import Turtle

class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.starter()

    def starter(self):
        self.goto(0, -180)

    def movement(self):
        self.forward(5)

    def bacment(self):
        self.forward(-5)
