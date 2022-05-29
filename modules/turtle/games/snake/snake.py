from random import randrange
from turtle import *
from gamebase import square


snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
apple_x = randrange(-200, 200)
apple_y = randrange(-200, 200)
aim_x = 10
aim_y = 0


def gameLoop():
    global apple_x, apple_y
    clear()
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])
    snake.pop(0)
    for i in range(len(snake)):
        square(snake[i][0], snake[i][1], 10, "black")

    square(apple_x, apple_y, 10, "red")
    ontimer(gameLoop, 300)
    update()


setup(420, 420, 0, 0)
hideturtle()
tracer(False)
gameLoop()
done()
