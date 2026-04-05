from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS Iterative
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,root.val)]
        counter = 0

        while stack:
            root,max_value = stack.pop()
        
            if root.val >= max_value:
                counter += 1
            if root.right:
                stack.append((root.right,max(root.val,max_value)))

            if root.left:
                stack.append((root.left,max(root.val,max_value)))

        return counter
        
        