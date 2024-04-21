#mail prof
#perla.hajjar@sqy.fr*


import customtkinter
import multiprocessing

from buffer import *
from paquet import *
from source import *


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de flux")
        self.capaciteT = source.capacite + t1.capacite + t2.capacite + t3.capacite + dest.capacite
        self.pertesT = source.pertes + t1.pertes + t2.pertes + t3.pertes + dest.pertes
        self.texte = 0
        self.vitesse = 500
        self.flag = True
        font0 = ('Helvetica', 20)

        #titres horizontaux
        self.titreBuffer = customtkinter.CTkLabel(master=self, text="Buffers", font=font0)
        self.paquetsT = customtkinter.CTkLabel(master=self, text="Paquets transmis", font=font0)
        self.paquetsR = customtkinter.CTkLabel(master=self, text="Paquets recus", font=font0)
        self.capa = customtkinter.CTkLabel(master=self, text="Capacité", font=font0)
        self.pertes = customtkinter.CTkLabel(master=self, text="Pertes",font=font0)

        #buffers
        self.source = customtkinter.CTkLabel(master=self, text="Source", font=font0)
        self.transit1 = customtkinter.CTkLabel(master=self, text="Transit 1", font=font0)
        self.transit2 = customtkinter.CTkLabel(master=self, text="Transit 2", font=font0)
        self.transit3 = customtkinter.CTkLabel(master=self, text="Transit 3", font=font0)
        self.dest = customtkinter.CTkLabel(master=self, text="Destination", font=font0)

        #totaux
        self.totaux = customtkinter.CTkLabel(master=self, text="Totaux", font=font0)

        #boutons
        self.start = customtkinter.CTkButton(master=self, text="Start", font=font0, command=self.start_sim)
        self.restart = customtkinter.CTkButton(master=self, text="Restart", font=font0, command=self.restart_func)

        #capacités
        self.capa_source = customtkinter.CTkLabel(master=self, text=source.capacite, font=font0)
        self.capa_transit1 = customtkinter.CTkLabel(master=self, text=t1.capacite, font=font0)
        self.capa_transit2 = customtkinter.CTkLabel(master=self, text=t2.capacite, font=font0)
        self.capa_transit3 = customtkinter.CTkLabel(master=self, text=t3.capacite, font=font0)
        self.capa_dest = customtkinter.CTkLabel(master=self, text=dest.capacite, font=font0)
        self.capa_tot = customtkinter.CTkLabel(master=self, text=self.capaciteT, font=font0)

        #pertes
        self.pertes_source = customtkinter.CTkLabel(master=self, text=0, font=font0)
        self.pertes_transit1 = customtkinter.CTkLabel(master=self, text=0, font=font0)
        self.pertes_transit2 = customtkinter.CTkLabel(master=self, text=0, font=font0)
        self.pertes_transit3 = customtkinter.CTkLabel(master=self, text=0, font=font0)
        self.pertes_dest = customtkinter.CTkLabel(master=self, text=0, font=font0)
        self.pertes_tot = customtkinter.CTkLabel(master=self, text=0, font=font0)

        #menus
        self.strategy = customtkinter.CTkOptionMenu(master=self, values=["Max capacités", "Tour de rôle", "Random"])

        ###############################################################################################
        #widget packing
        #titres
        self.titreBuffer.grid(row=0, column=0, padx=10, pady=2)
        self.paquetsT.grid(row=0, column=1, padx=10, pady=2)
        self.paquetsR.grid(row=0, column=2, padx=10, pady=2)
        self.capa.grid(row=0, column=3, padx=10, pady=2)
        self.pertes.grid(row=0, column=4, padx=10, pady=2)

        #buffers
        self.source.grid(row=1, column=0, padx=10, pady=2)
        self.transit1.grid(row=2, column=0, padx=10, pady=2)
        self.transit2.grid(row=3, column=0, padx=10, pady=2)
        self.transit3.grid(row=4, column=0, padx=10, pady=2)
        self.dest.grid(row=5, column=0, padx=10, pady=2)

        #totaux:
        self.totaux.grid(row=6, column=0, padx=10, pady=2)

        #capacité
        self.capa_source.grid(row=1, column=3, padx=10, pady=2)
        self.capa_transit1.grid(row=2, column=3, padx=10, pady=2)
        self.capa_transit2.grid(row=3, column=3, padx=10, pady=2)
        self.capa_transit3.grid(row=4, column=3, padx=10, pady=2)
        self.capa_dest.grid(row=5, column=3, padx=10, pady=2)
        self.capa_tot.grid(row=6, column=3, padx=10, pady=2)

        #pertes
        self.pertes_source.grid(row=1, column=4, padx=10, pady=2)
        self.pertes_transit1.grid(row=2, column=4, padx=10, pady=2)
        self.pertes_transit2.grid(row=3, column=4, padx=10, pady=2)
        self.pertes_transit3.grid(row=4, column=4, padx=10, pady=2)
        self.pertes_dest.grid(row=5, column=4, padx=10, pady=2)
        self.pertes_tot.grid(row=6, column=4, padx=10, pady=2)

        #boutons
        self.start.grid(row=0, column=5, padx=10, pady=2)
        self.restart.grid(row=0, column=6, padx=10, pady=2)

        #menus
        self.strategy.grid(row=1, column=5, padx=10, pady=2)
    
    def syst(self):
        if t1.pertes < 1000:
            t1.pertes += 1
            self.config(t1.pertes)
            self.after(1000//self.vitesse, self.syst)

    def start_sim(self):
        if self.flag:
            if self.strategy.get() == "Max capacités":
                self.maxcapa()
            elif self.strategy.get() == "Tour de rôle":
                self.tour_de_role()
            elif self.strategy.get() == "Random":
                self.rd()
                """if dest.capacite > 0:
                    self.fill(10, source)
                    self.send(5, source, t1)
                    self.send(1, t1, dest)
                    self.config()
                    self.after(1000//self.vitesse, self.start_sim)"""
        else:
            source.capacite, dest.capacite = 600, 600
            source.pertes, dest.pertes = 0, 0
            t1.capacite, t2.capacite, t3.capacite = 200, 200, 200
            t1.pertes, t2.pertes, t3.pertes = 0, 0, 0
            self.config()
            self.flag = True

    def restart_func(self):
        self.flag = False

              
    def config(self):
        self.capa_source.configure(text=source.capacite)
        #transit1
        self.capa_transit1.configure(text=t1.capacite)
        self.pertes_transit1.configure(text=t1.pertes)
        #transit2
        self.capa_transit2.configure(text=t2.capacite)
        self.pertes_transit2.configure(text=t2.pertes)
        #transit3
        self.capa_transit3.configure(text=t3.capacite)
        self.pertes_transit3.configure(text=t3.pertes)

        self.capa_dest.configure(text=dest.capacite)
        self.pertesT = source.pertes + t1.pertes + t2.pertes + t3.pertes + dest.pertes
        self.pertes_source.configure(text=source.pertes)
        
        self.pertes_dest.configure(text=dest.pertes)
        self.pertes_tot.configure(text=self.pertesT)

    def fill(self, lamb, buffer):
        for _ in range(lamb):
            buffer.arrivee_paquet(Paquet().get_paquet())

    def send(seelf, lamb, buffer_source, buffer_dest):
        for  i in range(lamb):
            buffer_source.transmission_paquet(buffer_source.buffer[i], buffer_dest)

    def maxcapa(self):
        buffers = {
            t1: t1.capacite,
            t2: t2.capacite,
            t3: t3.capacite
        }
        if dest.capacite > 0:
            self.fill(10, source)
            self.send(random.randint(5, 10), source, t1)
            self.send(random.randint(5, 10), source, t2)
            self.send(random.randint(5, 10), source, t3)
            min_key = min(buffers, key=buffers.get)
            self.send(random.randint(2, 5), min_key, dest)
            self.config()
            self.after(1000//self.vitesse, self.maxcapa)

    def tour_de_role(self):
        pass

    def rd(self):
        buffers = [t1, t2, t3]

if __name__ == '__main__':

    source, dest = Buffer(600), Buffer(600)
    t1, t2, t3 = Buffer(200), Buffer(200), Buffer(200)

    app = App()
    app.mainloop()

    
    
        

