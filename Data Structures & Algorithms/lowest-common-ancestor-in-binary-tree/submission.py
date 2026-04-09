'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def checkLowestCommonAncestor(node):
            if not node:
                return False


            left = checkLowestCommonAncestor(node.left)
            right = checkLowestCommonAncestor(node.right)

            mid = node == p or node == q

            if mid + left + right >= 2:
                self.ans = node

            return mid or left or right
        
        checkLowestCommonAncestor(root)
        return self.ans
