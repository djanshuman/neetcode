# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])

        while queue:
            p_node, q_node = queue.popleft()
            
            if p_node is None and q_node is None:
                continue
            if p_node is None or q_node is None or (p_node.val != q_node.val):
                return False

            queue.append((p_node.left,q_node.left))
            queue.append((p_node.right,q_node.right))

        return True
