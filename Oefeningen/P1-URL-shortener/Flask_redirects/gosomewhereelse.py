from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def go_to_ap():
    # De browser wordt direct doorgestuurd naar de opgegeven URL
    return redirect("https://www.ap.be")

if __name__ == "__main__":
    app.run(debug=True)