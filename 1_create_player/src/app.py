import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages/gamerocket-1.0.0-py2.7.egg/")

import gamerocket
from flask import Flask, request, render_template
app = Flask(__name__)

gamerocket.Configuration.configure(gamerocket.Environment.Development,
                                    apiKey = "your_apiKey",
                                    secretKey = "your_secretKey")

                                    
@app.route("/")
def form():
    return render_template("form.html")

@app.route("/create_player", methods=["POST"])
def create_player():
    result = gamerocket.Player.create({
        "name":request.form["name"],
        "locale":request.form["locale"]
    })
    
    if result.is_success:
        return "<h1>Success! Player ID: " + result.player.id + "</h1>"
    else:
        return "<h1>Error " + result.error + ": " + result.error_description + "</h1>"

if __name__ == '__main__':
    app.run(debug=True)