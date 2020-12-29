def cloneGraph(self, node: 'Node') -> 'Node':
    graphCopy = {}
    def dfs(node):
        if not node:
            return
        else:
            node_copy = Node(node.val, [])
            graphCopy[node] = node_copy
            for neighbor in node.neighbors:
                if neighbor in graphCopy:
                    node_copy.neighbors.append(graphCopy[neighbor])
                else:
                    node_copy.neighbors.append(dfs(neighbor))
            return node_copy
    return dfs(node)