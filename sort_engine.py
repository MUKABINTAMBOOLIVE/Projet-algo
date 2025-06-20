def trier_par_titre(livres):
    return sorted(livres, key=lambda x: x["titre"])

def trier_par_auteur(livres):
    return sorted(livres, key=lambda x: x["auteur"])
