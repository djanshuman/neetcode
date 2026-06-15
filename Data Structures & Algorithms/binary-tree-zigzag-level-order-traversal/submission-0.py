# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =[]
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            level = []
            lenq= len(queue)
            for _ in range(lenq):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            reversed_level = level[::-1] if len(res) % 2 else level
            res.append(reversed_level)
        return res

        