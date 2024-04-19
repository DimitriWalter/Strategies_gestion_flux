import time
import random as rd
import numpy as np


class Source(object):
    poisson_lambda = 5
    intervalle = 1
    id = 0  # variable id pour les sources
    def __init__(self):
        Source.id += 1  # incrémente de + 1 à chaque création d'une source
        self.id = Source.id  # id de la source (appelle genere_id)
        self.paquets = list()  # liste des paquets à envoyer par la source
        self.taux_arrive = 120

    def generer_paquet(self):  # fonction qui créer des paquets composées de bits
        num_packets = np.random.poisson(Source.poisson_lambda * Source.intervalle)
        paquets = list()
        for _ in range(num_packets):
            contenu = list()
            for i in range(rd.randint(2, 10)):
                contenu.append("")
                for _ in range(rd.randint(2, 12)):
                    contenu[i] += str(rd.randint(0, 1))

            paquets.append(Paquet(self.id, contenu, self.taux_arrive))

        return paquets


class Buffer(object):
    id = 0  # variable id pour les buffer
    taux_lien = 100  # taux de transmission du lien
    def __init__(self, capacite):
        Buffer.id += 1
        self.id = Buffer.id
        self.capacite = capacite  # capacité C du buffer
        self.queue = list()  # file d'attente du buffer
        self.paquets_perdus = list()  # paquets perdus du buffer
        self.paquets_transmis = list()  # paquets transmis

    def __add__(self, paquet):
        if len(self.queue()) < self.capacite():
            self.queue.append(paquet)
        else:
            self.paquets_perdus.append(paquet)
            print("Buffer plein")

    def __sub__(self):
        self.paquets_transmis.append(self.paquets_perdus.pop())


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
    s1 = Source()
    buffer = Buffer(10)
    paquets = s1.generer_paquet()
    for elt in paquets:
        print(elt)


if __name__ == "__main__":
    test()
