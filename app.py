from pathlib import Path

from flask import Flask, render_template, send_from_directory
from flask_minify import minify

app = Flask(__name__)
minify(app=app, html=True, js=True, cssless=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index/index.html")


@app.route("/cv.pdf")
def cv():
    return send_from_directory(
        Path(__file__).resolve().parent,
        "static/portfolio/cv.pdf"
    )


if __name__ == '__main__':
    app.run()
