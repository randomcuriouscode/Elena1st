import overpy
from geopy.distance import vincenty

from elena.model.node import *

HEIGHT = 'height'


def get_distance(node1, node2):
    coord1 = (node1.lat, node1.lng)
    coord2 = (node2.lat, node2.lng)
    return vincenty(coord1, coord2).meters


def parse_nodes(result):
    node_list = result.get_nodes()
    nodeStorage = NodeStorage()
    for parsed_node in node_list:
        if HEIGHT in parsed_node.attributes:
            nodeStorage.add_node(parsed_node.id,
                                 Node(parsed_node.id, parsed_node.lat, parsed_node.lon, parsed_node.attributes[HEIGHT]))
        else:
            nodeStorage.add_node(parsed_node.id, Node(parsed_node.id, parsed_node.lat, parsed_node.lon, 0))

    return nodeStorage


def parse_ways(result, nodeStorage):
    ways_list = result.get_ways()
    for parsed_way in ways_list:
        nodes = parsed_way._node_ids  ##REFERRING TO A PRIVATE VARIABLE!!!
        offset = 1
        i = 0
        # skipping nodes that are referred to in the ways but not present in the node cache
        while i + offset < len(nodes):
            if not nodeStorage.contains(nodes[i]) or not nodeStorage.contains(nodes[i + offset]):
                print("{} and {}".format(nodes[i], nodes[i + offset]))
                offset += 1
                continue
            node1 = nodeStorage.get_node(nodes[i])
            node2 = nodeStorage.get_node(nodes[i + offset])
            dist = get_distance(node1, node2)
            node1.add_node(node2.id, dist)
            node2.add_node(node1.id, dist)
            i = i + offset
            offset = 1


def parse(filename):
    api = overpy.Overpass()
    with open(filename, 'r') as f:
        data = f.read()
    result = api.parse_xml(data)
    print("Nodes: {}".format(len(result.nodes)))
    print("Ways: {}".format(len(result.ways)))

    nodeStorage = parse_nodes(result)
    parse_ways(result, nodeStorage)
    return nodeStorage
