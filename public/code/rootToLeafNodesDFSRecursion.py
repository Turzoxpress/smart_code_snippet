class Solution:
    def rootToLeafNodes(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        result = []
        def dfs(node, path):
            if not node:
                return 
            path.append(node.val)
            if not node.left and not node.right:
                result.append(list(path))
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return result