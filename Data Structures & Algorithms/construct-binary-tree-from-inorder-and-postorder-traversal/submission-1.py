# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
left_size is the bridge — inorder tells you where the root is, which tells you how many elements are on the left. You then use that count to carve the same number of elements from the front of postorder for the left subtree, and everything else (minus the root) goes to the right.

inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
indices:    [0   1   2   3  4]

Inorder boundaries are straightforward:

left:  in_left=0,     in_right=mid-1=0    → [9]
right: in_left=mid+1=2, in_right=4        → [15, 20, 7]

Postorder boundaries need left_size:

postorder = [9, 15, 7, 20, 3]
             ↑            ↑
          post_left    post_right (always the current root, excluded)

left subtree has 1 element (left_size=1):
  post_left=0, post_left + left_size - 1 = 0  → [9]

right subtree gets the rest (excluding root at post_right):
  post_left + left_size = 1, post_right - 1 = 3  → [15, 7, 20]
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Step 1 : generate hashMap to store indices and value
        inorder_map = {val : idx for idx,val in enumerate(inorder)}

        def helper(in_left, in_right, post_left, post_right):
            # base case
            if in_left > in_right:
                return None

            root = TreeNode(postorder[post_right])
            mid = inorder_map[root.val]
            left_len = mid - in_left
            
            # left_len = mid - in_left is the key — tells you how many elements are in the left subtree, so you can correctly split postorder

            root.left = helper(in_left , mid -1 , post_left, post_left + left_len - 1)
            root.right = helper(mid + 1 , in_right , post_left + left_len , post_right - 1)
            return root  
        

        return helper(0, len(inorder) - 1, 0 , len(postorder) - 1)