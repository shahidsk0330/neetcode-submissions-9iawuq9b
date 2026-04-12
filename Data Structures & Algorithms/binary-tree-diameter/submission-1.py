# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  
        def helper(root):
            if not root:
                return 0
            lt = helper(root.left)
            rt = helper(root.right)
            self.diameter = max(lt+rt, self.diameter)
            return 1 + max(lt, rt)
        helper(root)
        return self.diameter
        
        
        

        
     

        