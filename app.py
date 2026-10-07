from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Forside.html")


@app.route("/om")
def om():
    navn = "Leo"
    elever = ["Jonas", "Henrik", "Filip"]

    return render_template("ommeg.html", navn=navn, elever=elever)


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)