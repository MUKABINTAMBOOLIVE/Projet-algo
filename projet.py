import json

FICHIER_DONNEES = "livres.json"

def charger_donnees():
    
    try:
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def sauvegarder_donnees(livres):
    with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
        json.dump(livres, f, ensure_ascii=False, indent=4)

def ajouter_livre(livres, livre):
    livres.append(livre)

def supprimer_livre(livres, isbn):
    livres[:] = [livre for livre in livres if livre["isbn"] != isbn]
def recherche_par_titre(livres, titre):
    return [livre for livre in livres if titre.lower() in livre["titre"].lower()]

def recherche_par_auteur(livres, auteur):
    return [livre for livre in livres if auteur.lower() in livre["auteur"].lower()]

def recherche_par_isbn(livres, isbn):
    return [livre for livre in livres if livre["isbn"] == isbn]
def trier_par_titre(livres):
    return sorted(livres, key=lambda x: x["titre"])

def trier_par_auteur(livres):
    return sorted(livres, key=lambda x: x["auteur"])
def emprunter_livre(livres, isbn, emprunteur):
    for livre in livres:
        if livre["isbn"] == isbn:
            livre["emprunte"] = True
            livre["emprunteur"] = emprunteur
            return True
    return False

def retourner_livre(livres, isbn):
    for livre in livres:
        if livre["isbn"] == isbn:
            livre["emprunte"] = False
            livre["emprunteur"] = None
            return True
    return False
from data_manager import (
    charger_donnees, sauvegarder_donnees,
    ajouter_livre, supprimer_livre
)
from search_engine import (
    recherche_par_titre, recherche_par_auteur, recherche_par_isbn
)
from sort_engine import (
    trier_par_titre, trier_par_auteur
)
from loan_manager import (
    emprunter_livre, retourner_livre
)

def afficher_livre(livre):
    etat = "Emprunté" if livre["emprunte"] else "Disponible"
    print(f"- {livre['titre']} | {livre['auteur']} | ISBN: {livre['isbn']} | Statut: {etat}")

def afficher_menu():
    livres = charger_donnees()
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Rechercher un livre")
        print("4. Trier les livres")
        print("5. Emprunter un livre")
        print("6. Retourner un livre")
        print("7. Lister les livres")
        print("8. Rapport")
        print("9. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            isbn = input("ISBN : ")
            livre = {"titre": titre, "auteur": auteur, "isbn": isbn, "emprunte": False, "emprunteur": None}
            ajouter_livre(livres, livre)
            sauvegarder_donnees(livres)
            print("✔ Livre ajouté.")

        elif choix == "2":
            isbn = input("ISBN du livre à supprimer : ")
            supprimer_livre(livres, isbn)
            sauvegarder_donnees(livres)
            print("✔ Livre supprimé.")

        elif choix == "3":
            critere = input("Rechercher par (titre / auteur / isbn) : ").lower().strip()
            terme = input("Mot-clé : ").strip()
            if critere == "titre":
                resultats = recherche_par_titre(livres, terme)
            elif critere == "auteur":
                resultats = recherche_par_auteur(livres, terme)
            elif critere == "isbn":
                resultats = recherche_par_isbn(livres, terme)
            else:
                print("❌ Critère invalide.")
                continue
            for livre in resultats:
                afficher_livre(livre)

        elif choix == "4":
            critere = input("Trier par (titre / auteur) : ").lower().strip()
            if critere == "titre":
                livres = trier_par_titre(livres)
            elif critere == "auteur":
                livres = trier_par_auteur(livres)
            else:
                print("❌ Critère invalide.")
                continue
            print("✔ Liste triée.")
            for livre in livres:
                afficher_livre(livre)

        elif choix == "5":
            isbn = input("ISBN du livre à emprunter : ")
            nom = input("Nom de l’emprunteur : ")
            if emprunter_livre(livres, isbn, nom):
                print("📚 Livre emprunté avec succès.")
            else:
                print("❌ Livre non disponible.")
            sauvegarder_donnees(livres)

        elif choix == "6":
            isbn = input("ISBN du livre à retourner : ")
            if retourner_livre(livres, isbn):
                print("🔁 Livre retourné.")
            else:
                print("❌ Livre non trouvé.")
            sauvegarder_donnees(livres)

        elif choix == "7":
            filtre = input("Afficher (tous / empruntés / disponibles) : ").lower().strip()
            if filtre == "empruntés":
                a_afficher = [l for l in livres if l["emprunte"]]
            elif filtre == "disponibles":
                a_afficher = [l for l in livres if not l["emprunte"]]
            else:
                a_afficher = livres
            for livre in a_afficher:
                afficher_livre(livre)

        elif choix == "8":
            total = len(livres)
            empruntes = sum(1 for l in livres if l["emprunte"])
            dispo = total - empruntes
            print(f"\n📊 RAPPORT:")
            print(f"Total de livres : {total}")
            print(f"Livres empruntés : {empruntes}")
            print(f"Livres disponibles : {dispo}")

        elif choix == "9":
            sauvegarder_donnees(livres)
            print("💾 Données sauvegardées. À bientôt !")
            break

        else:
            print("❌ Choix non reconnu.")
