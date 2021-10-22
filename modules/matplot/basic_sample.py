import numpy as np
from matplotlib import pyplot as plt


# x = list(range(1, 11))
# y = list(map(lambda x: x * 2 + 5, x))

"""用numpy更方便些"""
x = np.arange(1, 11)
y = 2 * x + 5


def sample1():
    """设置title和坐标轴说明，画图，保存图，展示图"""
    plt.title("Matplotlib demo")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x, y)
    plt.savefig('./sample.png', dpi=48)  # 保存图片，要在show之前调用
    plt.show()


def sample2():
    """设置画线的style，包括点的样式和颜色，--代表虚线，o代表点标记为o，ms是标记的大小，mec是标记外部颜色，mfc是标记内部颜色，b代表blue"""
    plt.plot(x, y, linestyle='--', linewidth='2.5', marker="o", ms=12, mec='g', mfc='r', color="b")  # 颜色也可以用'#8FBC8F'
    plt.plot(x, y, ".b")
    plt.show()


def plot_sin():
    """画sin曲线"""
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.title("sin wave")
    plt.plot(x, y)
    plt.show()


def plot_sin_cos():
    """在一张图上同时绘制sin和cos曲线"""
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.plot(x, y_sin, linestyle="--", label="sin wave")
    plt.plot(x, y_cos, label="cos wave")
    plt.title("sin cos wave")
    plt.legend(loc='best')  # 使用plt.legend()生成默认图例, 图例是集中于地图一角或一侧的地图上各种符号和颜色所代表内容与指标的说明
    plt.show()


def subplot1():
    """在同一张图中绘制两个子图"""
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.subplot(2, 1, 1)  # 建立 subplot 网格，高为 2，宽为 1，并激活第一个 subplot
    plt.plot(x, y_sin)
    plt.title("sin wave")

    plt.subplot(2, 1, 2)  # 将第二个 subplot 激活，并绘制第二个图像
    plt.plot(x, y_cos)
    plt.title("cos wave")
    plt.show()


def subplot2():
    """使用add_subplot的方式在绘制多个子图"""
    x = np.arange(0, 100)
    fig = plt.figure()
    ax1 = fig.add_subplot(221)  # 221表示两行两列的第一个位置
    ax1.plot(x, x)
    ax2 = fig.add_subplot(222)  # 222表示两行两列的第二个位置
    ax2.plot(x, -x)
    ax3 = fig.add_subplot(223)
    ax3.plot(x, x ** 2)
    ax4 = fig.add_subplot(224)
    ax4.plot(x, np.log(x))
    plt.show()


def plot_bar():
    """绘制条形图"""
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, label="bar1", align='center')
    plt.bar(x2, y2, label="bar2", color='g', align='center')
    plt.legend()
    plt.title("Bar graph")
    plt.show()


def plot_histogram():
    """绘制直方图"""
    a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
    hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
    # print(hist, bins)
    plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
    plt.title("histogram")
    plt.show()


def plot_stack():
    """绘制堆叠图"""
    days = [1, 2, 3, 4, 5]
    sleeping = [7, 8, 6, 11, 7]
    eating = [2, 3, 4, 3, 2]
    working = [7, 8, 7, 2, 2]
    playing = [8, 5, 7, 8, 13]
    plt.plot([], [], color='m', label='Sleeping', linewidth=5)
    plt.plot([], [], color='c', label='Eating', linewidth=5)
    plt.plot([], [], color='r', label='Working', linewidth=5)
    plt.plot([], [], color='k', label='Playing', linewidth=5)
    plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


def plot_scatter():
    """绘制散点图"""
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
    sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90])  # 点大小
    # colors = np.array(["red", "green", "black", "orange", "purple", "beige", "cyan", "magenta"])  # 点颜色
    # plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
    colors = np.array([0, 10, 30, 40, 60, 70, 90, 100])  # 使用颜色条
    plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=1)  # alpha是透明程度，1最高
    plt.title("Scatter")
    plt.colorbar()  # 显示颜色条
    plt.show()


def plot_pie():
    """绘制饼状图"""
    slices = [7, 2, 2, 13]
    activities = ['sleeping', 'eating', 'working', 'playing']
    cols = ['c', 'm', 'r', 'b']
    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=True,
            explode=(0, 0.1, 0, 0),  # 用explode拉出一个切片
            autopct='%1.1f%%')  # 显示百分比

    plt.title('Interesting Graph\nCheck it out')
    plt.show()


def plot_animation():
    """绘制动画"""
    from matplotlib import animation
    fig, ax = plt.subplots()  # 是一个简单写法，相当于fig = plt.figure(), ax = fig.add_subplot(111)
    x = np.arange(0, 2 * np.pi, 0.01)
    line, = ax.plot(x, np.sin(x))

    def animate(i):
        line.set_ydata(np.sin(x + i / 10.0))
        return line,

    def init():
        line.set_ydata(np.sin(x))
        return line,

    ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)
    plt.show()


def plot_3d():
    """绘制3D图像"""
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.arange(-10, 10, 0.25)
    y = np.arange(-10, 10, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    # z = r
    z = np.sin(r)

    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.contourf(x, y, z, zdir='z', offset=-2, cmap=plt.cm.hot)
    ax.set_zlim(-2, 2)

    plt.show()


if __name__ == "__main__":
    # sample1()
    # sample2()
    # plot_sin()
    # plot_sin_cos()
    # subplot1()
    # subplot2()
    # plot_bar()
    # plot_histogram()
    # plot_stack()
    plot_scatter()
    # plot_pie()
    # plot_animation()
    # plot_3d()
