"""
 CREDIT: This code is adapted for `pages`  based on Nader Elshehabi's  article:
   https://dev.to/naderelshehabi/securing-plotly-dash-using-flask-login-4ia2
   https://github.com/naderelshehabi/dash-flask-login

For other Authentication options see:
  Dash Enterprise:  https://dash.plotly.com/authentication#dash-enterprise-auth
  Dash Basic Auth:  https://dash.plotly.com/authentication#basic-auth

"""
import datetime
import functools
import json
import logging
import urllib.parse as up
import os

from flask import Flask, jsonify, render_template, request

import env_demo as env

MY_IP = '0.0.0.0'


def check_token(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        allowed = False
        # print(f"got args {args} {kwargs} {request.args}")
        uid = request.args.get('uid', '')
        if uid in env.USERS:
            if env.USERS[uid] == request.args.get('key'):
                allowed = True
                message = 'unknown key'
        else:
            message = 'unknown user'
        if allowed:
            return f(*args, **kwargs)
        else:
            return {'message': message}, 400

    return wrap


server = Flask(__name__)


@server.route('/api/watchdog', methods=['GET'])
@check_token
def watchdog():
    # logic to send gmail if a message is not received within X minutes goes here.
    return jsonify({'message': 'alive'})


@server.route('/api/alarm/<code>', methods=['GET'])
@check_token
def alarm(code):
    # send gmail here
    return jsonify({'message': 'ok'})


if __name__ == "__main__":
    server.run(debug=True, host=MY_IP, port=8090)
