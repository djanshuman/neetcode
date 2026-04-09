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

            ''' In case p and q are same then threshold will be 1 , if we don't have this check then it will never reach 2 and it will return false '''
            mid = node == p or node == q
            threshold = 1 if p == q else 2

            if mid + left + right >= threshold:
                self.ans = node

            return mid or left or right
        
        checkLowestCommonAncestor(root)
        return self.ans
