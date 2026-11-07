from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        for key, value in count.items():
            bucket[value].append(key)
        
        for i in range(len(nums), -1, -1):
            for number in bucket[i]:
                res.append(number)
                if len(res) == k:
                    return res