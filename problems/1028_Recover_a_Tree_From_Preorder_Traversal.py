from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: #NA , ~1hr
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if traversal=="": return None
        root = int(traversal.split("-")[0])
        traversal = traversal[len(str(root)):]

        curStack = [[0,root]]

        cnt = 0
        val = ""
        for i in range(len(traversal)):
            if (traversal[i]=="-"):
                if val!="":
                    curStack.append([cnt,int(val)])
                    cnt = 0
                cnt+=1
                val = ""
            else:
                val += traversal[i]
        if val!="":
            curStack.append([cnt,int(val)])
            cnt = 0
        
        print(curStack)
        p = TreeNode(root)
        rootNode = TreeNode(-1)
        rootNode.left = p
        depth = 0
        stack = [[0,p]]
        for i in range(1,len(curStack)):
            cDepth = curStack[i][0]
            curNode = TreeNode(curStack[i][1])
            if cDepth>stack[-1][0]:
                stack[-1][1].left = curNode
                stack.append([cDepth,curNode])
            elif cDepth==stack[-1][0]:
                stack[-2][1].right = curNode
                stack.append([cDepth,curNode])
            elif cDepth<stack[-1][0]:
                lf = cDepth
                while lf!=stack[-1][0]:
                    stack.pop()
                    cDepth = stack[-1][0]
                    curNode = stack[-1][1]
                stack.pop()
                curNode = TreeNode(curStack[i][1])
                stack[-1][1].right = curNode
                stack.append([cDepth,curNode])
        return rootNode.left
