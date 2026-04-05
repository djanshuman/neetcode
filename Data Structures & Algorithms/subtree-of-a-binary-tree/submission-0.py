# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root: return False
        if not subRoot : return True

        if self.same_tree(root,subRoot): #In case root has different val but subtree root has same val and is a subtree
            return True
        return (self.isSubtree(root.left,subRoot) or 
                      self.isSubtree(root.right,subRoot))
        


    def same_tree(self,root,subroot):
        if not root and not subroot:
            return True

        if root and subroot and root.val == subroot.val:
            return (self.same_tree(root.left,subroot.left) and 
                self.same_tree(root.right,subroot.right))


        