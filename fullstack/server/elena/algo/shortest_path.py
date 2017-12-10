from heapq import heappush, heappop
from elena.util.util import get_distance


def heuristic(node1, node2):
    return get_distance(node1, node2)


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
