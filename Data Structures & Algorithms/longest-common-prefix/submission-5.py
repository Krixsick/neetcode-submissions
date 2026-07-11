class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for letter_index in range(len(prefix)):
            for word in strs:
                if letter_index == len(word) or prefix[letter_index] != word[letter_index]:
                    return prefix[:letter_index]
        return prefix