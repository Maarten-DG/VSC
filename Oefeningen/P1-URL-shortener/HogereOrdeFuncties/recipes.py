def make_chocolate_sauce():
    print("- Smelt 100g pure chocolade met een scheutje room.")
    print("- Roer tot een gladde chocoladesaus.")

def make_caramel():
    print("- Smelt suiker in een pan tot het goudbruin is.")
    print("- Voeg voorzichtig boter en warme room toe.")

def make_donut(sauce_function):
    print("--- RECEPT VOOR EEN DONUT ---")
    print("1. Maak het gistdeeg en laat het rijzen.")
    print("2. Steek cirkels uit en frituur ze goudbruin.")
    print("3. Bereid de saus:")
    
    # Hier roepen we de functie aan die we als argument hebben gekregen
    sauce_function()
    
    print("4. Dip de donut in de saus en laat afkoelen.")
    print("-----------------------------\n")

# --- De aanroepen (calls) ---

# Maak een chocoladedonut
make_donut(make_chocolate_sauce)

# Maak een carameldonut
make_donut(make_caramel)