from turtle import Turtle, Screen
from user import Crosser
from car import Car
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 400)
screen.tracer(0)
cars = Car()
crosser = Crosser()
count = Scoreboard()

start = screen.textinput("START GAME", "PRESS ANY KEY TO START")
screen.listen()
screen.onkeypress(fun=crosser.movement, key="Up")
screen.onkeypress(fun=crosser.bacment, key="Down")
game_on = False
if start:
    game_on = True

game_speed = 0.1

while game_on:
    time.sleep(game_speed)
    screen.update()
    crosser.setheading(90)
    cars.car_move()

    for posit in cars.car_pos():
        if crosser.distance(posit) < 27:
            count.gameover()
            game_on = False


    #  score count
    if crosser.ycor() > 170:
        count.score_count()
        crosser.starter()
        game_speed *= 0.9











screen.exitonclick()