from geopy.distance import vincenty


def get_distance(node1, node2):
    coord1 = (node1.lat, node1.lng)
    coord2 = (node2.lat, node2.lng)
    return vincenty(coord1, coord2).meters


def calculate_cost(nodeStorage, path):
    sum = 0
    for i in range(0, len(path) - 1):
        node1 = nodeStorage.get_node(path[i])
        node2 = nodeStorage.get_node(path[i+1])
        sum += get_distance(node1, node2)
    return sum
