class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -given an array of nums return triplets where it equals 0
            -no duplicate subarrays and return a subarray of len 3

        """ 
        nums.sort()
        res = []
        for index in range(0, len(nums)):
            l, r = index + 1, len(nums) - 1
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            while l < r:
                curr_res = nums[l] + nums[index] + nums[r]
                if curr_res == 0:
                    res.append([nums[index], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif curr_res < 0:
                    l += 1
                else:
                    r -= 1
        return res
