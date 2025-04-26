from flask import Flask, render_template
import compute 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("input.html")
    