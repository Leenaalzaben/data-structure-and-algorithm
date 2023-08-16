class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)

    def depth_first(self, start_node):
        visited = set()
        traversal_order = []

        def dfs(node):
            nonlocal traversal_order
            visited.add(node)
            traversal_order.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_node)
        return traversal_order

if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('D', 'F')

    start_node = 'A'
    traversal_order = graph.depth_first(start_node)
    print("Result:", ', '.join(traversal_order))
