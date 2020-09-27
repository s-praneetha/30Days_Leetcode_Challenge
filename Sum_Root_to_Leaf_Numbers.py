# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
            
        def helper (root, node_val): 
            if root:
                helper(root.left, node_val * 10 + root.val)
                helper(root.right, node_val * 10 + root.val)
                if not root.left and not root.right:
                    self.sum += node_val * 10 + root.val
        self.sum = 0
        helper(root, 0)
        return self.sum