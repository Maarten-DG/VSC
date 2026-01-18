import sqlite3

# 1. Verbinding maken (maakt het bestand aan als het nog niet bestaat)
connection = sqlite3.connect('mijn_school.db')
cursor = connection.cursor()

# 2. De tabel Students aanmaken
cursor.execute("CREATE TABLE IF NOT EXISTS Students (FirstName TEXT, LastName TEXT)")

# 3. Gegevens toevoegen
# We gebruiken een lijst van tuples voor jouw data en die van klasgenoten
studenten_data = [
    ('JouwVoornaam', 'JouwAchternaam'),
    ('Karel', 'De Grote'),
    ('Marie', 'Curie')
]

# Gebruik executemany om de hele lijst in één keer toe te voegen
cursor.executemany("INSERT INTO Students (FirstName, LastName) VALUES (?, ?)", studenten_data)

# 4. Belangrijk: De wijzigingen opslaan en de verbinding verbreken
connection.commit()
connection.close()

print("Database succesvol aangemaakt en gevuld!")