import logging
from flask import Flask, render_template

# 1. Configuratie van de logger
logging.basicConfig(
    filename='flask_experiment.log',
    level=logging.DEBUG, # We zetten dit op DEBUG om ook debug-berichten te vangen
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

app = Flask(__name__)

@app.route("/")
def index():
    # Log dat de pagina bezocht is (INFO)
    logging.info("De homepagina is bezocht.")

    # We lezen de tekst uit het bestand (zoals in de eerste oefening)
    try:
        with open("pagecontents.txt", "r") as f:
            tekst_inhoud = f.read()
    except FileNotFoundError:
        tekst_inhoud = "Bestand niet gevonden."
        logging.error("pagecontents.txt kon niet worden gevonden!")

    # Genereer de response body
    response_body = render_template("index.html", citaat=tekst_inhoud)
    
    # Log de volledige response body (DEBUG)
    logging.debug(f"Response body inhoud: {response_body}")
    
    return response_body

if __name__ == "__main__":
    app.run(debug=True)