import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        self.distance = []
        result = []
        heapq.heapify(self.distance) 
        for point in points:
            distance = math.sqrt((point[0])**2 + (point[1]**2))
            heapq.heappush(self.distance, [distance, point])
        for amount in range(k):
            tmp = heapq.heappop(self.distance)
            result.append(tmp[1])
        return(result)