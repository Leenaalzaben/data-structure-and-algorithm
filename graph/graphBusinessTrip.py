from graph.graph import Vertex,Graph

def business_trip(graph, city_names):


    """
    Calculate the total cost of a business trip between cities if exist.

    Args:
        graph : The graph representing cities and flight connections.
        city_names: A list of city names representing the trip itinerary.

    Returns:
        int or None: The total cost of the trip if all flights are direct, or None if any flight is not available.
    """


    total_cost = 0

    for i in range(len(city_names) - 1):
        current_city = city_names[i]
        next_city = city_names[i + 1]

        neighbors = graph.get_neighbors(Vertex(current_city))  
        direct_flight = False

        for edge in neighbors:
            if edge.vertex.value == next_city:
                total_cost += edge.weight
                direct_flight = True
                break

    if not direct_flight:
        return None

    return total_cost



  
