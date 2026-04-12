# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0
        def dfs(root, maxi):
            if not root:
                return 
            if root:
                if root.val >= maxi:
                    self.result += 1
                    maxi = root.val
                lt = dfs(root.left, maxi) #1
                rt = dfs(root.right, maxi)
        dfs(root, root.val)
        return self.result
                
                
        