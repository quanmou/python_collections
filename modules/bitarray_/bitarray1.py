from bitarray import bitarray
import hashlib


class BitMap:
    def __init__(self, size):
        self.size = size
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        offset = int(hashlib.sha1(s.encode()).hexdigest(), 16) % self.size
        self.bit_array[offset] = 1

    def lookup(self, s):
        offset = int(hashlib.sha1(s.encode()).hexdigest(), 16) % self.size
        if self.bit_array[offset] == 0:
            return "No"
        return "Probably"


bm = BitMap(500000)
bm.add("test")
bm.add("hello")
print(bm.lookup("test"))  # Probably
print(bm.lookup("hello"))  # Probably
print(bm.lookup("world"))  # No
print(bm.bit_array.count())  # 2
