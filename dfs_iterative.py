def dfs_iterative(graph, start):
    visited = set()  # To keep track of visited nodes
    stack = [start]  # Use a stack for DFS (LIFO structure)

    while stack:
        node = stack.pop()  # Pop the top element
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node,  end=" ")  # Process the node
            # Add neighbors to the stack (in reverse order for correct processing order)
            stack.extend(reversed(graph[node]))
            
            
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

# Test Iterative DFS
print("DFS Iterative Traversal:")
dfs_iterative(graph, 'A')
