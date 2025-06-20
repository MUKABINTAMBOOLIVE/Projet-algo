def recherche_par_titre(livres, titre):
    return [livre for livre in livres if titre.lower() in livre["titre"].lower()]

def recherche_par_auteur(livres, auteur):
    return [livre for livre in livres if auteur.lower() in livre["auteur"].lower()]

def recherche_par_isbn(livres, isbn):
    return [livre for livre in livres if livre["isbn"] == isbn]
