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

@app.route("/run_action", methods=["GET"])
def run_action():
    result = gamerocket.Action.run(
        "hello-world",
        {
        "player": "your_player_id",
        "name":request.args.get("name")
        }
    )
    
    if result.is_success:
        return "<h1>Success!: " + result.data["hello"] + "</h1>"
    else:
        return "<h1>Error " + result.error + ": " + result.error_description + "</h1>"

@app.route("/unlock_content", methods=["GET"])
def buy_purchase():
    result = gamerocket.Purchase.buy(
        "unlock-content",
        {"player": "your_player_id"}
    )
    
    if result.is_success:
        return "<h1>Success!: " + result.data["message"] + "</h1>"
    else:
        return "<h1>Error " + result.error + ": " + result.error_description + "</h1>"
      
if __name__ == '__main__':
    app.run(debug=True)
