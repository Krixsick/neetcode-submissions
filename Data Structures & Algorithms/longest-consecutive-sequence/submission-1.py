class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        if len(nums) == 0:
            return 0
        lcs = 0
        for number in nums:
            seen.add(number)
        for number in nums:
            temp = 0
            prev_val = number - 1
            next_val = number + 1
            if prev_val in seen:
                continue
            elif prev_val not in seen:
                while next_val in seen:
                    temp += 1
                    next_val += 1
                    lcs = max(lcs, temp)
        return lcs + 1
                
        


          