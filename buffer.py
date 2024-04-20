class Buffer:
    def __init__(self, b_capacite=100):
        self.buffer = [[] for _ in range(b_capacite)]
        self.capacite = b_capacite
        self.pertes = 0

    def capacite_minus(self, amount):
        self.capacite -= amount
        for _ in range(amount):
            self.buffer.remove(self.buffer[-1])

    def capacite_add(self, amount):
        self.capacite += amount
        for _ in range(amount):
            self.buffer.append([])

    def arrivee_paquet(self, paquet):
        if self.capacite > 0:
            self.insertion_paquet(paquet)
        elif self.capacite == 0:
            self.pertes += 1

    def insertion_paquet(self, paquet):
        for i in range(len(self.buffer)):
            if self.buffer[i] == []:
                self.buffer[i] = paquet
                self.capacite -= 1
                break

    def retrait_paquet(self, paquet):
        self.buffer.remove(paquet)
        self.capacite_add(1)


    def transmission_paquet(self, paquet, destination):
        if destination.capacite > 0:
            destination.insertion_paquet(paquet)
            self.retrait_paquet(paquet)
        elif destination.capacite == 0 or destination.capacite <= 0:
            destination.pertes += 1
            self.retrait_paquet(paquet)

    def afficher_buffer(self):
        print(self.buffer)

    def afficher_capacite(self):
        print(self.capacite)


if __name__ == '__main__':
    print("hello world!")