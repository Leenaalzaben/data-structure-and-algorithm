def business_trip(graph, cities):
    costs = {city: float('inf') for city in cities}
    costs[cities[0]] = 0

    def dfs(city, path_cost):
        if city == cities[-1]:
            costs[city] = min(costs[city], path_cost)
            return

        for neighbor, cost in graph.get(city, []):
            if path_cost + cost < costs[neighbor]:
                dfs(neighbor, path_cost + cost)

    dfs(cities[0], 0)
    return costs[cities[-1]] if costs[cities[-1]] != float('inf') else None
