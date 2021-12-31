from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run()
