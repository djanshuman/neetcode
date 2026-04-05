from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root,root.val)])
        counter = 0

        while queue:
            root,max_value = queue.popleft()
        
            if root.val >= max_value:
                counter += 1
            if root.right:
                queue.append((root.right,max(root.val,max_value)))

            if root.left:
                queue.append((root.left,max(root.val,max_value)))
                
        return counter
        
        