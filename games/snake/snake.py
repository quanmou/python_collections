# 引用函数
from turtle import *
from time import sleep
import random

# 定义变量
snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]  # 初始化蛇的位置
# 初始化苹果的位置
apple_x = random.randrange(-20, 18) * 10
apple_y = random.randrange(-19, 19) * 10
# 如果苹果生成在蛇身上 那么重新生成
while [apple_x, apple_y] in snake:
    apple_x = random.randrange(-20, 18) * 10
    apple_y = random.randrange(-19, 19) * 10
# 初始化蛇的前进方向
aim_x = 0
aim_y = 10


# 定义函数
def square(x, y, size, color_name):
    """
    画方块
    :param x: 左上角x坐标
    :param y: 左上角y坐标
    :param size: 方块边长
    :param color_name: 方块填充颜色
    :return:
    """
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()

    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    end_fill()


def inside_wall():
    """
    判断蛇头是否在墙里
    """
    return (snake[-1][0] == -210 or snake[-1][0] == 190) or (snake[-1][1] == -200 or snake[-1][1] == 200)


def inside_snake():
    """
    判断蛇头是否咬到自己
    """
    for n in range(len(snake) - 1):
        if snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False


def change(x, y):
    """
    改变蛇头行进方向
    """
    global aim_x, aim_y

    if aim_x + x != 0 or aim_y + y != 0:  # 判断是否与当前行进方向相反
        aim_x = x
        aim_y = y


def game_loop():
    """
    游戏每帧过程
    """
    global apple_x, apple_y, aim_x, aim_y, snake
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])  # 在行进方向前一格添加新蛇头
    print(snake[-1])  # 打印蛇头坐标

    # 判断蛇头是否吃到苹果并进行相应的操作
    if snake[-1][0] == apple_x and snake[-1][1] == apple_y:
        # 吃到了苹果后生成新苹果
        apple_x = random.randrange(-20, 18) * 10
        apple_y = random.randrange(-19, 19) * 10
        # 如果苹果生成在蛇身上 那么重新生成
        while [apple_x, apple_y] in snake:
            apple_x = random.randrange(-20, 18) * 10
            apple_y = random.randrange(-19, 19) * 10
    else:
        snake.pop(0)  # 没吃到苹果保持蛇长度不变

    # 游戏的两种结束判断：1.蛇头撞墙。 2.蛇咬到自己
    if inside_wall() or inside_snake():
        square(snake[-1][0], snake[-1][1], 10, "red")  # 撞墙提示
        update()
        # 三秒后重置游戏
        sleep(3)
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
        apple_x = random.randrange(-20, 18) * 10
        apple_y = random.randrange(-19, 19) * 10
        aim_x = 0
        aim_y = 10

    clear()
    square(-210, -200, 410, "black")  # 画黑布
    square(-200, -190, 390, "white")  # 画白布

    # 画蛇
    for i in range(len(snake)):
        square(snake[i][0], snake[i][1], 10, "green")
    square(apple_x, apple_y, 10, "red")  # 画苹果
    ontimer(game_loop, 100)  # 每隔100毫秒，循环当前函数一次
    update()  # 将作画结果更新到屏幕上


def main():
    # 主程序
    setup(420, 420, 0, 0)  # 设置画布
    hideturtle()  # 隐藏箭头
    tracer(False)  # 隐藏轨迹
    # 监听键盘操作
    listen()
    onkey(lambda: change(0, 10), "w")
    onkey(lambda: change(-10, 0), "a")
    onkey(lambda: change(0, -10), "s")
    onkey(lambda: change(10, 0), "d")
    # 开始游戏
    game_loop()
    done()


if __name__ == "__main__":
    main()
