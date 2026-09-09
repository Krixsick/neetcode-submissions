class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        -two arrays, len(nums1) = m and len(nums2) = n
        -return the median value between the two
        -brute force
            -we can combine nums1 and nums2 tgt by looping through
            and checking which value is lower or higher
            -if it's even or odd we do something
            -odd
                -return len(nums) // 2
            -even
                -get positions by ind = len(nums) // 2  
                -return (nums[ind] + nums[ind - 1]) / 2
            
        """
        sorted_arr = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                sorted_arr.append(nums1[p1])
                p1 += 1
            else:
                sorted_arr.append(nums2[p2])
                p2 += 1
        if p1 >= len(nums1):
            sorted_arr.extend(nums2[p2:])
        if p2 >= len(nums2):
            sorted_arr.extend(nums1[p1:])
        
        length = len(sorted_arr) % 2
        if length == 1:
            ind = len(sorted_arr) // 2
            return sorted_arr[ind]
        else:
            ind = len(sorted_arr) // 2
            value = (sorted_arr[ind] + sorted_arr[ind - 1]) / 2
            return value
        