# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:  
    def subtree(self,p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return self.subtree(p.left,q.left) and self.subtree(p.right,q.right)
            else:
                return False 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque()
        self.result = False
        if not root and not subRoot:
            return True
        queue.append(root)
        while(len(queue)>0):
            for i in range(len(queue)):
                c = queue.popleft()
                self.result = self.subtree(c,subRoot)
                if(self.result):
                    return True
                if(c.left is not None):
                    queue.append(c.left)
                if(c.right is not None):
                    queue.append(c.right)
        return self.result

            

