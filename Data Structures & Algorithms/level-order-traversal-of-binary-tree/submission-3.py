# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
''' BFS , Level order traversal'''
''' Per level track the queue length'''
''' return list of level per level iteration completion

This BFS skeleton is the base for a whole family — right-side view (199) (take level[-1]), zigzag (103) (reverse every other level), average per level (637), largest per level (515), rightmost/leftmost. Same loop, you just change what you extract from level. Worth memorizing cold because it recurs constantly.

O(n) time, O(n) space (widest level in the queue).

'''
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            # The lenq ensures we are processing level by level
            lenq = len(q)
            level = []
            for _ in range(lenq):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                res.append(level)

        return res
                    
        