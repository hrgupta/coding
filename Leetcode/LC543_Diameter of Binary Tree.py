"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
"""
Solution:

106 / 106 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 15.9 MB

Explanation:

The solution is the node with the maximum sum of depth of left and right subtree. So we find the depth of left subtree and right
subtree, count the current node and compare it with current maximum diameter.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1

        depth(root)
        return self.ans
