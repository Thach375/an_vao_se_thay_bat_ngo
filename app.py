from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yes1")
def yes1():
    return render_template("yes1.html")

@app.route("/no1")
def no1():
    return render_template("no1.html")

@app.route("/yes2")
def yes2():
    return render_template("yes2.html")

@app.route("/no2")
def no2():
    return render_template("no2.html")

@app.route("/cont")
def cont():
    return render_template("cont.html")

@app.route("/last")
def last():
    return render_template("last.html")

if __name__ == "__main__":
    app.run(debug=True)
