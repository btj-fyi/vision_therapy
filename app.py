from flask import Flask, send_file
import os
from peripheral_awareness.peripheral_awareness import main

app = Flask(__name__)


@app.route("/")
def myapp():

    main()
    return send_file(
        "peripheral_awareness/peripheral_awareness.png", mimetype="image/png"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
