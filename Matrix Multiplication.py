def next_vertex(in_tree, distance):
    distances_to_consider = []
    for i in range(len(in_tree)):
        if not in_tree[i]:
            distances_to_consider.append(distance[i])
    smallest = min(distances_to_consider)
    return distance.index(smallest)

in_tree =  [0, 1, 2, 3, 4]
distance = [5, 3, 2, 5, 4]

print(next_vertex(in_tree, distance))