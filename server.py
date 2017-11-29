import flask
import elena.algo.lawler_paths

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
    fromlat = request.args.get('fromlat')
    fromlng = request.args.get('fromlng')
    tolat = request.args.get('tolat')
    tolng = request.args.get('tolng')
    prefs = request.args.get('route_pref')
    elevation = prefs.get('elevation')
    distance = prefs.get('distance')
    pathList = get_shortest_paths
    print("fromlat: "+str(fromlat)+"\nfromlng: "+str(fromlng)+"\ntolat: "+str(tolat)+"\ntolng: "+str(tolng)+"\nflexibility: "+str(flex))
    return 'callback()'

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
