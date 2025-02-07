from flask import Flask, send_file
import os
from peripheral_awareness.peripheral_awareness import peripheral_awareness

app = Flask(__name__)


@app.route("/peripheral_awareness_v1")
def myapp():
    peripheral_awareness()
    return send_file(
        "peripheral_awareness/peripheral_awareness.png", mimetype="image/png"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
