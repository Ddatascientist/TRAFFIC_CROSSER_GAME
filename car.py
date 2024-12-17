from turtle import Turtle
import random

colors = ['red', 'green', 'purple','blue','violet','cyan2',"orange"]


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_manager()


    def car_pos(self):
        return [car.position() for car in self.all_cars]

    def car_manager(self):
        for i in range(0, 7):
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.setheading(180)
            new_car.shapesize(1,2.3)
            new_car.goto(random.randint(-70, 290), random.randint(-140, 150))
            new_car.color(random.choice(colors))
            self.all_cars.append(new_car)

    def car_move(self):
        for i in range (len(self.all_cars)):
            self.all_cars[i].forward(random.randint(5,10))
            if self.all_cars[i].xcor() < -280:
                self.all_cars[i].goto(random.randint(250, 290), random.randint(-145, 145))





