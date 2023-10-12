from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        
    def isSameTree(self, t, s):
        if not t and not s:
            return True
        
        if t and s and t.val == s.val:
            return (self.isSameTree(t.left, s.left) and 
                    self.isSameTree(t.right, s.right))

        return False
