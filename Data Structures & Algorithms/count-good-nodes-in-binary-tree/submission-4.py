# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs_node(root,maxval):
            if not root:
                return 0
                
            counter = 0
            if root.val >= maxval:
                counter += 1

            counter += dfs_node(root.left,max(maxval,root.val))
            counter += dfs_node(root.right,max(maxval,root.val))

            return counter

        return dfs_node(root,float('-inf'))
        