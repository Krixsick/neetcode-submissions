# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(root, max_value):
            nonlocal total
            if root is None:
                return 
            new_max = max(max_value, root.val)
            left = dfs(root.left, new_max)
            right = dfs(root.right, new_max)
            if root.val >= new_max:
                total += 1
        dfs(root, root.val)
        return total 