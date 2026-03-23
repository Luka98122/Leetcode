# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None: return ""
        res = str(root.val)
        
        if root.right==None and root.left == None:
            return res
        
        elif root.right != None and root.left==None:
            res+="()"
            res+=f"({self.tree2str(root.right)})"
        elif root.right == None and root.left!=None:
            res+=f"({self.tree2str(root.left)})"
        else:
            res+=f"({self.tree2str(root.left)})"
            res+=f"({self.tree2str(root.right)})"
        return res