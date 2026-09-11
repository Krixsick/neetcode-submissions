from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        -sliding window approach
        -get Counter(s1)
        -for r in range(len(s2)):
            add to dict
            if dict2 == dict1:
                return True
            while loop runs if dict1 == dict2 and keys dont match
                remove from dict2 
                l += 1
        return False
        """
        l = 0
        dict2 = {}
        dict1 = Counter(s1)
        for r in range(len(s2)):
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    del dict2[s2[l]]
                l += 1
            if dict2 == dict1:
                return True

        return False