class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for ind1 in range(len(nums)):
            product = 1
            for ind2 in range(len(nums)):
                if ind2 == ind1:
                    continue 
                product *= nums[ind2]
            res.append(product)
        return res