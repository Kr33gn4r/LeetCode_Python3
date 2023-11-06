from heapq import heappop, heappush
class SeatManager:

    def __init__(self, n: int):
        self.q = []
        self.index = 0

    def reserve(self) -> int:
        if self.q:
            return heappop(self.q)
        else:
            self.index += 1
            return self.index

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)