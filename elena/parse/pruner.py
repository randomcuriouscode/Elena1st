from collections import defaultdict
from elena.parse.parser import *

def prune_nodes(nodeStorage):
    new_map = {}

    for id, node in nodeStorage.nodeMap.items():
        if nodeStorage.get_node(id).nodes:
            new_map[id] = node

    nodeStorage.set_map(new_map)


def breadth_first(nodeStorage, node, node_bool):
    cur_list = [node]
    node_bool[node] = True
    return_list = [node]

    while len(cur_list) > 0:
        cur_node = cur_list.pop(0)
        neighbors = nodeStorage.get_neighbors(cur_node)

        for neighbor in neighbors:
            if node_bool[neighbor.id]:
                continue
            cur_list.append(neighbor.id)
            node_bool[neighbor.id] = True
            return_list.append(neighbor.id)

    return return_list


def check_connectivity(nodeStorage):
    node_bool = defaultdict(bool)

    non_connect_component_list = []

    for key in nodeStorage.nodeMap.keys():
        if not node_bool[key]:
            non_connect_list = breadth_first(nodeStorage, key, node_bool)
            non_connect_component_list.append(non_connect_list)

    return non_connect_component_list


def remove_disconnected(nodeStorage):
    non_connect_component_list = check_connectivity(nodeStorage)
    max_size = -1
    max_size_index = 0
    final_map = {}

    for i in range(0, len(non_connect_component_list)):
        if len(non_connect_component_list[i]) > max_size:
            max_size = len(non_connect_component_list[i])
            max_size_index = i

    final_list = non_connect_component_list[max_size_index]

    for node_id in final_list:
        final_map[node_id] = nodeStorage.get_node(node_id)

    nodeStorage.set_map(final_map)
