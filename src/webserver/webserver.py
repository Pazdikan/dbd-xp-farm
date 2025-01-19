from flask import Flask
from rich.text import Text

from util.console import log
from flask import send_from_directory
import os
import webserver.api as api
import webserver.panel as panel

app = Flask(__name__)

api.init(app)
panel.init(app)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

def run_webserver():
    app.run(debug=False, host='0.0.0.0')
