# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        -differnce is more than 2
        """
        is_balance = True
        def balance(root):
            nonlocal is_balance
            if root is None:
                return 0
            left = balance(root.left)
            right = balance(root.right)
            if (abs(right - left)) >= 2:
                is_balance = False
            return max(left, right) + 1
        balance(root)
        return is_balance