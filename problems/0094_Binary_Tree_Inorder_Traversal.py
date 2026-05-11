# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def recur(root : TreeNode) -> List[int]:
            if root is None:
                return []
            trav = []
            if root.left != None:
                r1 = recur(root.left)
                for item in r1:
                    trav.append(item)
            trav.append(root.val)
            if root.right != None:
                r1 = recur(root.right)
                for item in r1:
                    trav.append(item)
            return trav
        return recur(root)

a = TreeNode(1)
a.right = TreeNode(2)
a.right.left = TreeNode(3)

c = Solution()
print(c.inorderTraversal(a))