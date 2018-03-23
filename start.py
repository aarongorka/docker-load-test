#!/usr/bin/env python3
from multiprocessing.dummy import Pool as ThreadPool
from flask import Flask,jsonify,request
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return_object = f(10)
    return json.dumps(return_object)

def f(x):
    start_time = datetime.datetime.now()
    elapsed_time = datetime.datetime.now() - start_time
    while elapsed_time.microseconds < 1000000:
        elapsed_time = datetime.datetime.now() - start_time
        x = 213123
        x*x
        x = x + 1
    return 'Done!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
