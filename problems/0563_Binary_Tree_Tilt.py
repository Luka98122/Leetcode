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