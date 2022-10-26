from flask import Flask, render_template
from flask_minify import minify

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
minify(app)


@app.route("/")
def index():
    return render_template("index/index.html")


if __name__ == '__main__':
    app.run()
