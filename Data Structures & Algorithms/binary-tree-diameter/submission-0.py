# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def height(root):
            if not root:
                return 0
            ldepth = height(root.left)
            rdepth = height(root.right)
            self.result = max(self.result,ldepth+rdepth)
            return 1+max(ldepth,rdepth)
        height(root)
        return self.result

        