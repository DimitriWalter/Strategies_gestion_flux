import time
import random as rd
import numpy as np
import math


class Source(object):
    id = 0  # variable id pour les sources
    def __init__(self, lambd):
        Source.id += 1  # incrémente de + 1 à chaque création d'une source
        self.id = Source.id  # id de la source (appelle genere_id)
        self.paquets = list()  # liste des paquets à envoyer par la source
        self.taux_arrive = lambd

    def generer_paquet(self):  # fonction qui créer des paquets composées de bits
        paquets = list()
        for _ in range(self.taux_arrive):
            contenu = list()
            for i in range(rd.randint(2, 9)):
                contenu.append("")
                for _ in range(5):
                    contenu[i] += str(rd.randint(0, 1))

            paquets.append(Paquet(self.id, contenu, self.taux_arrive))

        return paquets
    
    def arrive(self, paquet, buffer):  # fonction d'arrivée des paquets dans le buffer
        if paquet.taux_arrive > Buffer.taux_lien:
            buffer + paquet
        else:
            buffer.paquets_transmis.append(paquet)


class Buffer(object):
    id = 0  # variable id pour les buffer
    taux_lien = 2  # taux de transmission du lien
    def __init__(self, capacite):
        Buffer.id += 1
        self.id = Buffer.id
        self.capacite = capacite  # capacité C du buffer
        self.queue = list()  # file d'attente du buffer
        self.paquets_perdus = list()  # paquets perdus du buffer
        self.paquets_transmis = list()  # paquets transmis

    def __add__(self, paquet):  # fonction d'insertion de paquets dans le buffer
        if len(self.queue) < self.capacite:
            self.queue.append(paquet)
            print(f"Paquet {paquet.id}, {paquet.contenu} arrivé dans le buffer")
        else:
            self.paquets_perdus.append(paquet)
            print("Buffer plein")

    def retrait(self):  # fonction de retrait d'un paquet du buffer
        if self.queue:
            paquet = self.queue.pop(0)
            print(f"Paquet {paquet.id} est sorti du buffer")
            self.paquets_transmis.append(paquet)


class Paquet(object):
    id = 0  # variable id pour les paquets
    def __init__(self, source_id, contenu, taux):
        Paquet.id += 1
        self.id = Paquet.id
        self.source_id = source_id  # id de la source du paquet
        self.contenu = contenu  # contenu du paquet
        self.taille = len(contenu) * 100  # taille des paquets en bits (taille fictive)
        self.taux_arrive = taux

    def __str__(self):
        return f"Paquet {self.contenu} de source {self.source_id}"
    

def test():
    s1 = Source(4)
    buffer = Buffer(15)
    while True:
        paquets = s1.generer_paquet()
        for elt in paquets:
            s1.arrive(elt, buffer)


if __name__ == "__main__":
    test()
    print(rd.uniform(0, 0.1))
