
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0
        maxDepth = 0
        def dfs(node, path):
            nonlocal maxDepth
            if not node:
                return
            path.append(node.val)
            for child in node.children:
                dfs(child, path)
            if len(path) > maxDepth:
                maxDepth = len(path)
            path.pop()
        
        dfs(root, [])
        return maxDepth