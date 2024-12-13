from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start]) #list hishebe pathaiche tai 3rd bracket
    bfs_traversal = []

    while queue:
        node = queue.popleft() #shudhu pop dile reverse dfs hoye jeto
        if node not in visited:
            visited.add(node)
            bfs_traversal.append(node)
            queue.extend(graph[node])

    return bfs_traversal

def dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            dfs_traversal.append(node)
            stack.extend(reversed(graph[node]))

    return dfs_traversal

graph = {
    22: [7, 50],
    7: [1, 10],
    50: [25, 56],
    10: [8, 20],
    25: [30],
    56: [58],
    58: [57, 100],
    1: [],
    8: [],
    20: [],
    30: [],
    57: [],
    100: []
}

start_node = 22

bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)