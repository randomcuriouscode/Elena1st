from flask import Flask, render_template, request, jsonify
from elena.algo.lawler_paths import *
from elena.parse.parser import parse
from elena.util.util import get_distance_coordinates


app = Flask(__name__, static_folder='../client/dist', template_folder='../client')
nodeStorage = parse("map.osm")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/route', methods=['GET'])
def route():
    # This will receive the to/from coordinates
    # print(request.get_data())
    # arraydata = str(request.get_data()).replace('&',' ').replace('=',' ').replace('\'',' ').split(" ")
    # print(request.args)
    fromlat = request.args.get('fromlat')
    fromlng = request.args.get('fromlng')
    fromId = get_node(fromlat, fromlng)
    tolat = request.args.get('tolat')
    tolng = request.args.get('tolng')
    toId = get_node(tolat, tolng)
    elevation = request.args.get('elevation')  # TODO CHANGE THIS TO PARAM
    distance = request.args.get('distance')
    pathList = get_shortest_paths(nodeStorage, fromId, toId, distance)
    bestPath = pathList[0]
    bestElev = get_elevation(bestPath[0])
    for path in pathList:
        elv = get_elevation(path[0])
        if elv == bestElev:
            if bestPath[1] < path[1]:
                bestElev = elv
                bestPath = path
        elif elevation == 1:
            if elv < bestElev:
                bestElev = elv
                bestPath = path
        elif elevation == 2:
            if elv > bestElev:
                bestElev = elv
                bestPath = path\
    bestPathCoords = []
    for node in bestPath[0]:
        node = nodeStorage.get_node(node)
        bestPathCoords.append(node.lat, node.lng)
    return jsonify(List=bestPathCoords, distance=bestPath[1], elev=bestElev)


def get_elevation(nodeList):
    elevSum = 0
    previousNode = None
    for node in nodeList:
        node = nodeStorage.get_node(node)
        if previousNode is not None:
            difference = node.height-previousNode.height
            if difference > 0:
                elevSum += difference
        previousNode = node
    return elevSum


def get_node(lat, long):
    best_node = None
    best_dist = None
    for k, v in nodeStorage.nodeMap.items():
        dist = get_distance_coordinates(lat, long, v.lat, v.lng)
        if best_dist is None or best_dist > dist:
            best_node = k
            best_dist = dist
    return best_node


def callback():
    return 'placeholder'


if __name__ == '__main__':
    app.run()
