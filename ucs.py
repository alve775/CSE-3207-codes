import heapq

# Uniform Cost Search (UCS)
def uniform_cost_search(graph, start, goal):
    # Priority queue to store (cost, node, path)
    priority_queue = [(0, start, [])]
    visited = set()  # To keep track of visited nodes

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)  # Get the node with the lowest cost

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        # If the goal is reached, return the cost and path
        if node == goal:
            return cost, path

        # Add neighbors to the priority queue
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return float('inf'), []  # Return infinity if the goal is not reachable

# Example Graph with Weights for UCS
graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3), ('G', 6)],
    'D': [('B', 2)],
    'E': [('B', 5), ('H', 1)],
    'F': [('C', 3)],
    'G': [('C', 6)],
    'H': [('E', 1)]
}

print("Uniform Cost Search:")
cost, path = uniform_cost_search(graph_weighted, 'A', 'H')
print(f"Cost: {cost}, Path: {path}")
