from flask import Flask, jsonify
import time
from threading import Lock

app = Flask(__name__)

time_requests_count = 0
counter_lock = Lock()

@app.route('/time', methods=['GET'])
def get_time():
    global time_requests_count
    with counter_lock:
        time_requests_count += 1
    return jsonify({'time': int(time.time())})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    global time_requests_count
    with counter_lock:
        return jsonify({'count': time_requests_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
