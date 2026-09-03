import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            middle = (l + r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / middle)
            if total_time > h:
                l = middle + 1
            else:
                res = middle
                r = middle - 1
        return res