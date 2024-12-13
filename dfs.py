
#this is a iterative method for dfs
def dfs(graph, start):
    visited = set()
    st = [start]
    dfs_tr = []
    while st:
        node = st.pop()
        if node not in visited:
            visited.add(node)
            dfs_tr.append(node)
            st.extend(reversed(graph[node]))
    return dfs_tr
        

        
        
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

dfs_result = dfs(graph, 'A')
print("DFS Traversal:", dfs_result)