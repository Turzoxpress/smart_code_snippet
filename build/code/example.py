# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        totalSum = 0

        def dfs(node, path):
            nonlocal totalSum
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                temp = ''
                for child in path:
                    temp += str(child)
                totalSum += int(temp, base=2)

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return totalSum
