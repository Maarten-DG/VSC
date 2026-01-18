import logging
import datetime

# 1. Configureer de logging naar het juiste bestand
logging.basicConfig(
    filename='keuzemenu.log',
    level=logging.DEBUG, # Zorg dat alle niveaus worden vastgelegd
    format='%(message)s' # We bepalen de structuur zelf in de string
)

# Lijst voor Nederlandse dagnamen
dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

while True:
    # Haal de huidige dag van de week op
    dag_index = datetime.datetime.now().weekday()
    dag_naam = dagen[dag_index]

    print("\nWat voor bericht wil je loggen?")
    print("1. een diagnostisch bericht")
    print("2. nuttige informatie")
    print("3. een waarschuwing")
    print("4. een foutmelding")
    
    keuze = input("Maak een keuze (of druk op Ctrl+C om te stoppen): ")

    # Logica voor de keuzes
    if keuze == "1":
        logging.debug(f"{dag_naam} - Diagnostisch bericht")
    elif keuze == "2":
        logging.info(f"{dag_naam} - Nuttige informatie")
    elif keuze == "3":
        logging.warning(f"{dag_naam} - Waarschuwing")
    elif keuze == "4":
        logging.error(f"{dag_naam} - Foutmelding")
    else:
        # Ongeldige keuze wordt gelogd als INFO level
        logging.info(f"{dag_naam} - Ongeldige keuze gemaakt door gebruiker")
        print("Ongeldige keuze. Dit is gelogd als informatie.")