from flask import Flask, render_template
from db import hentedata

app = Flask(__name__)


@app.route("/")
def index():
    data = hentedata()
    return render_template("flasker.html", flasker = data)


@app.route("/om")
def om():
    navn = "Leo"
    elever = ["Jonas", "Henrik", "Filip"]

    return render_template("ommeg.html", navn=navn, elever=elever)


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
