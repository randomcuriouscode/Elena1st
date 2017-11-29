import flask
import elena.algo.lawler_paths
from geopy.distance import vincenty

app = Flask(__name__, static_folder='../static/dist', template_folder='../static')

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
    nodeStorage = parse("nodeStorage.pickle")
    fromlat = request.args.get('fromlat')
    fromlng = request.args.get('fromlng')
    tolat = request.args.get('tolat')
    tolng = request.args.get('tolng')
    prefs = request.args.get('route_pref')
    elevation = prefs.get('elevation')
    distance = prefs.get('distance')
    pathList = get_shortest_paths(nodeStorage, fromnode, tonode,
    bestPath = pathList[0]
    bestElev = get_elevation(bestPath[0])
    for path in pathList:
        elv = get_elevation(path[0])
        if elv == bestElev:
            if bestPath[1] < path[1]:
                bestElev = elv
                bestPath = path
        elif elevation = 1:
            if elv < bestElev:
                bestElev = elv
                bestPath = path
        elif elevation = 2:
            if elv > bestElev:
                bestElev = elv
                bestPath = path
    return jsonify(List=bestPath[0], distance=bestPath[1], elev=bestElev)

def get_elevation(nodeList):
    elevSum = 0
    previousNode = None
    for node in nodeList:
        if previousNode != None:
            difference = node.height-previousNode.height
            if difference > 0:
                elevSum+=difference
        previousNode = node
    return elevSum

        
def callback():
    return 'placeholder'


if __name__ == '__main__':
    app.run()
