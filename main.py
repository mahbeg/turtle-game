import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(turtle.move, "Up")
screen.onkey(turtle.move_back, "Down")


T = Turtle()
T.hideturtle()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_shape()
    car.move_car()


    if turtle.ycor() == 270:
        score_board.count_score()
        turtle.goto(0, -280)
        car.speed_cars()



    for car_item in car.all_car:
        if car_item.distance(turtle) < 20:
            # T.write("Game over", align="center", font=("Courier", 15, "normal"))
            score_board.game_over()
            game_is_on = False





screen.exitonclick()