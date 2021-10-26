from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_shape(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.all_car.append(car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def speed_cars(self):
        self.car_speed += MOVE_INCREMENT












