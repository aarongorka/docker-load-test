#!/usr/bin/env python3
from multiprocessing.dummy import Pool as ThreadPool
from flask import Flask,jsonify,request
import datetime
import json
from multiprocessing import Pool
from multiprocessing import cpu_count

app = Flask(__name__)

@app.route('/loadtester/load', methods=['GET'])
def main():
    processes = cpu_count()
    pool = ThreadPool(processes)
    return_object = pool.starmap(f, zip(list(range(processes))))
    pool.close()
    pool.join()
    return json.dumps(return_object)

def f(x):
    start_time = datetime.datetime.now()
    elapsed_time = datetime.datetime.now() - start_time
    x = 213123
    while elapsed_time.microseconds < 10000:
        elapsed_time = datetime.datetime.now() - start_time
        x = x*x
        x = x + 1
    return 'Done!'

@app.route('/loadtester/health', methods=['GET'])
def healthcheck():
    return json.dumps('OK!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
