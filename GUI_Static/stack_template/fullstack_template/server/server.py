import random
from flask import Flask, render_template, request

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
    flex = request.args.get('pctflex')
    # this will print out a summary of the values:
    print("fromlat: "+str(fromlat)+"\nfromlng: "+str(fromlng)+"\ntolat: "+str(tolat)+"\ntolng: "+str(tolng)+"\nflexibility: "+str(flex))
    return 'callback()'


def callback():
    return 'placeholder'


if __name__ == '__main__':
    app.run()
