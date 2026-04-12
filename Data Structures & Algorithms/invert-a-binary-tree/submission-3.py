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
        def invertBfs(root):
            if not root:
                return root
            d = deque()
            d.append(root)
            while d:
                node = d.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        invertBfs(root)
        return root
           

        