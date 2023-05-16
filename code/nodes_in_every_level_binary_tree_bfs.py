class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def nodes_in_every_level_binary_tree_bfs(self, root: Optional[TreeNode]) -> List[TreeNode]:

        queue = [root]
        result = []
        while queue:
            size = len(queue)
            temp = []
            for node in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)

        return result
