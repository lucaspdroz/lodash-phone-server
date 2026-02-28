
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/compute", methods=["POST"])
def compute():
    data = request.json
    start = data["start"]
    end = data["end"]

    total = 0
    for i in range(start, end):
        total += math.sqrt(i)

    return jsonify({"result": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
