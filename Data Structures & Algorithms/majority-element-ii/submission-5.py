from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        -arr size n
        -find elements appearing more than 3 times
        """
        if not nums:
            return []
        seen = Counter(nums)
        freq = int(len(nums) / 3)
        res = []
        for key, value in seen.items():
            if value > freq:
                res.append(key)
        return res

