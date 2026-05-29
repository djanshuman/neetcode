# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = None
        self.counter = 0

        def dfs_findKth(root):
            if not root:
                return None

            dfs_findKth(root.left)
            self.counter += 1

            if self.counter == k:
                self.val = root.val
              

            dfs_findKth(root.right)

        dfs_findKth(root)
        return self.val



''' Iterative solution      
        
#BST in-order traversal gives element in sorted order
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Step 1 : Initialization
        counter = 0 
        stack = []
        curr = root
        
        # Step 2: While curr is non-empty or there is element in stack to be processed
        # Outer loop
        while curr or stack:

            #Step 3 : Inner loop to traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            #Step 4: Once left exploration complete, pop the visited node
            node = stack.pop()
            counter += 1

            #Step 5: Check if we got the kth element, every pop gives the sorted element in-order
            if counter == k:
                return node.val

            curr = node.right

''' 