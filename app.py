#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request
import configparser
import deploy

conf = configparser.ConfigParser()
conf.read('config.ini')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/AutoDeploy')
def auto_deploy():

    list = [1, 4, 7, 3]
    list_new = list.pop(2)
    return "1"


if __name__ == '__main__':
    run_port = conf.get('config', 'port')
    print("Server running on port "+run_port)
    app.run(port=run_port)







