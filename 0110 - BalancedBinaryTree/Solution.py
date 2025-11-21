# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_height_and_balance(node):
            if not node:
                return 0, True
            height_left, left_balanced = check_height_and_balance(node.left)
            height_right, right_balanced = check_height_and_balance(node.right)
            if not left_balanced or not right_balanced or abs(height_left-height_right)>1:
                return 0, False
            else:
                return max(height_left, height_right) + 1, True
        _, balanced = check_height_and_balance(root)
        return balanced