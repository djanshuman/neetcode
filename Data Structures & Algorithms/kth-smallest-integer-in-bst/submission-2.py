# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.min_val =  None
        self.counter = 0
        def traverseFindSmallest(root):
            if not root or self.min_val is not None :
                return

            traverseFindSmallest(root.left)

            self.counter += 1
            if self.counter ==  k:
                self.min_val = root.val
                return
    
            traverseFindSmallest(root.right)
        
        traverseFindSmallest(root)
        return self.min_val
            