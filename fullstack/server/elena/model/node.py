class Node:
    def __init__(self, id, lat, lng, height, nodes=None):
        if nodes is None:
            nodes = []
        self.id = id
        self.lat = lat
        self.lng = lng
        self.height = height
        self.nodes = nodes

    def __repr__(self):
        return "Node id = {} lat = {} lng = {} height = {} nodes = {}".format(self.id, self.lat, self.lng, self.height,
                                                                              self.nodes)

    def add_node(self, id, distance=0):
        self.nodes.append(NodeRelation(id, distance))


class NodeRelation:
    def __init__(self, id, distance=0):
        self.id = id
        self.distance = distance

    def __repr__(self):
        return "NodeRelation id = {} distance = {}".format(self.id, self.distance)


class NodeStorage:
    def __init__(self, nodeMap=None):
        if nodeMap is None:
            nodeMap = {}
        self.nodeMap = nodeMap

    def __repr__(self):
        return repr(self.nodeMap)

    def add_node(self, id, node):
        self.nodeMap[id] = node

    def get_node(self, id):
        return self.nodeMap[id]

    def contains(self, id):
        return id in self.nodeMap

    def get_neighbors(self, id):
        return self.nodeMap[id].nodes

    def set_map(self, nodeMap):
        self.nodeMap = nodeMap
