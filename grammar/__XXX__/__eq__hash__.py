"""
__eq__和__hash__
"""


class Item:
    def __init__(self, val):
        self.val = val

    # def __eq__(self, other):
    #     return self.val == other.val


first = Item("hello")
second = Item("hello")
print(first == second)
