# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxsum = 0
        def calc_diameter(root):
            if not root:
                return 0

            left = calc_diameter(root.left)
            right = calc_diameter(root.right)

            self.maxsum = max(self.maxsum, left + right)

            return 1 + max(left,right)
        
        calc_diameter(root)
        return self.maxsum

        
