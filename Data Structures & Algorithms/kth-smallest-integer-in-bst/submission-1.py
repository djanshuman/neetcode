# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.min_val =  []
        self.counter = 0
        def traverseFindSmallest(root):
            if not root:
                return

            traverseFindSmallest(root.left)

            self.min_val.append(root.val)
    
            traverseFindSmallest(root.right)
        
        traverseFindSmallest(root)
        return self.min_val[k - 1]
            