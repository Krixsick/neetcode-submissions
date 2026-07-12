from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        bucket_sort = [[] for i in range(len(nums) + 1)]

        for key, index in freq.items(): 
            bucket_sort[index].append(key)
        
        for row in range(len(nums), 0, -1):
            for value in bucket_sort[row]:
                if len(res) != k:
                    res.append(value)
        return res