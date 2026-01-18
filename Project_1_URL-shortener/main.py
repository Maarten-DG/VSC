from flask import Flask, render_template, request, redirect

import sqlite3

def init_db():
    with sqlite3.connect('shortener.db') as conn:
        cursor = conn.cursor()
        # Maak de tabel aan als deze nog niet bestaat
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mappings (
                alias TEXT PRIMARY KEY,
                url TEXT NOT NULL
            )
        """)
        conn.commit()

# Roep de functie aan
init_db()

app = Flask(__name__)

@app.route("/")
def home():
    # Input ophalen
    alias = request.args.get('alias')
    url = request.args.get('url')
    errors = []

    # Check of de gebruiker al iets heeft proberen te versturen
    # (Als alias None is, is de bezoeker er voor de eerste keer)
    if alias is not None or url is not None:
        if not alias:
            errors.append('De alias mag niet leeg zijn')
        if not url:
            errors.append("De url mag niet leeg zijn.")

        # Als er geen fouten zijn: opslaan in dict
        if not errors:
            # In plaats van: url_mapping[alias] = url
            # Nadat je checkt of de velden leeg zijn:
            with sqlite3.connect('shortener.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM mappings WHERE alias = ?", (alias,))
                bestaande_alias = cursor.fetchone()

                if bestaande_alias:
                    errors.append("Deze alias is al in gebruik. Kies een andere!")

            # Voer de INSERT pas uit als 'errors' nog steeds leeg is
            if not errors:
                cursor.execute("INSERT INTO mappings (alias, url) VALUES (?, ?)", (alias, url))
                conn.commit()
            return render_template("succes.html", alias=alias, url=url)
        
    # Als er fouten zijn (of eerste bezoek), toon formulier met eventuele fouten
    return render_template("home.html", fouten=errors)

@app.route("/shorturl/<alias>")
def toon_mapping(alias):
    # 1. Verbinding maken met de database
    with sqlite3.connect('shortener.db') as conn:
        cursor = conn.cursor()
        
        # 2. Zoek de URL die bij deze alias hoort
        cursor.execute("SELECT url FROM mappings WHERE alias = ?", (alias,))
        resultaat = cursor.fetchone() # Haalt de eerste (en enige) rij op
    
    # 3. Controleren of er iets gevonden is
    if resultaat:
        # resultaat is een tuple, bijv: ('https://www.ap.be',)
        # We hebben het eerste element nodig: resultaat[0]
        return redirect(resultaat[0])
    else:
        return "Alias bestaat niet", 404
    
if __name__ == "__main__":
    app.run(debug=True)