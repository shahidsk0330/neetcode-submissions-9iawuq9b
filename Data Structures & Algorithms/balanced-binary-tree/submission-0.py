# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def dfs(root):
            if not root:
                return 0
            ldepth = dfs(root.left)
            rdepth = dfs(root.right)
            if(abs(ldepth-rdepth)>1):
                self.result = False
            return 1+ max(ldepth,rdepth)
        dfs(root)
        return self.result

        