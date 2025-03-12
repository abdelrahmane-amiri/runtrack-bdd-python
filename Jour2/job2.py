import mysql.connector


conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="Nostale2004@",
    database="LaPlateforme" )

if conn.is_connected():
    print("Connexion réussie à la base de données 'LaPlateforme'.")

cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiant")

etudiants = cursor.fetchall()

for etudiant in etudiants:
    print(etudiant)