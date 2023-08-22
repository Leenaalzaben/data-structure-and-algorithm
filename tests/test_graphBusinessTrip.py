import unittest
from graph.graph import Graph,Vertex 
from graph.graphBusinessTrip import business_trip
class TestBusinessTripFunction(unittest.TestCase):


    def test_no_direct_trip(self):
        graph = Graph()
        city_a = graph.add_vertex(Vertex("CityA"))
        city_b = graph.add_vertex(Vertex("CityB"))
        
        city_names = ["CityA", "CityB"]
        result = business_trip(graph, city_names)
        self.assertIsNone(result)

    
    def test_invalid_city(self):
        graph = Graph()
        city_a = graph.add_vertex(Vertex("CityA"))
        
        city_names = ["CityA", "CityB"]  
        result = business_trip(graph, city_names)
        self.assertIsNone(result)

    def test_missing_city_in_graph(self):
        graph = Graph()
        city_a = graph.add_vertex(Vertex("CityA"))
        city_b = graph.add_vertex(Vertex("CityB"))
        graph.add_edge(city_a, city_b, 200)

        city_names = ["CityA", "CityC"]  
        result = business_trip(graph, city_names)
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()
