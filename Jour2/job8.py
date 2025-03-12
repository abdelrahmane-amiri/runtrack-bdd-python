import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.conn.commit()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (id_cage,))
        self.conn.commit()

    def supprimer_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (id_animal,))
        self.conn.commit()

    def modifier_cage(self, id_cage, superficie, capacite_max):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        values = (superficie, capacite_max, id_cage)
        self.cursor.execute(query, values)
        self.conn.commit()

    def modifier_animal(self, id_animal, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_animaux(self):
        self.cursor.execute("SELECT * FROM animal")
        return self.cursor.fetchall()

    def afficher_animaux_par_cage(self):
        query = """
        SELECT a.nom, a.race, a.date_naissance, a.pays_origine, c.id AS cage_id, c.superficie, c.capacite_max
        FROM animal a
        JOIN cage c ON a.id_cage = c.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def superficie_totale_cages(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        return self.cursor.fetchone()[0]

    
    def close(self):
        self.cursor.close()
        self.conn.close()

def menu():
    zoo = Zoo(host='localhost', user='root', password='Nostale2004@', database='zoo')

    while True:
        print("\n1. Ajouter une cage")
        print("2. Ajouter un animal")
        print("3. Supprimer une cage")
        print("4. Supprimer un animal")
        print("5. Modifier une cage")
        print("6. Modifier un animal")
        print("7. Afficher tous les animaux")
        print("8. Afficher les animaux par cage")
        print("9. Calculer la superficie totale des cages")
        print("10. Quitter")
        
        choix = input("Choisissez une option: ")
        
        if choix == "1":
            superficie = float(input("Superficie de la cage: "))
            capacite_max = int(input("Capacité maximum: "))
            zoo.ajouter_cage(superficie, capacite_max)
        
        elif choix == "2":
            nom = input("Nom de l'animal: ")
            race = input("Race: ")
            id_cage = int(input("ID de la cage: "))
            date_naissance = input("Date de naissance (YYYY-MM-DD): ")
            pays_origine = input("Pays d'origine: ")
            zoo.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)
        
        elif choix == "3":
            id_cage = int(input("ID de la cage à supprimer: "))
            zoo.supprimer_cage(id_cage)
        
        elif choix == "4":
            id_animal = int(input("ID de l'animal à supprimer: "))
            zoo.supprimer_animal(id_animal)
        
        elif choix == "5":
            id_cage = int(input("ID de la cage à modifier: "))
            superficie = float(input("Nouvelle superficie: "))
            capacite_max = int(input("Nouvelle capacité maximum: "))
            zoo.modifier_cage(id_cage, superficie, capacite_max)
        
        elif choix == "6":
            id_animal = int(input("ID de l'animal à modifier: "))
            nom = input("Nom de l'animal: ")
            race = input("Race: ")
            id_cage = int(input("ID de la cage: "))
            date_naissance = input("Date de naissance (YYYY-MM-DD): ")
            pays_origine = input("Pays d'origine: ")
            zoo.modifier_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)
        
        elif choix == "7":
            animaux = zoo.afficher_animaux()
            print("Animaux dans le zoo:")
            for animal in animaux:
                print(animal)
        
        elif choix == "8":
            animaux_par_cage = zoo.afficher_animaux_par_cage()
            print("Animaux dans chaque cage:")
            for animal in animaux_par_cage:
                print(animal)
        
        elif choix == "9":
            superficie_totale = zoo.superficie_totale_cages()
            print(f"Superficie totale des cages: {superficie_totale} m²")
        
        elif choix == "10":
            zoo.close()
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


menu()
