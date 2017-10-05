from flask import Flask, render_template, request, session
import os

echo_app = Flask(__name__)

echo_app.secret_key = os.urandom(32)

logins = dict()
logins["username"] = "password"

@echo_app.route("/", methods = ["GET", "POST"])
def root():
    try:
        if session["username"] in logins.keys() and session["password"] == logins[session["username"]]:
            return render_template("welcome.html", osis = session["username"])
    except:
        return render_template('base.html')

@echo_app.route("/response/", methods = ["POST"])
def welcome():
    #print request.form
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    session["password"] = password
    if session["username"] in logins.keys() and session["password"] == logins[session["username"]]:
        return render_template("welcome.html", osis = username)
    return render_template("response.html")

@echo_app.route("/logout/")
def logout():
    session.clear()
    return render_template('base.html')





if __name__ == "__main__":
    echo_app.debug = True
    echo_app.run()
