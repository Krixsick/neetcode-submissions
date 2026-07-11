from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for element in strs:
            lst = [0] * 26
            for character in element:
                lst[ord(character) - ord('a')] += 1
            lst = tuple(lst)
            groups[lst].append(element)
        return list(groups.values())