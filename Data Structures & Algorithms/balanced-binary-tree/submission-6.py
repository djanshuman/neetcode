# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def check_isBalanced(root):
            if not root:
                return 0

            left = check_isBalanced(root.left)
            right = check_isBalanced(root.right)

            if left < 0:
                return -1

            if right < 0:
                return -1

            if abs(left -right) > 1:
                return -1

            return 1 + max(left, right)
            
        return check_isBalanced(root) != -1