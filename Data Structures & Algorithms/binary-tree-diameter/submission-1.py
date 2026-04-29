# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def height(node):
            if not node : return 0
            left = height(node.left) 
            right = height(node.right)

            self.max_dia = max(self.max_dia, left+right)
            return 1 + max(left,right)
        _ = height(root)
        return self.max_dia