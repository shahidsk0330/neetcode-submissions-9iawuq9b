# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        d.append(root)
        result =[]
        if not root:
            return []
        while (len(d) > 0):
            x = len(d)
            for i in range(len(d)):
                current = d.popleft()
                if(i == x-1):
                    result.append(current.val)
                if current.left != None:
                    d.append(current.left)
                if current.right != None:
                    d.append(current.right)
        return result
                
            


        