import heapq
class MedianFinder:

    def __init__(self):
        self.result = []
        # heapq.heapify(self.result)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.result, num)
        self.result.sort()

    def findMedian(self) -> float:
        middle = len(self.result) // 2
        if len(self.result) % 2 == 0:
            tmp = (self.result[middle - 1] + self.result[middle]) / 2
            return tmp
        else:
            return self.result[middle]
            
        