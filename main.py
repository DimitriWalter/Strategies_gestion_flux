# mail prof
# perla.hajjar@sqy.fr*


import customtkinter
import math
import random


from buffer import *
from paquet import *
from source import *
from time import time


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Initialise l'application avec le titre
        self.title("Stratégies de gestion de flux")
        # Calcul des statistiques globales de capacité, pertes, transmission et réception pour tous les éléments du système
        self.capaciteT = source.capacite + t1.capacite + t2.capacite + file_attente.capacite + t3.capacite + dest.capacite
        self.pertesT = source.pertes + t1.pertes + t2.pertes + t3.pertes + file_attente.pertes + dest.pertes
        self.transT = source.trans + t1.trans + t2.trans + t3.trans + file_attente.trans + dest.trans
        self.recT = source.rec + t1.rec + t2.rec + t3.rec + file_attente.rec + dest.rec
        self.flag = True  # Indicateur pour une certaine fonctionnalité
        self.temps = [0]  # Liste pour enregistrer le temps
        font0 = ('Helvetica', 20)  # Définition de la police de caractères

        # titres horizontaux
        self.titreBuffer = customtkinter.CTkLabel(master=self, text="Buffers", font=font0, text_color="#0c7399")
        self.paquetsT = customtkinter.CTkLabel(master=self, text="Paquets transmis", font=font0, text_color="#0c7399")
        self.paquetsR = customtkinter.CTkLabel(master=self, text="Paquets recus", font=font0, text_color="#0c7399")
        self.capa = customtkinter.CTkLabel(master=self, text="Capacité", font=font0, text_color="#0c7399")
        self.pertes = customtkinter.CTkLabel(master=self, text="Pertes",font=font0, text_color="#0c7399")

        # buffers
        self.source = customtkinter.CTkLabel(master=self, text="Source", font=font0, text_color="#0c7399")
        self.transit1 = customtkinter.CTkLabel(master=self, text="Transit 1", font=font0, text_color="#0c7399")
        self.transit2 = customtkinter.CTkLabel(master=self, text="Transit 2", font=font0, text_color="#0c7399")
        self.transit3 = customtkinter.CTkLabel(master=self, text="Transit 3", font=font0, text_color="#0c7399")
        self.buffer_attente = customtkinter.CTkLabel(master=self, text="File d'attente", font=font0, text_color="#0c7399")
        self.dest = customtkinter.CTkLabel(master=self, text="Destination", font=font0, text_color="#0c7399")

        # entrys
        self.source_lambda = customtkinter.CTkEntry(master=self, placeholder_text="Source λ", font=font0)
        self.buffer_attente_lambda = customtkinter.CTkEntry(master=self, placeholder_text="Transit principal λ", font=font0)

        # totaux
        self.totaux = customtkinter.CTkLabel(master=self, text="Totaux", font=font0, text_color="#bf156d")
        self.temps_moyen = customtkinter.CTkLabel(master=self, text="Temps moyen", font=font0)

        # boutons
        self.start = customtkinter.CTkButton(master=self, text="Start", font=font0, command=self.start_sim)
        self.restart = customtkinter.CTkButton(master=self, text="Restart", font=font0, command=self.restart_func)
        self.remplir = customtkinter.CTkButton(master=self, text="Fill", font=font0, command=self.fillin)

        # capacités
        self.capa_source = customtkinter.CTkLabel(master=self, text=source.capacite, font=font0)
        self.capa_transit1 = customtkinter.CTkLabel(master=self, text=t1.capacite, font=font0)
        self.capa_transit2 = customtkinter.CTkLabel(master=self, text=t2.capacite, font=font0)
        self.capa_transit3 = customtkinter.CTkLabel(master=self, text=t3.capacite, font=font0)
        self.capa_dest = customtkinter.CTkLabel(master=self, text=dest.capacite, font=font0)
        self.capa_file = customtkinter.CTkLabel(master=self, text=file_attente.capacite, font=font0)
        self.capa_tot = customtkinter.CTkLabel(master=self, text=self.capaciteT, font=font0, text_color="#bf156d")

        # pertes
        self.pertes_source = customtkinter.CTkLabel(master=self, text=source.pertes, font=font0)
        self.pertes_transit1 = customtkinter.CTkLabel(master=self, text=t1.pertes, font=font0)
        self.pertes_transit2 = customtkinter.CTkLabel(master=self, text=t2.pertes, font=font0)
        self.pertes_transit3 = customtkinter.CTkLabel(master=self, text=t3.pertes, font=font0)
        self.pertes_file = customtkinter.CTkLabel(master=self,text=file_attente.pertes, font=font0)
        self.pertes_dest = customtkinter.CTkLabel(master=self, text=dest.pertes, font=font0)
        self.pertes_tot = customtkinter.CTkLabel(master=self, text=self.pertesT, font=font0, text_color="#bf156d")

        # fichiers transmis
        self.trans_source = customtkinter.CTkLabel(master=self, text=source.trans, font=font0)
        self.trans_transit1 = customtkinter.CTkLabel(master=self, text=t1.trans, font=font0)
        self.trans_transit2 = customtkinter.CTkLabel(master=self, text=t2.trans, font=font0)
        self.trans_transit3 = customtkinter.CTkLabel(master=self, text=t3.trans, font=font0)
        self.trans_file = customtkinter.CTkLabel(master=self,text=file_attente.trans, font=font0)
        self.trans_dest = customtkinter.CTkLabel(master=self, text=dest.trans, font=font0)
        self.trans_tot = customtkinter.CTkLabel(master=self, text=self.transT, font=font0, text_color="#bf156d")

        # fichiers recus
        self.rec_source = customtkinter.CTkLabel(master=self, text=source.rec, font=font0)
        self.rec_transit1 = customtkinter.CTkLabel(master=self, text=t1.rec, font=font0)
        self.rec_transit2 = customtkinter.CTkLabel(master=self, text=t2.rec, font=font0)
        self.rec_transit3 = customtkinter.CTkLabel(master=self, text=t3.rec, font=font0)
        self.rec_file = customtkinter.CTkLabel(master=self,text=file_attente.rec, font=font0)
        self.rec_dest = customtkinter.CTkLabel(master=self, text=dest.rec, font=font0)
        self.rec_tot = customtkinter.CTkLabel(master=self, text=self.recT, font=font0, text_color="#bf156d")

        # menus
        self.strategy = customtkinter.CTkOptionMenu(master=self, values=["Max capacités", "Tour de rôle", "Random", "Simple"])

        ######################################################################
        # widget packing
        # titres
        self.titreBuffer.grid(row=0, column=0, padx=10, pady=2)
        self.paquetsT.grid(row=0, column=1, padx=10, pady=2)
        self.paquetsR.grid(row=0, column=2, padx=10, pady=2)
        self.capa.grid(row=0, column=3, padx=10, pady=2)
        self.pertes.grid(row=0, column=4, padx=10, pady=2)

        # buffers
        self.source.grid(row=1, column=0, padx=10, pady=2)
        self.transit1.grid(row=2, column=0, padx=10, pady=2)
        self.transit2.grid(row=3, column=0, padx=10, pady=2)
        self.transit3.grid(row=4, column=0, padx=10, pady=2)
        self.buffer_attente.grid(row=5, column=0, padx=10, pady=2)
        self.dest.grid(row=6, column=0, padx=10, pady=2)

        # entrys
        self.source_lambda.grid(row=2, column=5, padx=5, pady=2)
        self.buffer_attente_lambda.grid(row=3, column=5, padx=5, pady=2)

        # totaux:
        self.totaux.grid(row=7, column=0, padx=10, pady=2)
        self.temps_moyen.grid(row=4, column=5, padx=10, pady=2)
        # fichiers transmis
        self.trans_source.grid(row=1, column=1, padx=10, pady=2)
        self.trans_transit1.grid(row=2, column=1, padx=10, pady=2)
        self.trans_transit2.grid(row=3, column=1, padx=10, pady=2)
        self.trans_transit3.grid(row=4, column=1, padx=10, pady=2)
        self.trans_file.grid(row=5, column=1, padx=10, pady=2)
        self.trans_dest.grid(row=6, column=1, padx=10, pady=2)
        self.trans_tot.grid(row=7, column=1, padx=10, pady=2)

        # fichiers recus
        self.rec_source.grid(row=1, column=2, padx=10, pady=2)
        self.rec_transit1.grid(row=2, column=2, padx=10, pady=2)
        self.rec_transit2.grid(row=3, column=2, padx=10, pady=2)
        self.rec_transit3.grid(row=4, column=2, padx=10, pady=2)
        self.rec_file.grid(row=5, column=2, padx=10, pady=2)
        self.rec_dest.grid(row=6, column=2, padx=10, pady=2)
        self.rec_tot.grid(row=7, column=2, padx=10, pady=2)

        # capacité
        self.capa_source.grid(row=1, column=3, padx=10, pady=2)
        self.capa_transit1.grid(row=2, column=3, padx=10, pady=2)
        self.capa_transit2.grid(row=3, column=3, padx=10, pady=2)
        self.capa_transit3.grid(row=4, column=3, padx=10, pady=2)
        self.capa_file.grid(row=5, column=3, padx=10, pady=2)
        self.capa_dest.grid(row=6, column=3, padx=10, pady=2)
        self.capa_tot.grid(row=7, column=3, padx=10, pady=2)

        # pertes
        self.pertes_source.grid(row=1, column=4, padx=10, pady=2)
        self.pertes_transit1.grid(row=2, column=4, padx=10, pady=2)
        self.pertes_transit2.grid(row=3, column=4, padx=10, pady=2)
        self.pertes_transit3.grid(row=4, column=4, padx=10, pady=2)
        self.pertes_file.grid(row=5, column=4, padx=10, pady=2)
        self.pertes_dest.grid(row=6, column=4, padx=10, pady=2)
        self.pertes_tot.grid(row=7, column=4, padx=10, pady=2)

        # boutons
        self.start.grid(row=0, column=5, padx=5, pady=2)
        self.restart.grid(row=0, column=6, padx=5, pady=2)
        self.remplir.grid(row=0, column=7, padx=5, pady=2)

        # menus
        self.strategy.grid(row=1, column=5, padx=5, pady=2)

    def start_sim(self):
        """
        Cette fonction commence la simulation
        """
        self.flag = True
        if self.flag:
            if self.strategy.get() == "Max capacités":
                self.maxcapa()
            elif self.strategy.get() == "Tour de rôle":
                self.tour_de_role()
            elif self.strategy.get() == "Random":
                self.rd()
            elif self.strategy.get() == "Simple":
                self.simple()
        else:
            source.capacite, source.pertes, source.trans, source.rec = 10000, 0, 0, 0
            dest.capacite, dest.pertes, dest.trans, dest.rec = 1000, 0, 0, 0
            t1.capacite, t1.pertes, t1.trans, t1.rec = 100, 0, 0, 0
            t2.capacite, t2.pertes, t2.trans, t2.rec = 100, 0, 0, 0
            t3.capacite, t3.pertes, t3.trans, t3.rec = 100, 0, 0, 0
            file_attente.capacite, file_attente.pertes, file_attente.trans, file_attente.rec = 1250, 0, 0, 0
            self.config()

    def restart_func(self):
        "rénitialise la simulation"
        self.flag = False
        source.capacite, source.pertes, source.trans, source.rec = 10000, 0, 0, 0
        dest.capacite, dest.pertes, dest.trans, dest.rec = 1000, 0, 0, 0
        t1.capacite, t1.pertes, t1.trans, t1.rec = 100, 0, 0, 0
        t2.capacite, t2.pertes, t2.trans, t2.rec = 100, 0, 0, 0
        t3.capacite, t3.pertes, t3.trans, t3.rec = 100, 0, 0, 0
        file_attente.capacite, file_attente.pertes, file_attente.trans, file_attente.rec = 1250, 0, 0, 0
        self.temps = [0]
        self.config()

    def fillin(self):
        """
        remplis les 3 files d'attentes Bi
        Cette fonction peut être utilisée avant de lancer la simulation afin de pouvoir
        commencer directement la avec des files d'attentes pré-remplies
        """
        self.flag = True
        if self.flag:
            if t1.capacite > 0 and t2.capacite > 0 and t3.capacite > 0:
                self.fill(1, t1)
                self.fill(1, t2)
                self.fill(1, t3)
                self.config()
                self.after(10, self.fillin)

    def config(self):
        """
        Actualise l'affichage des labels
        """
        self.capa_source.configure(text=source.capacite)
        self.trans_source.configure(text=source.trans)
        self.rec_source.configure(text=source.rec)
        # transit1
        self.capa_transit1.configure(text=t1.capacite)
        self.pertes_transit1.configure(text=t1.pertes)
        self.trans_transit1.configure(text=t1.trans)
        self.rec_transit1.configure(text=t1.rec)
        # transit2
        self.capa_transit2.configure(text=t2.capacite)
        self.pertes_transit2.configure(text=t2.pertes)
        self.trans_transit2.configure(text=t2.trans)
        self.rec_transit2.configure(text=t2.rec)
        # transit3
        self.capa_transit3.configure(text=t3.capacite)
        self.pertes_transit3.configure(text=t3.pertes)
        self.trans_transit3.configure(text=t3.trans)
        self.rec_transit3.configure(text=t3.rec)

        # file d'attente principale
        self.capa_file.configure(text=file_attente.capacite)
        self.pertes_file.configure(text=file_attente.pertes)
        self.trans_file.configure(text=file_attente.trans)
        self.rec_file.configure(text=file_attente.rec)

        self.capa_dest.configure(text=dest.capacite)
        self.capaciteT = source.capacite + t1.capacite + t2.capacite + file_attente.capacite + t3.capacite + dest.capacite
        self.pertesT = source.pertes + t1.pertes + t2.pertes + t3.pertes + file_attente.pertes + dest.pertes
        self.transT = source.trans + t1.trans + t2.trans + t3.trans + file_attente.trans + dest.trans
        self.recT = source.rec + t1.rec + t2.rec + t3.rec + file_attente.rec+  dest.rec
        self.pertes_source.configure(text=source.pertes)

        self.pertes_dest.configure(text=dest.pertes)
        self.pertes_tot.configure(text=self.pertesT)
        self.rec_tot.configure(text=self.recT)
        self.trans_tot.configure(text=self.transT)
        self.capa_tot.configure(text=self.capaciteT)

        self.temps_moyen.configure(text="{:.3f} s".format(sum(self.temps) / len(self.temps)))

    def maxcapa(self):
        """
        La file d’attente choisie est celle contenant le plus grand nombre de paquets
        """
        buffers = {
            t1: t1.capacite,
            t2: t2.capacite,
            t3: t3.capacite
        }
        min_key = min(buffers, key=buffers.get)
        if self.flag:
            if dest.capacite > 0:
                # Remplit la source, envoie des paquets à la file d'attente choisie et de la file d'attente à la destination
                self.fill(float(self.source_lambda.get())/100, source)
                self.send(5, min_key, file_attente)
                self.send(float(self.buffer_attente_lambda.get())/100, file_attente, dest)
                self.config()
                self.after(10, self.maxcapa)

    def tour_de_role(self):
        """
        Un paquet est pris de chaque file d’attente, à tour de rôle.
        """
        buffers = {
            t1: t1.capacite,
            t2: t2.capacite,
            t3: t3.capacite
        }
        if self.flag:
            if dest.capacite > 0:
                # Remplit la source, envoie un paquet de chaque file d'attente et de la file d'attente à la destination
                self.fill(float(self.source_lambda.get())/100, source)
                for key in buffers.keys():
                    self.send(2.5, key, file_attente)
                self.send(float(self.buffer_attente_lambda.get())/100, file_attente, dest)
                self.config()
                self.after(10, self.tour_de_role)

    def rd(self):
        """
        La file d’attente est choisie de manière aléatoire
        """
        buffers = [t1, t2, t3]
        if self.flag:
            if dest.capacite > 0:
                # Remplit la source, choisit une file d'attente aléatoire et envoie de cette file d'attente à la destination
                self.fill(float(self.source_lambda.get())/100, source)
                self.send(5, random.choice(buffers), file_attente)
                self.send(float(self.buffer_attente_lambda.get())/100, file_attente, dest)
                self.config()
                self.after(10, self.rd)

    def simple(self):
        if self.flag:
            if dest.capacite > 0:
                # Remplit la source, envoie un paquet de la source à t1, puis de t1 à la destination
                self.fill(float(self.source_lambda.get())/100, source)
                self.send(5, source, t1)
                self.send(2.5, t1, dest)
                self.config()
                self.after(10, self.simple)

    def fill(self, lamb, buffer):
        # Remplit un buffer avec un nombre d'arrivées poissonnien
        num_arrivals = self.poisson_arrivals(lamb)
        for _ in range(num_arrivals):
            buffer.arrivee_paquet(Paquet().get_paquet())
        buffer.rec += num_arrivals

    def send(self, lamb, buffer_source, buffer_dest):
        # Envoie un certain nombre de paquets d'un buffer source à un buffer destination avec des intervalles de temps poissonniens
        num_transmissions = self.poisson_arrivals(lamb)
        current_timee = time()
        for _ in range(num_transmissions):
            buffer_source.transmission_paquet(buffer_source.buffer[0], buffer_dest)
            temps_attente_paquet = Paquet().paquet_temps_arrivee - current_timee
            self.temps.append(temps_attente_paquet)
        buffer_source.trans += num_transmissions
        buffer_dest.rec += num_transmissions

    def poisson_arrivals(self, lamb):
        # Génère le nombre d'arrivées selon une distribution de Poisson avec le taux lambda
        # Utilise l'approche de la méthode de l'inversion de la fonction de répartition inverse
        L = math.exp(-lamb)
        k = 0
        p = 1
        while p > L:
            k += 1
            p *= random.uniform(0, 1)
        return k

    def poisson_delay(self):
        # Génère un délai selon une distribution de Poisson avec lambda = 1
        # Cela simule le temps entre les événements (arrivées de paquets)
        return self.poisson_arrivals(1) * 1000 // self.vitesse


if __name__ == '__main__':

    source, dest = Buffer(10000), Buffer(1000)
    t1, t2, t3 = Buffer(100), Buffer(100), Buffer(100)
    file_attente = Buffer(1250)

    app = App()
    app.mainloop()