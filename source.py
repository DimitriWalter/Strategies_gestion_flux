import random
import uuid
from random_ip_generator import random_ip_for_country


def genere_adresse():
    # Génère une adresse IP pour le pays 'FR'
    return random_ip_for_country('FR')


def genere_taille():
    # Génère une taille aléatoire pour un paquet, entre 1 et 100000 octets
    return random.randint(1, 100000)


class Source:
    def __init__(self):
        # Initialise un objet Source avec un identifiant unique, une adresse
        # source de destination aléatoire, et une taille de paquet aléatoire
        self.id: str = str(uuid.uuid4())  # Identifiant unique pour la source
        self.adresse: str = str(genere_adresse())  # Adresse IP source
        self.destination: str = str(genere_adresse())  # Adresse IP destination
        self.taille: int = genere_taille()  # Taille du paquet

    def generer_paquet(self) -> dict:
        # Génère un paquet avec les attributs de la source et
        # le retourne sous forme de dictionnaire
        self.paquet = {
            "id": self.id,
            "adresse_source": self.adresse,
            "destination": self.destination,
            "taille": self.taille
        }
        return self.paquet

    def get_source(self):
        # Renvoie les informations de la source sous forme de dictionnaire
        return self.paquet


if __name__ == '__main__':
    a = Source()
    a.generer_paquet()
    print(a.get_source())    # Test pour valider le bon fonctionnement du code
