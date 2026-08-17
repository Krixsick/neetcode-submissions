class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l_largest = 0
        l_arr = [0] * len(height)
        r_largest = 0
        r_arr = [0] * len(height)
        for r in range(len(height)):
            l_largest = max(l_largest, height[r])
            l_arr[r] = l_largest
        for l in range(len(height) - 1, -1, -1):
            r_largest = max(r_largest, height[l])
            r_arr[l] = r_largest
        for ind in range(1, len(height) - 1):
            tmp = min(l_arr[ind - 1], r_arr[ind + 1]) - height[ind]
            if tmp > 0:
                total += tmp
        return total
            

