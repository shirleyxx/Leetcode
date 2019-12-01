class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        queue, nodes = [root], []
        while queue:
            nodes.insert(0, [q.val for q in queue])
            queue = [q for node in queue for q in (node.left, node.right) if q]
        return nodes
