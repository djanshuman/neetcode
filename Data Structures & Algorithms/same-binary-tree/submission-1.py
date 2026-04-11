# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([(p,q)])

        while q:
            p_node, q_node = q.popleft()

            if not p_node and not q_node:
                continue
            if (p_node and not q_node) or (q_node and not p_node) or (p_node.val != q_node.val):
                return False

            q.append((p_node.left,q_node.left))
            q.append((p_node.right,q_node.right))

        return True
