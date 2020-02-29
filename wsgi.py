# Web Sever Gateway Interface Python file

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
  return render_template("index.html")
@app.route("/features.html")
def features():
  return render_template("features.html")
@app.route("/pricing.html")
def pricing():
  return render_template("pricing.html")
@app.route("/contact.html")
def contact():
  return render_template("contact.html")
@app.route("/donate.html")
def blog():
  return render_template("donate.html")



if __name__ == "__main__":
  app.run(debug=True)