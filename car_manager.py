from turtle import Turtle, Screen
import random

COLORS = ["images/Blue car.gif", "images/green car.gif", "images/orange car.gif", "images/yellow car.gif", "images/red car.gif", "images/purple car.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()
screen = Turtle().getscreen()
screen.register_shape('images/Blue car.gif')
screen.register_shape('images/green car.gif')
screen.register_shape('images/red car.gif')
screen.register_shape('images/yellow car.gif')
screen.register_shape('images/purple car.gif')
screen.register_shape('images/orange car.gif')

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            random_cars = random.choice(COLORS)
            new_car = Turtle(random_cars)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT