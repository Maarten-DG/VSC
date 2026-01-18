from flask import Flask, render_template, request # Voeg render_template toe

app = Flask(__name__)

@app.route("/")
def index():
    # We sturen de gebruiker gewoon naar het formulier
    return render_template("index.html")

@app.route("/greet")
def greet():
    # Haal de data uit de URL (?voornaam=...&familienaam=...)
    vn = request.args.get('voornaam')
    fn = request.args.get('familienaam')
    
    return f"Hallo, {vn} {fn}"

if __name__ == "__main__":
    app.run(debug=True)