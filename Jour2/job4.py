import mysql.connector


conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="Nostale2004@",
    database="LaPlateforme" )

if conn.is_connected():
    print("Connexion réussie à la base de données 'LaPlateforme'.")

cursor = conn.cursor()

cursor.execute("SELECT * FROM salle")

salles = cursor.fetchall()

for salle in salles:
    print(f"Nom: {salle[0]}, Capacité: {salle[3]}")
        
        # Exécution de la requête SQL pour calculer la superficie totale
cursor.execute("SELECT SUM(superficie) FROM etage")
superficie_totale = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

cursor.execute("SELECT SUM(capacite) FROM salle")
capacite_totale = cursor.fetchone()[0]
print(f"La capacité totale des salles est de {capacite_totale} personnes")