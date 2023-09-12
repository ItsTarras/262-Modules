def min_capacity(city_map, depot_position):
    city_map = city_map.replace("\n", " ")
    map_data = city_map.split(" ")
    #Replaces map data, by removing the icky bits.
    if map_data[0] == "":
        map_data = map_data[2:-1]
    else:
        map_data = map_data[0:-1]
    #Create a max_distance variable
    max_dist = 0
    
    #index for while loops
    index = 0
    index2 = 0
    # coutns the number of vertices
    num_vertices = int(map_data[1])

    graph = []
    # creates a graph, skipping the first line
    for i in range(3, len(map_data), 3):
        u = int(map_data[i])
        #print(u)
        v = int(map_data[i + 1])
        #print(v)
        w = int(map_data[i + 2])
        #print(w)
        
        graph.append((u, v, w))
        graph.append((v, u, w))

    # shortest path distance from depot_position to all other cities
    dist = get_shortest_path(graph, num_vertices, depot_position)
    #print(dist)
    
    for distance in dist:
        #print(d)
        if distance != float('inf') and distance > max_dist:
            max_dist = distance

    #Create batter capacity based on distance
    min_battery_capacity = int(max_dist * 4)
    return min_battery_capacity


def get_shortest_path(graph, num_vertices, src):
    """Using youtube, create a function to get the shortest distance from one node to the next"""
    #Creates an array that is of length vertices, and sets all the distances to infiinty.
    dist = [float("inf")] * num_vertices
    dist[src] = 0

    #updates the values of the inedxed vertices in the array
    for i in range(num_vertices - 1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


# testing the code

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))