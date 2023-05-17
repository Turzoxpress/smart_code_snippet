class Solution:
    def rootToLeafNodes(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [(root, [])]
        result = []

        while stack:
            node, path = stack.pop()
            path.append(node.val)
            if not node.left and not node.right:
                result.append(list(path))
            if node.left:
                stack.append((node.left, list(path)))
            if node.right:
                stack.append((node.right, list(path)))
        return result[::-1]
