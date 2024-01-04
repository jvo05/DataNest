from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)