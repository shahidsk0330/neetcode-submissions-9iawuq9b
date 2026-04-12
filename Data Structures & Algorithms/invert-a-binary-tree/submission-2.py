# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        When the node is present 
        I need to change the left_node to right_node 
        right_node to left node.
        """
        def invertAlgo(root):
            if root:
                root.left, root.right = root.right, root.left
                invertAlgo(root.left)
                invertAlgo(root.right)
        invertAlgo(root)
        return root
    
           

        