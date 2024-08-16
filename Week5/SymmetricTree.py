# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None or right is None:
            return left == right
        elif left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

