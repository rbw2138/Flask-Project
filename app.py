#rbw2138-final
#Ryan Watt

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

#start the server
if __name__ == "__main__":
    app.run()