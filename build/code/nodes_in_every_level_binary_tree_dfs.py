class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def nodes_in_every_level_binary_tree_dfs(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if not root:
            return []

        stack = [(root, 0)]
        result = []

        while stack:
            node, level = stack.pop()

            if level == len(result):
                result.append([])

            result[level].append(node.val)

            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

        return result
