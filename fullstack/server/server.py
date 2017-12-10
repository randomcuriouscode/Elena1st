from flask import Flask, render_template, request, jsonify
from elena.algo.lawler_paths import *
from elena.parse.parser import parse
from geopy.distance import vincenty


app = Flask(__name__, static_folder='../client/dist', template_folder='../client')
nodeStorage = parse("map.osm")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')


@app.route('/route', methods=['GET']) #
def route():
    # This will receive the to/from coordinates
    # print(request.get_data())
    # arraydata = str(request.get_data()).replace('&',' ').replace('=',' ').replace('\'',' ').split(" ")
    # print(request.args)
    fromlat = request.args.get('fromlat')
    fromlng = request.args.get('fromlng')
    fromId = getNode(fromlat, fromlng)
    tolat = request.args.get('tolat')
    tolng = request.args.get('tolng')
    toId = getNode(tolat, tolng)
    elevation = request.args.get('elevation') # TODO CHANGE THIS TO PARAM
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
                bestPath = path
    return jsonify(List=bestPath[0], distance=bestPath[1], elev=bestElev)

def get_elevation(nodeList):
    elevSum = 0
    previousNode = None
    for node in nodeList:
        node = nodeStorage.get_node(node)
        if previousNode != None:
            difference = node.height-previousNode.height
            if difference > 0:
                elevSum+=difference
        previousNode = node
    return elevSum

def getNode(lat, long):
    bestNode = None
    bestDist = None
    coord1 = (node1.lat, node1.lng)
    for k, v in nodeStorage.nodeList.items():
        coord2 = (v.lat, v.lng)
        dist = vincenty(coord1, coord2).meters
        if bestDist == None or bestDist > dist:
            bestNode = k
            bestDist = dist
    return bestNode

def getNode(lat, long):
    bestNode = None
    bestDist = None
    coord1 = (lat, long)
    for k, v in nodeStorage.nodeMap.items():
        coord2 = (v.lat, v.lng)
        dist = vincenty(coord1, coord2).meters
        if bestDist == None or bestDist > dist:
            bestNode = k
            bestDist = dist
    return bestNode


def callback():
    return 'placeholder'


if __name__ == '__main__':
    app.run()
