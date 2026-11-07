from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            tmp = "".join(sorted(word))
            groups[tmp].append(word)
        return list(groups.values())