# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            suc = self.minn(root.right)
            root.val = suc.val
            root.right = self.deleteNode(root.right, suc.val)

        return root

    def minn(self, node):
        while node.left:
            node = node.left
        return node