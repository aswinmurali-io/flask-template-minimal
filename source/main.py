# !/usr/bin/env python
#
# To start flask app as a native desktop web app
#    $ python main.py
#
# To start flask app as hosted server App
#    $ set FLASK_APP=hello.py
#    $ flask run
#
# flask main entry file

import sys
import threading
from flask import Flask, render_template

app: Flask = Flask(__name__)
PORT: int = 2837


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    if sys.platform not in ('win32', 'darwin', 'linux'):
        app.run(debug=False, host='localhost', port=PORT, use_reloader=False)
    else:
        import webview

        # Start the flask thread
        flask_thread = threading.Thread(target=lambda: app.run(
            debug=True, use_reloader=False, host="localhost", port=PORT),
            args=())
        flask_thread.daemon = True
        flask_thread.start()

        # Start the UI thread
        window = webview.create_window(title="Flask App",
                                       url=f"http://localhost:{PORT}/")
        webview.start()
