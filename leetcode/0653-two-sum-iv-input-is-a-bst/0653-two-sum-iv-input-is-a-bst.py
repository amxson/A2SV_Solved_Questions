# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dictt = {}
        def traverse(root,k):
            if root is None:
                return False
            if root.val  in dictt:
                return True
            dictt[k-root.val] = 5
            return traverse(root.left,k) or traverse(root.right,k)
        return traverse(root,k)
        