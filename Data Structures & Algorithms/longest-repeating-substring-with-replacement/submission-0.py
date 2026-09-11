class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            -s -> only eng characters
            -k -> can choose k characters to replace with anything
            -find longest substring of one distinct character
                - have a set storing everything we add to it
                - we use sliding window tech
                - check if s[r] is in set if it is, we increase maximum
                - if not we first we will increment a counter and if
                <= k, we keep looping and increasing maximum
                - otherwise if it passes k, we reset counter and continue finding elements that could make us the longest substring
        """
        l = 0
        maximum = 0
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while ((r - l + 1) - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1
            maximum = max(maximum, (r - l + 1))
        return maximum

