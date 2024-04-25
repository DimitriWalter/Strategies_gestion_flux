class Buffer:
    def __init__(self, b_capacite=100):
        # Initialise un objet Buffer avec une capacité définie, des statistiques de pertes et de réception, et un buffer vide
        self.buffer = [[] for _ in range(b_capacite)]
        self.capacite = b_capacite  # Capacité actuelle du buffer
        self.pertes = 0  # Nombre de paquets perdus
        self.rec = 0  # Nombre de paquets reçus
        self.trans = 0  # Nombre de paquets transmis

    def capacite_minus(self, amount):
        # Réduit la capacité du buffer de la quantité donnée
        self.capacite -= amount
        # Supprime des éléments du buffer pour correspondre à la nouvelle capacité
        for _ in range(amount):
            self.buffer.remove(self.buffer[-1])

    def capacite_add(self, amount):
        # Augmente la capacité du buffer de la quantité donnée
        self.capacite += amount
        # Ajoute des listes vides au buffer pour refléter la nouvelle capacité
        for _ in range(amount):
            self.buffer.append([])

    def arrivee_paquet(self, paquet):
        # Traite l'arrivée d'un nouveau paquet
        if self.capacite > 0:
            self.insertion_paquet(paquet)  # Insère le paquet dans le buffer s'il y a de la place
        elif self.capacite == 0:
            self.pertes += 1  # Incrémente le compteur de pertes si le buffer est plein

    def insertion_paquet(self, paquet):
        # Insère un paquet dans le buffer
        for i in range(len(self.buffer)):
            if self.buffer[i] == []:
                self.buffer[i] = paquet  # Place le paquet dans la première liste vide trouvée
                self.capacite -= 1  # Réduit la capacité du buffer
                break

    def retrait_paquet(self, paquet):
        # Retire un paquet du buffer
        self.buffer.remove(paquet)
        self.capacite_add(1)  # Augmente la capacité du buffer après le retrait du paquet

    def transmission_paquet(self, paquet, destination):
        # Transmet un paquet à une destination spécifiée
        if destination.capacite > 0:
            destination.insertion_paquet(paquet)  # Si la destination a de la place, insère le paquet là-bas
            self.retrait_paquet(paquet)  # Retire le paquet du buffer actuel
        elif destination.capacite == 0 or destination.capacite <= 0:
            destination.pertes += 1  # Si la destination est pleine, incrémente le compteur de pertes
            self.retrait_paquet(paquet)  # Retire quand même le paquet du buffer actuel

    def afficher_buffer(self):
        # Affiche le contenu actuel du buffer
        print(self.buffer)

    def afficher_capacite(self):
        # Affiche la capacité actuelle du buffer
        print(self.capacite)


if __name__ == '__main__':
    print("hello world!")  # Test pour valider le bon fonctionnement du code