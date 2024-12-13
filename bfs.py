from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node
    visited.add(start)

    while queue:
        node = queue.popleft()  # Dequeue a node
        print(node, end=" ")  # Process the node (in this case, print it)

        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# def bfs(graph, start):
#     visited = set()
#     queue = deque([start]) #list hishebe pathaiche tai 3rd bracket
#     bfs_traversal = []

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.add(node)
#             bfs_traversal.append(node)
#             queue.extend(graph[node])
    
#     return bfs_traversal

# Example usage
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

print("BFS Traversal starting from node 'A':")
bfs(graph, 'A')

