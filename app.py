from flask import Flask, send_file
import os
from peripheral_awareness.peripheral_awareness import main
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/")
def myapp():

    main()
    return send_file(
        "peripheral_awareness\peripheral_awareness.png", mimetype="image/png"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
