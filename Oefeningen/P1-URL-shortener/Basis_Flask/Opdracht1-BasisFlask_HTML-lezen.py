from flask import Flask

app = Flask(__name__)

@app.route("/")
def toon_inhoud():
    # We openen het bestand en lezen de tekst
    with open("pagecontents.txt", "r") as f:
        tekst = f.read()
    
    # We sturen de tekst terug naar de browser
    return tekst

if __name__ == "__main__":
    app.run(debug=True)