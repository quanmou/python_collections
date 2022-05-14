import numpy as np
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris, load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def compare_tsne_pca():
    # 加载数据集
    iris = load_iris()
    print(iris.data.shape)  # (150,4)，共有150个例子， 数据的类型是numpy.ndarray
    print(iris.target.shape)  # (150,)，对应的标签有0,1,2三种
    tsne = TSNE(n_components=2, learning_rate=100).fit_transform(iris.data)  # 使用TSNE进行降维处理。从4维降至2维。
    pca = PCA().fit_transform(iris.data)  # 使用PCA 进行降维处理

    plt.figure(figsize=(12, 6))  # 设置画布的大小

    plt.subplot(121)
    plt.title("tsne")
    plt.scatter(tsne[:, 0], tsne[:, 1], c=iris.target)

    plt.subplot(122)
    plt.scatter(pca[:, 0], pca[:, 1], c=iris.target)
    plt.title("pca")

    plt.colorbar()
    plt.show()


def scatter_with_label():
    """带标签的散点图"""
    digits = load_digits(n_class=6)
    X = digits.data  # 1083*64
    y = digits.target  # 1083 max(y)=5

    tsne = TSNE(n_components=2, init='pca', random_state=0)
    X_tsne = tsne.fit_transform(X)

    x_min, x_max = np.min(X_tsne, 0), np.max(X_tsne, 0)
    X_tsne = (X_tsne - x_min) / (x_max - x_min)

    for i in range(X_tsne.shape[0]):
        plt.text(X_tsne[i, 0], X_tsne[i, 1],
                 str(y[i]),
                 color=plt.cm.Set1(y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.title("t-SNE 2D")
    plt.show()


def scatter_with_label_3d():
    """三维带标签散点图"""
    digits = load_digits(n_class=6)
    X = digits.data  # 1083*64
    y = digits.target  # 1083 max(y)=5

    tsne = TSNE(n_components=3, init='pca', random_state=0)
    X_tsne = tsne.fit_transform(X)

    # 坐标缩放到[0,1]区间
    x_min, x_max = np.min(X_tsne, axis=0), np.max(X_tsne, axis=0)
    X_tsne = (X_tsne - x_min) / (x_max - x_min)

    # 降维后的坐标为（X_tsne[i, 0], X_tsne[i, 1], X_tsne[i,2]），在该位置画出对应的digits
    ax = plt.axes(projection='3d')
    for i in range(X_tsne.shape[0]):
        ax.text(X_tsne[i, 0], X_tsne[i, 1], X_tsne[i, 2],
                str(digits.target[i]),
                color=plt.cm.Set1(y[i] / 10.),
                fontdict={'weight': 'bold', 'size': 9})

    plt.title("t-SNE 3D")
    plt.show()


scatter_with_label_3d()
