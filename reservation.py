from datetime import date

class Chambre:
    def __init__(self, numero_chambre, type_chambre,prix_nuit):
        self.numero_chambre = numero_chambre
        self.type_chambre = type_chambre
        self.prix_nuit = prix_nuit
        self.est_disponible = True

    def __str__(self):
        statut = "Disponible" if self.est_disponible else "Non disponible"
        return f"la chambre type {self.type_chambre} au numero {self.numero_chambre} est {self.est_disponible} pour la nuit a {self.prix_nuit}fc"    
    
class Client:
    def __init__(self, id_client, Nom, prenom,numero_telephone,email):
        self.id_client = id_client #Un identifiant unique pour le client
        self.Nom = Nom
        self.prenom = prenom
        self.numero_telephone = numero_telephone
        self.email = email

    def __str__(self):
        return f"Client {self.id_client} Du nom de {self.Nom} {self.prenom} ({self.email})" 

class Reservation:
    def __init__(self, id_reservation, client_obj, chambre_obj, date_arrive, dete_depart,):
        self.id_reservation = id_reservation  #Un identifiant unique pour la reservation
        self.client = client_obj
        self.chambre = chambre_obj 
        self.date_arrive = date_arrive
        self.date_depart = dete_depart
        self.statut = "Confirmé"      

    def __str__(self):
        return f"Réservation #{self.id_reservation} - {self.client} - {self.chambre} - Du {self.date_arrive} au {self.date_depart} - Statut: {self.statut}" 
    

class Gestion_Hotel:
    def __init__(self):
        self.liste_chambres = [] 
        self.liste_clients = []
        self.liste_reservations = []  

    
    def ajouter_chambre(self, chambre):
        self.liste_chambres.append(chambre)

    def ajouter_client(self, client):
        self.liste_clients.append(client)    

    def afficher_chambre_disponible(self):
        print(f" Nombre de chambre dans la liste = {len(self.liste_chambres)}")
        # -----------------------------------
        if len(self.liste_chambres)== 0:
            print("il y'a aucune chambre disponible")
        else:
            print("\n ---les chambre disponible sont: ---")
            for chambre  in self.liste_chambres:
                if chambre.est_disponible:
                    print(chambre)   

    def effectuer_reservation(self, id_client , numero_chambre, date_arrive, date_depart):
        client_trouve = None
        for client in self.liste_clients:
            if client.id_client == id_client:  # Compare avec l'id reçu en paramètre
                client_trouve = client
                break
            if client_trouve is None:
                print("Client non trouvé")
                return 

        chambre_trouve = None
        for chambre in self.liste_chambres:
            if chambre.numero_chambre == numero_chambre: #Compare avec le numero de chambre reçu en paramètre
                chambre_trouve = chambre
                break
            if chambre_trouve is None:
                print("chambre non touvé")
                return
            if not chambre_trouve.est_disponible:
                print("chambre non disponible")
                return
            
        date_arrivee_obj = date.fromisoformat(date_arrive)
        date_depart_obj = date.fromisoformat(date_depart)    

        id_reservation = len(self.liste_reservations)+1
        nouvelle_reservation = Reservation(id_reservation, client_trouve, chambre_trouve, date_arrivee_obj, date_depart_obj)
        self.liste_reservations.append(nouvelle_reservation)
        chambre_trouve.est_disponible = False
        print(f"Reservation {id_reservation} confirmé par {client_trouve.prenom} {client_trouve.Nom}")

    def afficher_reservation_client(self, id_client):
        reservations_trouvees = []
        for reservation in self.liste_reservations:
            if reservation.client.id_client == id_client:
                reservations_trouvees.append(reservation)

            if not reservations_trouvees : #si la liste de reservation est vide
                print("Aucune reservation trouvé pour ce client")

            else:
                print(f"\n-- Reservation du client #{id_client}") 
                for reservation in reservations_trouvees:
                    print(reservation)

    def annuler_reservation(self , id_reservation):
        for reservation in self.liste_reservations:
            if reservation.id_reservation == id_reservation:
                reservation.statut = "Annulée"
                reservation.chambre.est_disponible = True
                print(f"Réservation #{id_reservation} annulée.")
                return
        print("Réservation non trouvée.")

    def creer_client(self, nouveau_client):
        self.liste_clients.append(nouveau_client)        
        print(f"client {nouveau_client.Nom} {nouveau_client.prenom} crée avec succès") 

    def afficher_client(self):
        if not self.liste_clients:
            print("\n Ancun client enregistré")
        else:
            print("\n-- liste des client---")
            for client in self.liste_clients:
                print(client)        

def affiche_Menu():
    print("1 - Afficher les chambre disponible")        
    print("2 - Effectuer une reservation")        
    print("3 - Afficher la reservation d'un client")        
    print("4 - Annuler une reservation")        
    print("5 - créer un client")        
    print("6 - Afficher les client")        
    print("7 - Ajouter un chambre")        
    print("8 - Quitter") 

def main():
    hotel = Gestion_Hotel()

    #ajouter des chambre au demarrage

    chambre101 = Chambre(101, "simple",10000.0)
    chambre102 = Chambre(102, "double",20000.0)
    chambre103 = Chambre(103, "suite",30000.0)

    hotel.ajouter_chambre(chambre101)
    hotel.ajouter_chambre(chambre102)
    hotel.ajouter_chambre(chambre103)

    #ajouter des client au demarrage

    client1 =Client(1,"Sawadogo","Abdou", 67654005, "sabdougani@gmail.com") 
    client2 =Client(2,"Santi","martin", 52874226, "martin@gmail.com") 

    hotel.ajouter_client(client1)
    hotel.ajouter_client(client2)

    while True:
        affiche_Menu()
        choix = input("Faites un choix entre (1-7)")

        if choix == '1':
            hotel.afficher_chambre_disponible()

        elif choix == '2':
            id_client = int(input("ID client entre (1-20):"))
            num_chambre = int(input("numero de chambre : ")) 
            date_arrivee = input("Date arrivée (AAAA-MM-JJ) : ")# 2025-10-5
            date_depart = input("Date départ (AAAA-MM-JJ) : ")# 2025-10-5
            hotel.effectuer_reservation(id_client, num_chambre, date_arrivee, date_depart)   

        elif choix == '3':
            id_client = int(input("ID client : "))
            hotel.afficher_reservation_client(id_client)

        elif choix == '4':
            id_reservation = int(input("ID réservation à annuler : "))
            hotel.annuler_reservation(id_reservation)

        elif choix == '5':
            # Créer un nouveau client
            id_client = int(input("Nouvel ID client : "))
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            telephone = input("Téléphone : ")
            email = input("Email : ")
            nouveau_client = Client(id_client, nom, prenom, telephone, email)
            hotel.creer_client(nouveau_client)

        elif choix == '6':
            hotel.afficher_client()

        elif choix == '7':
            numero_chambre = int(input("Numero de chambre : ")) 
            type_chambre = input("Entrez un type de chambre : ")
            prix_de_chambre = float(input("Entrez le prix de la chambre :"))
            nouvelle_chambre = Chambre(numero_chambre, type_chambre, prix_de_chambre)
            hotel.ajouter_chambre(nouvelle_chambre)
            print(f"le chambre {numero_chambre} de type {type_chambre} au prix {prix_de_chambre} ajoutée avec succès")
               

        elif choix == '8':
            print("Au revoir !")
            break
        else:
            print("Option invalide. faites un choix entre (1-7).") 

if __name__ == "__main__":
    main()                               