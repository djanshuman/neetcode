# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_balanced(root):
            if not root:
                return 0

            left = dfs_balanced(root.left)
            right= dfs_balanced(root.right)

            if left < 0:
                return -1

            if right < 0:
                return -1
            
            if abs(left - right) >= 2:
                return -1

            if abs(left - right) > 1:
                return False

            return max(left, right) + 1

        return dfs_balanced(root) != -1