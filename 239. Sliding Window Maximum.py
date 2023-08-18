from typing import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. new element is smaller than last queue element
        # 2. new element is bigger than part of queue
        # 3. current biggest element is out of queue

        queue: List[tuple(int, int)] = []
        for idx in range(k):
            if not queue or nums[idx] <= queue[-1][0]: queue.append((nums[idx], idx))
            elif nums[idx] >= queue[0][0]: queue = [(nums[idx], idx)]
            else:
                queue.pop(-1)
                while queue:
                    if nums[idx] > queue[-1][0]: queue.pop(-1)
                    else:
                        queue.append((nums[idx], idx))
                        break
                else: queue.append((nums[idx], idx))
        maxInSlidingWindow: List[int] = [queue[0][0]]

        for idx in range(k, len(nums)):
            # 1
            if nums[idx] <= queue[-1][0]: queue.append((nums[idx], idx))
            # 2
            elif nums[idx] >= queue[0][0]: queue = [(nums[idx], idx)]
            else:
                queue.pop(-1)
                while queue:
                    if nums[idx] > queue[-1][0]: queue.pop(-1)
                    else:
                        queue.append((nums[idx], idx))
                        break
                else: queue.append((nums[idx], idx))
            # 3
            if queue[0][1] <= idx - k: queue.pop(0)
            maxInSlidingWindow.append(queue[0][0])
        return maxInSlidingWindow