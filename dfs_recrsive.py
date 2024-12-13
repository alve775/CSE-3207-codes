def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set

    visited.add(node)  # Mark the node as visited
    print(node, end=" ")  # Process the node (e.g., print it)

    for neighbor in graph[node]:  # Explore neighbors
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)  # Recursive call
            
            
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Test Recursive DFS
print("DFS Recursive Traversal:")
dfs_recursive(graph, 'A')
