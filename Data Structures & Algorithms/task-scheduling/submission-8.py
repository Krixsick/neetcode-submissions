from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)

        counter = 0
        cooldown = deque()
        while heap or cooldown:
            counter += 1
            while cooldown and cooldown[0][0] <= counter:
                available_time, count = cooldown.popleft()
                heapq.heappush(heap, count)
            if heap:
                count = heapq.heappop(heap)
                count += 1
                if count < 0:
                    cooldown.append(((counter + n + 1), count))
        return counter