# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return (True,0)
            
            left = dfs(node.left)
            right = dfs (node.right)
            balanced = (left[0] and right[0]
                            and abs(left[1] - right[1]) <= 1)
            
            return (balanced, max(left[1],right[1]) + 1)

        return dfs(root)[0]



#Solution 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_node(root):
            if root is None:
                return 0

            left_ht = dfs_node(root.left)
            if left_ht  == -1:
                return -1

            right_ht = dfs_node(root.right)
            if right_ht == -1:
                return -1

            if abs(left_ht - right_ht) > 1:
                return -1

            return max(left_ht,right_ht) + 1

        return dfs_node(root) != -1
        
