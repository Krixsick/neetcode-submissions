from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        required = Counter(t)
        counts = {}
        have = 0
        need = len(required)
        l = 0
        minimum = float("inf")
        best_start = 0
        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            if char in required and counts[char] == required[char]:
                have += 1
            while have == need:
                length = r - l + 1
                if length < minimum:
                    minimum = length
                    best_start = l
                left_char = s[l]
                counts[left_char] -= 1
                if (left_char in required and counts[left_char] < required[left_char]):
                    have -= 1
                l += 1
        if minimum == float("inf"):
            return ""
        return s[best_start:best_start + minimum]