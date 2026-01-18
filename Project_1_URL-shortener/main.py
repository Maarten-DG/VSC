from flask import Flask

app = Flask(__name__)

url_mapping = {
    "ap": "https://www.ap.be",
    "google": "https://www.google.com",
    "canvas": "https://ap.instructure.com"
}

@app.route("/shorturl/<alias>")
def toon_mapping(alias):
    # 'alias' bevat nu wat de gebruiker in de URL typte
    # Bijvoorbeeld: als de URL 'localhost:5000/shorturl/ap' is, dan is alias == "ap"
    
    # Check of de alias in onze dictionary staat
    if alias in url_mapping:
        return url_mapping[alias]
    else:
        return "Alias bestaat niet"
    
if __name__ == "__main__":
    app.run(debug=True)