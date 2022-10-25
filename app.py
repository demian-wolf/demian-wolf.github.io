from pathlib import Path

from flask import Flask, render_template, send_from_directory
from flask_minify import minify
import yaml

app = Flask(__name__)
minify(app=app, html=True, js=True, cssless=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    with open("data.yaml") as fp:
        data = yaml.safe_load(fp)
        return render_template("index.html",
                               index=data["index"],
                               portfolio=data["portfolio"])


@app.route("/cv.pdf")
def cv():
    return send_from_directory(
        Path(__file__).resolve().parent,
        "cv.pdf"
    )


if __name__ == '__main__':
    app.run()
