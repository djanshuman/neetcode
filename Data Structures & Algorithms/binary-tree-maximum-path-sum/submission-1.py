# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]
        def dfs_maxsum(root):
            if not root:
                return 0

            left = dfs_maxsum(root.left)
            right = dfs_maxsum(root.right)

            left = max(left, 0)
            right = max(right, 0)
            self.res[0] = max(self.res[0] , root.val + left + right)

            return root.val + max(left,right)

        dfs_maxsum(root)
        return self.res[0]