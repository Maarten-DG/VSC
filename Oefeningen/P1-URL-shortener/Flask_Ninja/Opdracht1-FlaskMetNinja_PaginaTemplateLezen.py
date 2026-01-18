from flask import Flask, render_template # Voeg render_template toe

app = Flask(__name__)

@app.route("/")
def index():
    # We lezen de tekst uit het bestand
    with open("pagecontents.txt", "r") as f:
        tekst_inhoud = f.read()
    
    # We sturen de tekst naar 'index.html' onder de naam 'citaat'
    return render_template("index.html", citaat=tekst_inhoud)

if __name__ == "__main__":
    app.run(debug=True)