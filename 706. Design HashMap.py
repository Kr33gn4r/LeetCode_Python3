from typing import *
class MyHashMap:

    def __init__(self):
        self.lst: List[List[int]] = [[]] * 1024

    def put(self, key: int, value: int) -> None:
        k, sk = key // 1024, key % 1024
        if not self.lst[k]:
            self.lst[k] = [-1] * 1024
        self.lst[k][sk] = value
        return None

    def get(self, key: int) -> int:
        k, sk = key // 1024, key % 1024
        if not self.lst[k]: return -1
        return self.lst[k][sk]

    def remove(self, key: int) -> None:
        k, sk = key // 1024, key % 1024
        if self.lst[k]: self.lst[k][sk] = -1
        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)