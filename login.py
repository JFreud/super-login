from flask import Flask, render_template, request, session
import os

echo_app = Flask(__name__)

echo_app.secret_key = os.urandom(32)

logins = dict()
logins["username"] = "password"

@echo_app.route("/", methods = ["GET", "POST"])
def root():
    if request.method == "GET":
        return render_template('base.html')
    try:
        if session["username"] in logins.keys() and session["password"] == logins[session["username"]]:
            return welcome()
    except:
        return render_template('base.html')

@echo_app.route("/welcome/", methods = ["POST"])
def welcome():
    #print request.form
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    session["password"] = password
    return render_template("response.html", osis = username, requester = request.method)







if __name__ == "__main__":
    echo_app.debug = True
    echo_app.run()
