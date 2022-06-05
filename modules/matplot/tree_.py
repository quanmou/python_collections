"""
pip install Tree
Refer to: https://codeantenna.com/a/3TLZ3IlcKI
"""

# coding=utf-8
from Tree.core import Tree
from math import radians as rad
from PIL import Image


def main():
    branches = ((.5, rad(-30)), (.6, rad(30)), (.4, rad(60)))
    tree = Tree(pos=(0, 0, 0, -500), branches=branches)
    tree.grow(10)
    tree.move_in_rectangle()
    im = Image.new("RGB", tree.get_size(), (239, 239, 239))
    tree.draw_on(im, (85, 25, 0, 128, 53, 21), (0, 62, 21), 10)
    im.show()


if __name__ == '__main__':
    main()
