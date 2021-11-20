from collections import OrderedDict

from flask import Flask, render_template
from flask_minify import minify


app = Flask(__name__)
minify(app=app, html=True, js=True, cssless=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
