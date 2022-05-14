import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap


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
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # macos显示中文
    plt.scatter(x, y)
    for i in range(len(x)):
        plt.annotate(txt[i], xy=(x[i], y[i]), xytext=(x[i] + 0.1, y[i] + 0.1))  # 这里xy是需要标记的坐标，xytext是对应的标签坐标
    plt.show()


def high_dpi():
    """调整show的分辨率"""
    plt.rcParams['figure.dpi'] = 300  # 通过设置rcParams的分辨率，提高show的图片分辨率
    plt.plot((1, 2, 3), (4, 3, -1))
    plt.show()


def animation_1():
    fig = plt.figure()

    def f(x, y):
        return np.sin(x) + np.cos(y)

    x = np.linspace(0, 2 * np.pi, 120)
    y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
    # ims is a list of lists, each row is a list of artists to draw in the
    # current frame; here we are just animating one artist, the image, in
    # each frame
    ims = []
    for i in range(60):
        x += np.pi / 15.
        y += np.pi / 20.
        im = plt.imshow(f(x, y), animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    # ani.save('dynamic_images.mp4')

    plt.show()


def animation_2():
    def generate_data():
        a = np.arange(25).reshape(5, 5)
        b = 10 * np.random.rand(5, 5)
        return a - b

    def update(data):
        mat.set_data(data)
        return mat

    def data_gen():
        while True:
            yield generate_data()

    fig, ax = plt.subplots()
    mat = ax.matshow(generate_data())
    plt.colorbar(mat)
    ani = animation.FuncAnimation(fig, update, data_gen, interval=500, save_count=50)
    plt.show()


def animation_3():
    nrows, ncols = 20, 20
    mm = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]],
                  dtype=np.int)
    s = (0, 0)
    e = (7, 3)
    mm[s] = 2
    mm[e] = 2
    path = [(1, 0),
     (1, 1),
     (1, 2),
     (1, 3),
     (1, 4),
     (1, 5),
     (1, 6),
     (1, 7),
     (1, 8),
     (1, 9),
     (1, 10),
     (1, 11),
     (1, 12),
     (1, 13),
     (1, 14),
     (1, 15),
     (1, 16),
     (1, 17),
     (1, 18),
     (2, 18),
     (3, 18),
     (3, 17),
     (4, 16),
     (5, 16),
     (6, 16),
     (6, 15),
     (6, 14),
     (6, 13),
     (6, 12),
     (7, 11),
     (8, 11),
     (9, 11),
     (10, 11),
     (11, 11),
     (12, 11),
     (12, 10),
     (11, 9),
     (11, 8),
     (11, 7),
     (11, 6),
     (11, 5),
     (12, 4),
     (13, 4),
     (14, 4),
     (14, 3),
     (15, 2),
     (16, 2),
     (17, 2),
     (18, 2),
     (18, 1),
     (16, 0),
     (14, 1),
     (12, 0),
     (12, 1),
     (12, 2),
     (14, 2),
     (10, 3),
     (11, 2),
     (9, 4),
     (9, 5),
     (9, 6),
     (9, 7),
     (9, 8),
     (9, 9),
     (7, 10),
     (7, 9),
     (7, 8),
     (7, 7),
     (7, 6),
     (7, 5),
     (7, 4)]

    def init():
        plt.xticks(np.arange(0, nrows))
        plt.yticks(np.arange(0, ncols))
        for i in range(nrows):
            plt.axhline(y=0.5 + i, color='gray', linestyle='-')
        for i in range(nrows):
            plt.axvline(x=0.5 + i, color='gray', linestyle='-')

    fig, ax = plt.subplots()
    mat = ax.matshow(mm, cmap=ListedColormap(['w', 'k', 'r']))
    init()

    def update(frame):
        mm[path[frame]] = 3
        mat.set_data(mm)
        # mat.set_cmap(ListedColormap(['w', 'k', 'r', 'g']))
        # new_mat = ax.matshow(mm, cmap=ListedColormap(['w', 'k', 'r', 'g']))
        return mat,

    ani = animation.FuncAnimation(fig, func=update, frames=len(path), init_func=init, interval=100)
    plt.show()


if __name__ == "__main__":
    # plot_two_y_axis()
    # plot_ticks()
    # plot_grid()
    # plot_annotate()
    # high_dpi()
    # animation_1()
    # animation_2()
    animation_3()
    # animation_4()
