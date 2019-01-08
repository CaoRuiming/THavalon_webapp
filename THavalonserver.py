#!/usr/bin/env python3

import copy
import os
import random
import shutil
import datetime
import sys
sys.path.insert(0, '/home/nreed/.web/THavalon')
import THavalon
import thavalon
from os import listdir
from os.path import isfile, join
from datetime import timedelta
from functools import update_wrapper
from flask import Flask, request, send_from_directory, render_template, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/', methods=['GET', 'OPTIONS'])
#@crossdomain(origin='*')
def index_serve():
	return send_from_directory('.', 'index.html')

@app.route('/css/<file>')
def serve_css(file):
	return send_from_directory('css', file)

@app.route('/game1/')
def game_list_serve():
        files = os.listdir('game1')
        return render_template('files.html', files=files)

@app.route('/game2/')
def game_list_serve2():
        files = os.listdir('game2')
        return render_template('files.html', files=files)

@app.route('/game3/')
def game_list_serve3():
        files = os.listdir('game3')
        return render_template('files.html', files=files)

@app.route('/game<number>/ReallyDoNotOpen/')
def game_really_do_not_open(number):
	with open('game' + number + '/DoNotOpen', 'r') as file:
                output = file.read().replace("\n", "<br>")
	#print(output)
	return output
	#return send_from_directory('game' + number, user)

@app.route('/game<number>/DoNotOpen/')
def game_do_not_open(number):
        output = "Are you sure you wish to see DoNotOpen? <a href=\"/game" + number + "/ReallyDoNotOpen\">Click here to view</a>"
	return output

@app.route('/game<number>/<user>')
def game_serve(number, user):
	#assert(os.stat(user))
	with open('game' + number + '/' + user, 'r') as file:
                timestamp = os.path.getmtime('game' + str(number))
                val = datetime.datetime.fromtimestamp(timestamp)
                mtime = str(val.strftime('%H:%M:%S %m/%d/%Y'))
		output = "--- Game " + str(number)
                output += "---<br>This game was rolled at " + mtime
                output += "<br><br>You are viewing the information of: " + user + "<br><br>" + file.read().replace("\n", "<br>")
	#print(output)
	if user == "DoNotOpen":
		output = "Are you sure you wish to see DoNotOpen? <a href=\"/game" + number + "/ReallyDoNotOpen\">Click here to view</a>"
	return output
	#return send_from_directory('game', user)

@app.route('/gametime', methods=['GET', 'OPTIONS'])
#@crossdomain(origin='*')
def game_get_time():
        gameroom = request.args.getlist('gameroom')
        if (len(gameroom) == 1):
                timestamp = os.path.getmtime('game' + str(gameroom[0]))
                val = datetime.datetime.fromtimestamp(timestamp)
                return str(val.strftime('%H:%M:%S %m/%d/%Y'))
        else:
                return 'error'

@app.route('/thavalon', methods=['GET', 'OPTIONS'])
#@crossdomain(origin='*')
def main():
        gameroom = request.args.getlist('gameroom')
	players = request.args.getlist('player')
	if(len(players) == 0):
		path = "game1"
		if(gameroom == 2):
			path = "game2"
		if(gameroom == 3):
			path = "game3"
		currentPlayers = [f for f in listdir(path) if isfile(join(path,f))]
		for p in currentPlayers:
			if(p != "start" and p != "DoNotOpen"):
				players.append(p)
	thavalon.run_THavalon(players, gameroom)
	return 'called script'
			
if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded=True)

