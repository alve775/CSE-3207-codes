def bfs(graph, start):
    visited = set()
    queue = deque([start]) #list hishebe pathaiche tai 3rd bracket
    bfs_traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_traversal.append(node)
            queue.extend(graph[node])
    
    return bfs_traversal