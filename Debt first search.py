def DFSUtil(u,v, adj_list,visited,p):
    visited.add(v)
    if(u!=v):
        p[v]=u
    for i in range(len(adj_list[v])):
        if adj_list[v][i][0] not in visited:
            DFSUtil(v,adj_list[v][i][0],adj_list, visited,p)

def dfs_tree(adj_list,start):
    # Create a set to store visited vertices
    visited = set()
    parent_array = [None]*len(adj_list)
    # Call the recursive helper function
    # to print DFS traversal
    DFSUtil(start,start,adj_list,visited,parent_array)
    return parent_array

# an undirected graph

adj_list = [[(1, None), (4, None)], [(0, None), (2, None), (3, None)], [(1, None)], [(1, None), (4, None)], [(3, None), (0, None)]]


print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))
print(dfs_tree(adj_list, 4))