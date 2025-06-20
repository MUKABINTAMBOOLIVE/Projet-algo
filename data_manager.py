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
