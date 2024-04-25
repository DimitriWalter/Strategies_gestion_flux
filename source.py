import random
import uuid
from random_ip_generator import random_ip_for_country


def genere_adresse():
    return random_ip_for_country('FR')

def genere_taille():
    return random.randint(1, 100000)


class Source:
    def __init__(self):
        
        self.id : str = str(uuid.uuid4())
        self.adresse : str = str(genere_adresse())
        self.destination : str = str(genere_adresse())
        self.taille : int = genere_taille()

    def generer_paquet(self) -> dict:
        self.paquet = {
            "id": self.id,
            "adresse_source": self.adresse,
            "destination": self.destination,
            "taille": self.taille
        }
        return self.paquet
    
    def get_source(self):
        return self.paquet
    
if __name__ == '__main__':
    a = Source()
    a.generer_paquet()
    print(a.get_source())
