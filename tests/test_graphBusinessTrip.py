from graph.graphBusinessTrip import business_trip

def test_business_trip_valid_trip():
    graph = {
        "Metroville": [["Pandora", 82]],
        "Pandora": [],
    }
    cities = ["Metroville", "Pandora"]
    assert business_trip(graph, cities) == 82

def test_business_trip_invalid_trip_no_flight():
    graph = {
        "Narnia": [],
        "Arendelle": [],
        "Naboo": [],
    }
    cities = ["Narnia", "Arendelle", "Naboo"]
    assert business_trip(graph, cities) is None

def test_business_trip_invalid_trip_not_connected():
     pass

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

