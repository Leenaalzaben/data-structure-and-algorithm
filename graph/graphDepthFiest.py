class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        self.adjacency_list[value] = []
        return value

    def add_edge(self, start_vertex, end_vertex):
        self.adjacency_list[start_vertex].append(end_vertex)

    def depth_first(self, start_vertex):


        """
        Perform depth-first traversal on the graph starting from the given vertex.

        Args:
            start vertex : The vertex to start the traversal from.

        Returns:
            list: A list of vertices visited in the depth-first order.
        """

        visited = set()
        result = []

        def dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    dfs(neighbor)

        dfs(start_vertex)
        return result