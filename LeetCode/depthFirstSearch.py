adjacency_matrix = {1: [2, 3], 2: [4, 5], 3: [5], 4: [6], 5: [6], 6: [7], 7: []}
# Output should be: 1,3,5,6,7,2,4
# Queue:
def print_dfs(graph, head, visited=[]):
    visited += [head]
    for vertex in graph[head]:
        if not vertex in visited:
            visited = print_dfs(graph, vertex, visited)
    return visited


print(print_dfs(adjacency_matrix, 1))
