from flask import Flask
from prometheus_client import start_http_server, Summary
import time, random

app = Flask(__name__)
inference_latency = Summary('inference_latency_seconds', 'Time spent on inference')

@app.route('/infer')
@inference_latency.time()
def infer():
    time.sleep(random.uniform(0.1, 0.5))
    return "Inference Done"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)