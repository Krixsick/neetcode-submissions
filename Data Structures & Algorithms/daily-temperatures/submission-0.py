from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        for index, num in enumerate(temperatures):
            while s and s[-1][1] < num:
                s_ind, s_num = s.pop()
                res[s_ind] = index - s_ind
            else:
                s.append([index, num])
        return res

        