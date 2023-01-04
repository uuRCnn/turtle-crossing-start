from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.hideturtle()
        self.cars_hızı = STARTING_MOVE_DISTANCE

    def creat_car(self):
        random_count = random.randint(1, 6)
        if random_count == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(320, random.randint(-250, 250))
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.cars_hızı)

    def cars_spead(self):
        self.cars_hızı += MOVE_INCREMENT
