from geopy.distance import vincenty


def calculate_cost(nodeStorage, path):
    sum = 0
    for i in range(0, len(path) - 1):
        node1 = nodeStorage.get_node(path[i])
        node2 = nodeStorage.get_node(path[i+1])
        sum += vincenty((node1.lat, node1.lng), (node2.lat, node2.lng)).meters
    return sum
