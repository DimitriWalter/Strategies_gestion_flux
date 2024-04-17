import time
import random as rd


class Source(object):
    id = 0  # variable id pour les sources
    def __init__(self):
        Source.id += 1  # incrémente de + 1 à chaque création d'une source
        self.id = Source.id  # id de la source (appelle genere_id)
        self.poisson = None 
        self.paquets = list()  # liste des paquets à envoyer par la source

    def generer_paquet(self):  # fonction qui créer des paquets composées de bits
        contenu = list()
        for i in range(rd.randint(1, 10)):
            contenu.append("")
            for _ in range(rd.randint(1, 12)):
                contenu[i] += str(rd.randint(0, 1))

        paquet = Paquet(self.id, contenu)
        self.paquets.append(paquet)

        return paquet


class Buffer(object):
    id = 0  # variable id pour les buffer
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
    def __init__(self, source_id, contenu):
        Paquet.id += 1
        self.id = Paquet.id
        self.source_id = source_id  # id de la source du paquet 
        self.contenu = contenu  # contenu du paquet
        self.taille = len(contenu)  # taille du paquet

    def __str__(self):
        return f"Paquet {self.contenu} de source {self.source_id}"
    

def test():
    s1 = Source()
    for _ in range(5):
        print(s1.generer_paquet())


if __name__ == "__main__":
    test()
