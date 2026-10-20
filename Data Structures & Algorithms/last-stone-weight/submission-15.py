import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        -create a heap with neg numbers
        destroy both 
            if last_ele < sec_last_ele:
                heap.append(sec_last_ele)
            elif last_ele > sec_last_ele:
                heap.append(last_ele)
        """
        self.stones = [-stone for stone in stones]
        heapq.heapify(self.stones)
        while len(self.stones) > 1:
            last_element, second_last_element = heapq.heappop(self.stones), heapq.heappop(self.stones)
            if last_element < second_last_element: 
                tmp = -second_last_element + last_element
                heapq.heappush(self.stones, tmp)
            elif last_element > second_last_element:
                tmp = last_element - second_last_element
                heapq.heappush(self.stones, tmp)
        return -self.stones[0] if self.stones else 0