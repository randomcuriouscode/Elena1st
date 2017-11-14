from elena.algo.shortest_path import get_a_star_path
from elena.util.util import calculate_cost


def get_shortest_paths(nodeStorage, id1, id2, dist):
    shortest_path, shortest_cost = get_a_star_path(nodeStorage, id1, id2)
    if shortest_path is None:
        return None

    if shortest_cost > dist:
        return []

    A = [(shortest_path, shortest_cost)]
    B = []
    spur_index = 0

    print("Shortest path = {}".format(shortest_path))
    print("Shortest path cost = {}".format(shortest_cost))

    while True:
        k = len(A)
        cur_path = A[k - 1][0]
        for i in range(spur_index, len(cur_path) - 1):
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
                B.append((total_path, total_path_cost, i))

        if len(B) == 0:
            break

        B.sort(key=lambda tup: tup[1], reverse=True)
        if B[-1][1] > dist:
            break

        new_path_cost = B.pop()
        A.append(new_path_cost[:2])
        spur_index = new_path_cost[2]

    return A
