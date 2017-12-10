from collections import defaultdict
from elena.parse.parser import *


def breadth_first(nodeStorage, node, node_bool):
    cur_list = [node]
    node_bool[node] = True

    while len(cur_list) > 0:
        cur_node = cur_list.pop(0)
        neighbors = nodeStorage.get_neighbors(cur_node)

        for neighbor in neighbors:
            if node_bool[neighbor.id]:
                continue
            cur_list.append(neighbor.id)
            node_bool[neighbor.id] = True


def check_connectivity(nodeStorage):
    node_bool = defaultdict(bool)

    non_connect = 0
    non_connect_list = []

    for key in nodeStorage.nodeMap.keys():
        if not node_bool[key]:
            non_connect_list.append(key)
            breadth_first(nodeStorage, key, node_bool)
            non_connect += 1

    return non_connect, non_connect_list


if __name__ == '__main__':
    nodeStorage = parse("/Users/avaneesh/amherst")
    print(check_connectivity(nodeStorage))
