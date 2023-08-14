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
