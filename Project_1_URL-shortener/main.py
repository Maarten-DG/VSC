from flask import Flask, render_template, request, redirect
import sqlite3

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
    alias = request.args.get('alias')
    url = request.args.get('url')
    errors = []

    if alias is not None or url is not None:
        if not alias:
            errors.append('De alias mag niet leeg zijn')
        if not url:
            errors.append("De url mag niet leeg zijn.")

        if not errors:
            with sqlite3.connect('shortener.db') as conn:
                cursor = conn.cursor()
                # Check op dubbele alias
                cursor.execute("SELECT * FROM mappings WHERE alias = ?", (alias,))
                if cursor.fetchone():
                    errors.append("Deze alias is al in gebruik.")
                else:
                    # Opslaan
                    cursor.execute("INSERT INTO mappings (alias, url) VALUES (?, ?)", (alias, url))
                    conn.commit()
                    return render_template("succes.html", alias=alias, url=url)
        
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