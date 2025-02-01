# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while 1:  # Start an indefinite loop that will break once LCA is found
            if root.val < min(p.val, q.val):  # Check if both nodes are in the right subtree
                root = root.right
            elif root.val > max(p.val, q.val):  # Check if both nodes are in the left subtree
                root = root.left
            else:
                return root  # Found the LCA or one of the nodes is the LCA itself