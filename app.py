from flask import Flask, render_template, request
from flask_session import Session
from tempfile import mkdtemp
import sqlite3
from sqlite3 import Error
from cs50 import SQL


app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMENENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///feesRecord.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return render_template("profile.html", name= "nik")

@app.route("/create", methods=["GET", "POST"])
def create():
    if (request.method == "GET"):
        return render_template("create.html")
    else:
        name = request.form.get("name")
        std = request.form.get("class")
        fees = request.form.get("fees")
        month = request.form.get("month")
        cleared = request.form.get("cleared")

        print(name)
        print(std, fees, month, cleared)
        return "ac"

@app.route("/update", methods=["GET", "POST"])
def update():
    if (request.method == "GET"):
        return render_template("update.html")
    else:
        return "Updated"

@app.route("/search", methods=["GET", "POST"])
def search():
    if (request.method == "GET"):
        return render_template("search.html")
    else:
        return "Searched"

@app.route("/dues", methods=["GET", "POST"])
def dues():
    if (request.method == "GET"):
        return render_template("dues.html")
    else:
        return "Checked"