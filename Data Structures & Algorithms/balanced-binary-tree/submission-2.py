# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalance(root):
            if not root:
                return 0, True
            if root:
                ldepth, left = isBalance(root.left)
                rdepth, right = isBalance(root.right)
                if not left or not right or  abs(ldepth-rdepth) > 1:
                    return 0, False
                return 1+max(ldepth, rdepth), True
        _, result = isBalance(root)
        return result
        