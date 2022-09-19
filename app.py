from flask import Flask, render_template, request, redirect

app = Flask(__name__)


RESIGTRANTS = {}

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee", "Football"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    # validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    
    # validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    # remember registrant
    RESIGTRANTS[name] = sport 

    # confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=RESIGTRANTS)

if __name__ == '__main__':
    app.run(debug=True)