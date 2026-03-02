from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Hello from Flask in Docker & Kubernetes NEW FEATURE branch!",
        "message": "Production ready version",
	"version": "v1.0",
        "message": "Hello from Flask in Docker & Kubernetes!!!!!!",
        "feature": "logging enabled",
        "pod": os.environ.get("MY_POD", "unknown")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

