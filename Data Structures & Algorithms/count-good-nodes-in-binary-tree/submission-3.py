from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recursive
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root,max_value):
            if root is None:
                return 0

            counter = 0
            if root.val >= max_value:
                counter += 1

            max_value = max(root.val,max_value)

            counter += dfs(root.left,max_value) 
            counter += dfs(root.right,max_value) 
            
            return counter

        return dfs(root,root.val)
        