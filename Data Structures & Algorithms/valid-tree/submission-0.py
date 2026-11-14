from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = [[] for i in range(n)]

        for first, second in edges:
            nodes[first].append(second)
            nodes[second].append(first)
        visited = {0}
        queue = deque([(0, -1)])
        while queue:
            node, parent = queue.popleft()
            for neighbour in nodes[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False
                visited.add(neighbour)
                queue.append((neighbour, node))
        return len(visited) == n