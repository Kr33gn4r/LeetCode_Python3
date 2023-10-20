from typing import *
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr: List[int] = []
        self.idx: int = 0

        def goin(nest: [NestedInteger]):
            for lst in nest:
                if lst.getList():
                    goin(lst.getList())
                elif lst.getInteger() is not None:
                    self.arr.append(lst.getInteger())

        goin(nestedList)

    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx != len(self.arr)