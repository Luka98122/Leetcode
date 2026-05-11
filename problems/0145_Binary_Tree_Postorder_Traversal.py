from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        def rec(root : TreeNode):
            if not root:
                return
            
            
            rec(root.left)
            rec(root.right)
            res.append(root.val)
        rec(root)
        return res