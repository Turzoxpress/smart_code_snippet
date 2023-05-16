class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def nodes_in_every_level_binary_tree_dfs(self, root: Optional[TreeNode]) -> List[TreeNode]:
        result = []
        self.dfs(root, 0, result)
        return result

    def dfs(self, node, level, result):
        if not node:
            return

        if level == len(result):
            result.append([])

        result[level].append(node.val)

        self.dfs(node.left, level + 1, result)
        self.dfs(node.right, level + 1, result)
