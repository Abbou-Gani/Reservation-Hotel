#un class livre qui prend en paramétre le titre , l'auteur et l'année
class Livre:
    def __init__(self, titre , auteur, quantite=1):
        self.titre = titre
        self.auteur = auteur
        self.quantite = quantite
    
    def est_disponible(self):
        return self.quantite>0
        
    def emprunt(self):
        if self.est_disponible():
            self.quantite -=1 

    def retourner(self):
        self.quantite+=1

    def __str__(self):
        return (f"Titre: {self.titre}, Auteur: {self.auteur}, Quantité: {self.quantite}\n")              
    
class Membres:
    def __init__(self, Id_Membre, nom, prenom, numero, email):
        self.Id_Membre = Id_Membre #Un identifiant unique pour le client
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.email = email
        self.livres_empruntes = []

    def emprunter_livre(self, titre_du_livre):
        self.livres_empruntes.append(titre_du_livre)

    def retourner_livre(self, titre_du_livre):
        if titre_du_livre in self.livres_empruntes:
            self.livres_empruntes.remove(titre_du_livre) 

    def __str__(self):
            return(f"ID : {self.Id_Membre}|NOM: {self.nom}|PRENOM : {self.prenom}")          


class Gestion_Bibliothèque:
    def __init__(self ):
        self.liste_livres = []
        self.liste_Membres = [] 

    def afficher_livres(self):
        print(f" Nombre de livres dans la liste = {len(self.liste_livres)}")
        # -----------------------------------
        if len(self.liste_livres)== 0:
            print("La bibliothèque est vide")
        else:
            print("\n ---les livres disponible dans la bibliothèque")
            for livre in self.liste_livres:
                if livre.est_disponible():
                    print(livre)    

    def ajouter_livre(self, nouveau_livre):
        for livre_existant in self.liste_livres:
            if livre_existant.titre == nouveau_livre.titre and livre_existant.auteur == nouveau_livre.auteur:
                livre_existant.quantite += nouveau_livre.quantite
                print(f"la quantité du livre {nouveau_livre.titre} a augmenté de {nouveau_livre.quantite}")
                return
            
        self.liste_livres.append(nouveau_livre)
        print(f"Nouveau livre {nouveau_livre.titre} ajouté a la bibliothèque")

    def inscrire_membre(self, nouveau_membre):
        self.liste_Membres.append(nouveau_membre)        
        print(f"Membre {nouveau_membre} crée avec succès")
    
    def emprunter_livre(self,livre, membre):
        if livre in self.liste_livres:
            if livre.quantite> 0:
                livre.quantite -=1
                membre.emprunter_livre(livre.titre)
                print(f"Mr {membre.nom} a emprunté le livre :{livre.titre} \n quantite  restante: {livre.quantite}")
            else:
                print(f"le livre de {livre.titre} n'est pas disponible")
        else:
            print("ce livre n'est pas dans la bibliothèque")

    def supprimer_livre(self, livre):
        if livre in self.liste_livres:
            self.liste_livres.remove(livre)
            print("le livre a été supprimer de la bibliothèque")
        else:
            print("le livre n'est pas dans la bibliothèque")

    def afficher_membre(self):
        if not self.liste_Membres:
            print("\n Ancun membre inscrit")
        else:
            print("\n-- liste des membres---")
            for membre in self.liste_Membres:
                print(membre)            

def affiche_menu():
    print(" 1 - Afficher les livres disponibles")            
    print(" 2 - Ajouter un livre")            
    print(" 3 - Supprimer un livre")            
    print(" 4 - Inscrire un membre")             
    print(" 5 - Emprunter un livre")             
    print(" 6 - Afficher les membres inscrits")             
    print(" 7 - Quitter")   

def main():
    bibliothèque = Gestion_Bibliothèque()

    # AJOUTE DES LIVRES DANS LA LISTE DES LIVRES AU DÉMARRAGE
    livre_disponible = [
        Livre("Informatique", "Abdou ", 5),
        Livre("Math", "Dramane ", 2),
        Livre("Physique", "Hamed ", 7)
    ]
    for livre in livre_disponible:
        bibliothèque.ajouter_livre(livre)
    # FIN DE L'AJOUT

    while True:
        affiche_menu()
        choix = input("Faites un choix en (1-7)")

        if choix == '1':
            bibliothèque.afficher_livres()
            
        elif choix == '2':
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            quantite = int(input("Quantité : "))   
            nouveau_livre = Livre(titre, auteur, quantite)
            bibliothèque.ajouter_livre(nouveau_livre)
            
        elif choix == '3':
            bibliothèque.afficher_livres()
            titre = input("Titre du livre à supprimer : ")
            livre_trouve = None
            for livre in bibliothèque.liste_livres:
                if livre.titre == titre:
                    livre_trouve = livre
                    break
                    
            if livre_trouve:
                bibliothèque.supprimer_livre(livre_trouve)
            else:
                print("Livre non trouvé")
                
        elif choix == '4':
            id_membre = input("ID du membre : ")
            nom = input("Nom du membre : ")
            prenom = input("Prénom du membre : ")
            numero = input("Numéro de téléphone : ")
            email = input("Email : ")
            nouveau_membre = Membres(id_membre, nom, prenom, numero, email)
            bibliothèque.inscrire_membre(nouveau_membre)
            
        elif choix == '5':
            nom = input("Entrez votre nom: ")
            membre_trouve = None
            for membre in bibliothèque.liste_Membres:
                if membre.nom == nom:
                    membre_trouve = membre
                    break  
                    
            if membre_trouve is None:
                print("Membre non trouvé")
            else:
                titre_livre = input("Titre du livre à emprunter: ")
                livre_trouve = None
                for livre in bibliothèque.liste_livres:
                    if livre.titre == titre_livre:
                        livre_trouve = livre
                        break
                        
                if livre_trouve is None:
                    print("Livre non trouvé")
                else:
                    bibliothèque.emprunter_livre(livre_trouve, membre_trouve)
                    
        elif choix == '6':
            bibliothèque.afficher_membre()
            
        elif choix == '7':
            print("Au revoir et a bientôt")
            break
            
        else:
            print("Option introuvable")       


if __name__ == "__main__":
    main()                             
