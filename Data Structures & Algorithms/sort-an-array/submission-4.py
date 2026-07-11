class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            l, r = 0, 0
            sorted_array = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sorted_array.append(left[l])
                    l += 1
                else:
                    sorted_array.append(right[r])
                    r += 1
            while l < len(left):
                sorted_array.append(left[l])
                l += 1
            while r < len(right):
                sorted_array.append(right[r])
                r += 1
            return sorted_array 

        return merge_sort(nums)
            