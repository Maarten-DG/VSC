from flask import Flask, render_template, request

app = Flask(__name__)

url_mapping = {
    "ap": "https://www.ap.be",
    "google": "https://www.google.com",
    "canvas": "https://ap.instructure.com"
}

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
            url_mapping[alias] = url
            return render_template("succes.html", alias=alias, url=url)
        
    # Als er fouten zijn (of eerste bezoek), toon formulier met eventuele fouten
    return render_template("home.html", fouten=errors)

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