import math
from dataclasses import dataclass, field, asdict, astuple, is_dataclass
from typing import Any, List


@dataclass
class Lang:
    """
    a dataclass that describes a programming language

    使用了装饰器dataclass的Lang相当于
    class Lang:
        def __init__(self, name: str = 'python',
                     strong_type: bool = True,
                     static_type: bool = False,
                     age: int = 28):
            self.name = name
            self.strong_type = strong_type
            self.static_type = static_type
            self.age = age
    """
    name: str = 'python'
    strong_type: bool = True
    static_type: bool = False
    age: int = 28


@dataclass
class WithoutExplicitTypes:
    """
    在数据类中定义字段时，必须添加某种类型提示。 如果没有类型提示，该字段将不是dataclass类的一部分。
    但是，如果您不想向dataclass类添加显式类型，请使用typing.Any
    """
    name: Any
    value: Any = 42


@dataclass
class FloatNumber:
    """
    可以使用__post_init__函数处理__init__初始化后的事情
   """
    val: float = 0.0

    def __post_init__(self):
        self.decimal, self.integer = math.modf(self.val)


@dataclass
class InventoryItem:
    """
    Class for keeping track of an item in inventory.

    使用dataclass有一些好处，它比namedtuple更灵活。同时因为它是一个常规的类，所以我们可以像给类定义方法一样给dataclass类定义方法。
    """
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


@dataclass
class Base:
    """
    dataclass可以享受继承带来的便利
    """
    x: float = 25.0
    y: int = 0


@dataclass
class C(Base):
    """
    如果子类中的field与基类同名，那么子类将会无条件覆盖基类。
    """
    z: int = 10
    x: int = 15


@dataclass
class C:
    """
    对于list，当复制它时只是复制了一份引用，所以像dataclass里那样直接复制给实例的做法的危险而错误的，为了保证使用list时的安全性，应该这样做:
    当初始化C的实例时就会调用list()而不是直接复制一份list的引用，数据污染得到了避免。
    c1 = C()
    c1.my_list = [1, 2, 3]
    print(c1.my_list)  # [1, 2, 3]
    c2 = C()
    print(c2.my_list)  # []
    """
    my_list: List[int] = field(default_factory=list)


"""
`dataclasses`模块中提供了一些常用函数供我们处理数据类。
"""
print(asdict(Lang()))  # 将数据转为字典
print(astuple(Lang()))  # 将数据转为元组
print(is_dataclass(Lang))
print(is_dataclass(Lang()))
