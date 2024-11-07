from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    sport = db.Column(db.String(50))
    date = db.Column(db.Date, default = datetime.utcnow )

    def __repr__(self):
        return '<name >' % self.name



REGISTRANTS={}
SPORTS = ["cricket", "football"]

@app.route("/")
def name():  
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def req():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or not sport:
        return render_template("failure.html")

    REGISTRANTS[name] = sport
    return redirect("/registers")

@app.route("/registers")
def registers():
    return render_template("registers.html",registrants = REGISTRANTS)


