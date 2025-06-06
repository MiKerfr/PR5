from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/time")
def get_time():
    return jsonify({"time": int(time.time())})

if __name__ == "__main__":
    app.run()
time_requests_count = 0

@app.route('/time', methods=['GET'])
def get_time():
    global time_requests_count
    time_requests_count += 1
    return jsonify({'time': int(time.time())})

@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({'count': time_requests_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
