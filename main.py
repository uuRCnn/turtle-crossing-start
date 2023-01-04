import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.back_move, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.creat_car()
    car_manager.move_cars()
    scoreboard.level_göster()

    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.level_up()
        car_manager.cars_spead()
        scoreboard.level_artır()

screen.exitonclick()
