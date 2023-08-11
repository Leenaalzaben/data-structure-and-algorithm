import pytest
from graph.graph import Vertix, Graph, Queue

@pytest.fixture
def sample_graph():
    g = Graph()
    a = g.add_vertix('A')
    b = g.add_vertix('B')
    e = g.add_vertix('E')
    c = g.add_vertix('C')
    d = g.add_vertix('D')

    g.add_edge(a, b, weight=1)
    g.add_edge(a, c, weight=2)
    g.add_edge(b, d, weight=3)
    g.add_edge(b, e, weight=4)
    g.add_edge(e, d, weight=5)
    g.add_edge(e, c, weight=6)
    return g

def test_empty_graph_size():
    # Test size of an empty graph
    g = Graph()
    assert g.size() == 0

def test_add_vertex(sample_graph):
    f = sample_graph.add_vertix('F')
    vertices = sample_graph.get_vertices()
    assert f in vertices

def test_add_edge(sample_graph):
    f = sample_graph.add_vertix('F')
    g = sample_graph.add_vertix('G')
    sample_graph.add_edge(f, g)
    neighbors = sample_graph.get_neighbors(f)
    assert len(neighbors) == 1

def test_get_vertices(sample_graph):
    vertices = sample_graph.get_vertices()
    assert len(vertices) == 5

def test_get_neighbors(sample_graph):
    a = [v for v in sample_graph.get_vertices() if v.value == 'A'][0]
    neighbors = sample_graph.get_neighbors(a)
    assert len(neighbors) == 2

def test_graph_size(sample_graph):
    assert sample_graph.size() == 5

def test_breadth_first(sample_graph):
    a = [v for v in sample_graph.get_vertices() if v.value == 'A'][0]
    traversal_result = sample_graph.breadth_first(a)
    assert traversal_result == ['A', 'B', 'C', 'D', 'E']
