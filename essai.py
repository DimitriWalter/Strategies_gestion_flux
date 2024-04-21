import tkinter as tk
import time
import random as rd

class Source(object):
    id = 0  
    def __init__(self, lambd, time):
        Source.id += 1  
        self.id = Source.id  
        self.paquets = list()  
        self.taux_arrive = lambd
        self.time = time

    def generer_paquet(self):  
        paquets = list()
        for _ in range(5):
            contenu = list()
            for i in range(rd.randint(2, 9)):
                contenu.append("")
                for _ in range(5):
                    contenu[i] += str(rd.randint(0, 1))

            paquets.append(Paquet(self.id, contenu, self.taux_arrive))

        return paquets
    
    def arrive(self, paquet, buffer):  
        if paquet.taux_arrive > Buffer.taux_lien:
            t = rd.uniform(0, self.time/self.taux_arrive)
            time.sleep(t)
            buffer + paquet
        else:
            buffer.paquets_transmis.append(paquet)

class Buffer(object):
    id = 0  
    taux_lien = 0.4  
    def __init__(self, capacite):
        Buffer.id += 1
        self.id = Buffer.id
        self.capacite = capacite  
        self.queue = list()  
        self.paquets_perdus = list()  
        self.paquets_transmis = list()  

    def __add__(self, paquet):  
        if len(self.queue) < self.capacite:
            self.queue.append(paquet)
            app.buffer_text.insert(tk.END, f"Paquet {paquet.id} arrivé dans le buffer\n")
            app.buffer_text.see(tk.END)
        else:
            self.paquets_perdus.append(paquet)
            app.buffer_text.insert(tk.END, f"Paquet {paquet.id} est perdu\n")
        app.buffer_text.see(tk.END)

    def retrait(self):  
        if self.queue:
            paquet = self.queue.pop(0)
            app.buffer_text.insert(tk.END, f"Paquet {paquet.id} est sorti du buffer\n")
            time.sleep(1)
            self.paquets_transmis.append(paquet)
            app.buffer_text.insert(tk.END, f"Paquet {paquet.id} est transmis sur le lien\n")
            time.sleep(1)
        app.buffer_text.see(tk.END)


class Paquet(object):
    id = 0  
    def __init__(self, source_id, contenu, taux):
        Paquet.id += 1
        self.id = Paquet.id
        self.source_id = source_id  
        self.contenu = contenu  
        self.taille = len(contenu)
        self.taux_arrive = taux

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de flux")
        self.geometry("1000x700")
        self.geometry("+380+160")

        self.source = Source(1, 0.5)
        self.buffer = Buffer(47)

        self.buffer_label = tk.Label(self, text="Buffer", font="bold")
        self.buffer_label.grid(row=0, column=0)

        self.buffer_text = tk.Text(self, height=38, width=50)
        self.buffer_text.grid(row=1, column=0)
        
        self.lien_text = tk.Text(self, height=38, width=50)
        self.lien_text.grid(row=1, column=1)

        self.arrival_button = tk.Button(self, text="Arrivée Paquet", command=self.arrive_paquet)
        self.arrival_button.grid(columnspan=2)

        self.retrait_button = tk.Button(self, text="Retrait Paquet", command=self.buffer.retrait)
        self.retrait_button.grid()

    def arrive_paquet(self):
        paquets = self.source.generer_paquet()
        for paquet in paquets:
            self.source.arrive(paquet, self.buffer)

app = App()
app.mainloop()