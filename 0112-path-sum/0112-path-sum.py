# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         if not root.left and not root.right:
#             return targetSum == root.val
        
#         left_sum = self.hasPathSum(root.left, targetSum - root.val)
#         right_sum = self.hasPathSum(root.right, targetSum - root.val)
#         return left_sum or right_sum

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        v = targetSum - root.val
        return self.hasPathSum(root.left, v) or self.hasPathSum(root.right, v)