from source import *
from time import time

class Paquet:
    def __init__(self):
        self.paquet = Source().generer_paquet()
        self.paquet_temps_arrivee = time()
    def afficher_paquet(self):
        print(self.paquet)

    def get_paquet(self):
        return self.paquet


if __name__ == '__main__':
    print("hello world")
