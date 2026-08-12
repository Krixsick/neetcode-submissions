class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        -indexes a,b,c,d are distinct and are inbetween 0 and len(nums)
        -when their values are added tgt they should equal target
        -how to solve this?
            -similar to 3sum but just with an added num
                -sort the numbers
                -lets say index1 starts at the beginning and index2
                starts at the end, l = index + 1 and r = index2 - 1?
        -brute force would be
            start from beginning and then start from end, and then do 
            two pointers and it'll be like o(n^3) LOL
        '''
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    added_val = nums[i] + nums[j] + nums[l] + nums[r]
                    if added_val == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif added_val < target:
                        l += 1
                    else:
                        r -= 1
        return res