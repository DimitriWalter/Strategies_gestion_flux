from source import *
from time import time


class Paquet:
    def __init__(self):
        # Initialise un objet Paquet avec un paquet généré et un temps d'arrivée
        self.paquet = Source().generer_paquet()  # Génère un paquet en utilisant la classe Source()
        self.paquet_temps_arrivee = time()  # Enregistre le temps d'arrivée du paquet

    def afficher_paquet(self):
        # Affiche le contenu du paquet
        print(self.paquet)

    def get_paquet(self):
        # Renvoie le paquet
        return self.paquet


if __name__ == '__main__':
    print("hello world")  # Test pour valider le bon fonctionnement du code
