from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        res = []

        while queue:
            nodes = []
            for i in range(len(queue)):
                
                node = queue.popleft()
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if nodes:
                res.append(nodes)
        
        return res