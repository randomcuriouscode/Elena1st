from geopy.distance import vincenty
from heapq import *


def calculate_cost(nodeStorage, path):
    sum = 0
    for i in range(0, len(path) - 1):
        node1 = nodeStorage.get_node(path[i])
        node2 = nodeStorage.get_node(path[i+1])
        sum += vincenty((node1.lat, node1.lng), (node2.lat, node2.lng)).meters
    return sum


def heuristic(node1, node2):
    return vincenty((node1.lat, node1.lng), (node2.lat, node2.lng)).meters


# A-star implementation
def get_a_star_path(nodeStorage, id1, id2, excluded_nodes=None, excluded_edges=None):
    if excluded_nodes is None:
        excluded_nodes = set([])
    if excluded_edges is None:
        excluded_edges = set([])

    frontier = []
    heappush(frontier, (0, id1))
    backtrace = {id1: None}
    cost = {id1: 0}
    goal_reached = False

    while len(frontier) > 0:
        cur = heappop(frontier)

        if cur[1] == id2:
            goal_reached = True
            break

        for next in nodeStorage.get_neighbors(cur[1]):
            next_id = next.id
            if next_id in excluded_nodes:
                continue
            if (cur[1], next_id) in excluded_edges or (next_id, cur[1]) in excluded_edges:
                continue

            new_cost = cost[cur[1]] + next.distance
            if next_id not in cost or new_cost < cost[next_id]:
                cost[next_id] = new_cost
                priority = heuristic(nodeStorage.get_node(next_id), nodeStorage.get_node(id2)) + new_cost
                heappush(frontier, (priority, next_id))
                backtrace[next_id] = cur[1]

    if not goal_reached:
        return None, None

    path = []
    cur_id = id2
    while cur_id is not None:
        path.insert(0, cur_id)
        cur_id = backtrace[cur_id]

    return path, cost[id2]


def get_shortest_paths(nodeStorage, id1, id2, dist):
    shortest_path, shortest_cost = get_a_star_path(nodeStorage, id1, id2)
    if shortest_path is None:
        return None

    A = [(shortest_path, shortest_cost)]
    B = []

    print("Shortest path = {}".format(shortest_path))
    print("Shortest path cost = {}".format(shortest_cost))

    while True:
        k = len(A)
        cur_path = A[k - 1][0]
        for i in range(0, len(cur_path) - 1):
            spur_node = cur_path[i]
            root_path = cur_path[:i + 1]
            root_cost = calculate_cost(nodeStorage, root_path)

            excluded_nodes = set([])
            excluded_edges = set([])

            for path, cost in A:
                if i + 1 < len(path) and path[:i + 1] == root_path:
                    excluded_edges.add((path[i], path[i + 1]))

            for root_path_node in root_path:
                if not root_path_node == spur_node:
                    excluded_nodes.add(root_path_node)

            spur_path, spur_cost = get_a_star_path(nodeStorage, spur_node, id2, excluded_nodes, excluded_edges)
            if spur_path is None:
                continue

            total_path = root_path + spur_path[1:]
            total_path_cost = spur_cost + root_cost

            if (total_path, total_path_cost) not in B:
                B.append((total_path, total_path_cost))

        if len(B) == 0:
            break

        B.sort(key=lambda tup: tup[1], reverse=True)
        if B[-1][1] > dist:
            break

        new_path_cost = B.pop()
        A.append(new_path_cost)

    return A
