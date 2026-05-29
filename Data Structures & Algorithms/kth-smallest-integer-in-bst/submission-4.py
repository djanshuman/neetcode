# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = None
        self.counter = 0

        def dfs_findKth(root):
            if not root:
                return None

            dfs_findKth(root.left)
            self.counter += 1

            if self.counter == k:
                self.val = root.val

            dfs_findKth(root.right)

        dfs_findKth(root)
        return self.val