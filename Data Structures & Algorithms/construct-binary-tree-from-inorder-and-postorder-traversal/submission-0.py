# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx,val in enumerate(inorder)}

        def helper(in_left, in_right, post_left, post_right):
            if in_left > in_right:
                return None

            root = TreeNode(postorder[post_right])
            mid = inorder_map[root.val]
            left_len = mid - in_left

            root.left = helper(in_left , mid -1 , post_left, post_left + left_len - 1)
            root.right = helper(mid + 1 , in_right , post_left + left_len , post_right - 1)
            return root  
        

        return helper(0, len(inorder) - 1, 0 , len(postorder) - 1)