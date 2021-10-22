import numpy as np
import matplotlib.pyplot as plt


def plot_two_y_axis():
    """绘制两个y轴"""
    x = np.arange(0, 6)
    y1 = [30481, 12583, 51, 9, 2, 2]
    y2 = [0.0065, 0.016, 0.039, 0, 0, 0]

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()  # 做镜像处理
    ax1.plot(x, y1, 'g-')
    ax2.plot(x, y2, 'b--')

    ax1.set_xlabel('X data')  # 设置x轴标题
    ax1.set_ylabel('total_count', color='g')  # 设置Y1轴标题
    ax2.set_ylabel('bad_rate', color='b')  # 设置Y2轴标题

    plt.show()


def plot_ticks():
    """更改x轴和y轴的刻度频率"""
    x = [0, 5, 9, 10, 15]
    y = [0, 1, 2, 3, 4]
    plt.plot(x, y)
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.show()


def plot_grid():
    """绘制网格线"""
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 4, 9, 16])

    plt.title("Grid Test")
    plt.xlabel("x - label")
    plt.ylabel("y - label")
    plt.plot(x, y)
    plt.grid(axis='both', color='r', linestyle='--', linewidth=0.5)  # axis可选值为x、y、both
    plt.show()


def plot_annotate():
    """绘制标签"""
    x = [2, 4, 6, 7, 8, 5, 4, 3]
    y = [3, 6, 5, 8, 4, 3, 2, 4]
    txt = ['我', '今', '晚', '上', '吃', '了', '个', '鲸']
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.scatter(x, y)
    for i in range(len(x)):
        plt.annotate(txt[i], xy=(x[i], y[i]), xytext=(x[i] + 0.1, y[i] + 0.1))  # 这里xy是需要标记的坐标，xytext是对应的标签坐标
    plt.show()


if __name__ == "__main__":
    # plot_two_y_axis()
    # plot_ticks()
    # plot_grid()
    plot_annotate()
