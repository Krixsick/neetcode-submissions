from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def one_letter_apart(current, candidate):
            differences = 0
            for a, b in zip(current, candidate):
                if a != b:
                    differences += 1
            return differences == 1
        
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            current, length = queue.popleft()
            if current == endWord:
                return length
            for word in wordList:
                if word not in visited and one_letter_apart(current, word):
                    visited.add(word)
                    queue.append((word, length + 1))
        return 0

        