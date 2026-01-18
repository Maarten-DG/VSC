from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string

# 1. Database initialisatie
def init_db():
    with sqlite3.connect('shortener.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mappings (
                alias TEXT PRIMARY KEY,
                url TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()

app = Flask(__name__)

# 2. Home route: Formulieren verwerken en opslaan
@app.route("/")
def home():
    url = request.args.get('url')
    errors = []
    generated_alias = None # Om later te tonen in de template

    if url is not None: # Er is op 'opslaan' gedrukt
        if not url:
            errors.append("De url mag niet leeg zijn.")
        
        if not errors:
            # Genereer een alias van 15 kleine letters
            generated_alias = ''.join(random.choices(string.ascii_lowercase, k=15))
            
            # Voeg 'https://' toe als het ontbreekt (voorkomt de fout van net!)
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            # Opslaan in database
            with sqlite3.connect('shortener.db') as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO mappings (alias, url) VALUES (?, ?)", (generated_alias, url))
                conn.commit()
            
            return render_template("succes.html", alias=generated_alias, url=url)

    return render_template("home.html", fouten=errors)

# 3. Redirect route: De kern van Stap 4
@app.route("/shorturl/<alias>")
def toon_mapping(alias):
    with sqlite3.connect('shortener.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT url FROM mappings WHERE alias = ?", (alias,))
        resultaat = cursor.fetchone()
    
    if resultaat:
        url = resultaat[0]
        # Check of de URL begint met http. Zo niet, maak hem absoluut.
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        return redirect(url)
    else:
        return "Alias bestaat niet", 404

if __name__ == "__main__":
    app.run(debug=True)