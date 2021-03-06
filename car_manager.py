from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_create = random.randint(1, 6)
        if random_create == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x=280, y=random.randint(-200, 200))
            new_car.move_speed = 0.1
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT
