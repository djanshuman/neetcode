# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_validBst(root,left, right):
            if not root:
                return True

            # Bound check
            # Passing bounds down the call stack is the right approach — left bound tightens when going right, right # # bound tightens when going left. 
            if not (root.val < right and root.val > left):
                return False

            return (dfs_validBst(root.left, left, root.val) and
                dfs_validBst(root.right, root.val, right))

            
        return dfs_validBst(root,float('-inf') ,float('inf'))