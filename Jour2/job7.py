import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def obtenir_employes_salaire_au_dessus_de_3000(self):
        self.cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
        return self.cursor.fetchall()

    def obtenir_employes_et_services(self):
        query = """
        SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service
        FROM employe e
        JOIN service s ON e.id_service = s.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def mettre_a_jour_salaire(self, employe_id, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (nouveau_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

employe_manager = Employe(host='localhost', user='root', password='Nostale2004@', database='job7')

employe_manager.ajouter_employe('Bernard', 'Luc', 3600.00, 2)

employes_haut_salaire = employe_manager.obtenir_employes_salaire_au_dessus_de_3000()
print("Employés avec salaire supérieur à 3000 €:", employes_haut_salaire)

employes_services = employe_manager.obtenir_employes_et_services()
print("\nEmployés et leurs services:", employes_services)

employe_manager.mettre_a_jour_salaire(1, 4000.00)

employe_manager.supprimer_employe(4)

employe_manager.close()
