'''
- implement the graph with all methods needed.
- vertex  *
- Edge  *
- graph *
methods : 
  - add_vertex() * 
  - add_edge() *
  - get_verteces() *
  - get_neighbors() *
  - size () *
- breadth first traversal . 
  - Queue() *
'''
from collections import deque
# we spill it 'd-e-c-k'


class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


class Vertix:

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return self.value


class Edge:

    def __init__(self, vertix, weight=0):
        self.weight = weight
        self.vertix = vertix


class Graph:

    def __init__(self):
        self.__adj_list = {}

    def add_vertix(self, value):
        '''
        Arguments: value
        Returns: The added vertex
        Add a vertex to the graph
        '''

        vertix = Vertix(value)
        self.__adj_list[vertix] = []
        return vertix

    # def add_edge(self,start_vertix,end_vertix,weight=0):

        # edge1 = Edge(end_vertix)
        # edge2=Edge(start_vertix)
        # if start_vertix not in self.__adj_list:
        #   raise KeyError(" vertix not exist ")
        # if end_vertix not in self.__adj_list:
        #   raise KeyError(" vertix not exist ")

        # self.__adj_list[start_vertix].append(edge1)
        # self.__adj_list[end_vertix].append(edge2)

    def add_edge(self, start_vertix, end_vertix, weight=0):
        '''
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

    def get_vertices(self):
        '''
          Arguments: none
          Returns all of the vertices in the graph as a  
          collection (set, list, or similar)
          Empty collection returned if there are no vertices
        '''

        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, vertix):
        '''
        get neighbors
        A rguments: vertex
        Returns a collection of edges connected to the 
        given vertex
        Include the weight of the connection in the                      returned collection
        Empty collection returned if there are no vertices
        '''
        # return self.__adj_list[vertix]
        return self.__adj_list.get(vertix, [])

    def breadth_first(self, start_vertix):

        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.dequeue()

            result.append(current_vertix.value)

            neighbors = self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result


if __name__ == "__main__":
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)
    print(g.breadth_first(a))
