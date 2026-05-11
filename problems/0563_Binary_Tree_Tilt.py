from typing import Optional
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def solve(node):
            if not node:
                return 0

            left_sum = solve(node.left)
            right_sum = solve(node.right)

            node_tilt = abs(left_sum - right_sum)
            
            self.total_tilt += node_tilt

            return node.val + left_sum + right_sum

        solve(root)
        return self.total_tilt