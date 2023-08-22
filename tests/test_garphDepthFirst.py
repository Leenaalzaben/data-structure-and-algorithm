# from graph.graph import Graph
import pytest
from graph.graphDepthFiest import Graph 


def test_depth_first(sample_graph):
    result = sample_graph.depth_first("A")
    assert result == ["A", "B", "D", "E", "C"]


def test_depth_first_traversal(sample_graph):
    result = sample_graph.depth_first("B")
    assert result == ["B", "D", "E"]
    sample_graph.add_vertex("F")
    result = sample_graph.depth_first("F")
    assert result == ["F"]

def test_depth_first_disconnected_components():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    graph.add_vertex("X")
    graph.add_vertex("Y")
    graph.add_vertex("Z")

    graph.add_edge("X", "Y")

    result = graph.depth_first("A")
    assert result == ["A", "B", "C"]

    result = graph.depth_first("X")
    assert result == ["X", "Y"]


    
@pytest.fixture
def sample_graph():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("D", "E")

    return graph

def test_depth_first(sample_graph):
    result = sample_graph.depth_first("A")
    assert result == ["A", "B", "D", "E", "C"]



if __name__ == "__main__":
    test_depth_first_traversal()
