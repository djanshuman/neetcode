# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1 : edge case check
        if not preorder or not inorder:
            return None

        # Step 2 : find the root node from preorder
        root = TreeNode(preorder[0])
        # Step 3 : Fetch index of root node from the inorder as thats the separation point for Left and right
        mid = inorder.index(preorder[0])
        # Step 4 : Build left and right tree
        root.left = self.buildTree(preorder[1 : mid + 1] , inorder[: mid])
        root.right = self.buildTree(preorder[mid + 1 : ] , inorder[mid + 1 : ])
        return root