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
