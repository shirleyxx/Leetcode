"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
class Solution:
    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.cloned = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node in self.cloned:
            return self.cloned[node]
        
        clone_node = Node(node.val, [])
        self.cloned[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node

        
        
