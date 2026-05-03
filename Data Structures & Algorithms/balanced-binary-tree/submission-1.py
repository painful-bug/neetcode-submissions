# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def __init__(self) -> None:
        self.lcount = 0
        self.rcount = 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> List[bool, int]:
            if not root:
                return [True, 0] # We are essentially returning the height fo the subtree as well

            left, right = dfs(root.left), dfs(root.right)
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [is_balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]