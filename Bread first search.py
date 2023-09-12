def bfs_tree(adj_list, start):
    # number of vertices in the adjacency list of the graph.
    V = len(adj_list)

    # Initialise parent and visited arrays[].
    parent = [None] * V
    visited = [False] * V

    visited[start] = True
    queue = []
    queue.append(start)
    while len(queue) != 0:
        node_u = queue.pop(0)
        neighbours = adj_list[node_u]
        for node_v, weight in neighbours:
            if visited[node_v] is False:
                visited[node_v] = True
                parent[node_v] = node_u
                queue.append(node_v)
    return parent



# an undirected graph

adj_list = [[(1, None)], [(0, None)], [(0, None)]]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))
