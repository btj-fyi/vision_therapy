from flask import Flask, render_template
import os
from peripheral_awareness.peripheral_awareness import peripheral_awareness

app = Flask(__name__)


@app.route("/peripheral_awareness_v1")
def myapp():
    peripheral_awareness()
    return render_template("peripheral_awareness.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
