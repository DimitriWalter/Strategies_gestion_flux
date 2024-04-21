import tkinter as tk
import time
import random as rd

class Source(object):
    id = 0  
    def __init__(self, lambd, time, app):
        Source.id += 1  
        self.id = Source.id  
        self.paquets = list()  
        self.taux_arrive = lambd
        self.time = time
        self.app = app

    def generer_paquet(self):  
        paquets = list()
        for _ in range(10):
            contenu = list()
            for i in range(rd.randint(2, 9)):
                contenu.append("")
                for _ in range(5):
                    contenu[i] += str(rd.randint(0, 1))

            paquets.append(Paquet(self.id, contenu, self.taux_arrive))

        return paquets
    
    def arrive(self, paquet, buffer, app):  
        if paquet.taux_arrive > Buffer.taux_lien:
            t = rd.uniform(0, self.time/self.taux_arrive)
            time.sleep(t)
            buffer.insert(paquet, app)
        else:
            buffer.paquets_transmis.append(paquet)

class Buffer(object):
    id = 0  
    taux_lien = 0.4  
    def __init__(self, capacite, app):
        Buffer.id += 1
        self.id = Buffer.id
        self.capacite = capacite  
        self.queue = list()  
        self.paquets_perdus = list()  
        self.paquets_transmis = list()
        self.app = app

    def insert(self, paquet):
        if len(self.queue) < self.capacite:
            self.queue.append(paquet)
        else:
            self.paquets_perdus.append(paquet)

    def retrait(self):  
        if self.queue:
            paquet = self.queue.pop(0)
            self.paquets_transmis.append(paquet)


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
        self.geometry("880x790")
        self.geometry("+380+160")
        self.configure(bg="#D5CCDC")

        self.source = Source(2, 1, self)
        self.buffer = Buffer(47, self)

        self.widgets()
        self.after(10, self.actualise)

    
    def widgets(self):

        self.buffer_label = tk.Label(self, text=f"Buffer", font=("Helvetica", 15, "bold"), fg="white", bg="blue", padx=45, pady=10)
        self.buffer_label.place(x=150, y=7)

        self.buffer_canvas = tk.Canvas(self,height=600, width=400, bg="white")
        self.buffer_canvas.place(x=20, y=60)
        
        self.lien_label = tk.Label(self, text="Lien", font=("Helvetica", 15, "bold"), fg="white", bg="green", padx=45, pady=10)
        self.lien_label.place(x=580,y=7)

        self.lien_canvas = tk.Canvas(self, height=600, width=400, bg="white")
        self.lien_canvas.place(x=450, y=60)

        self.paquets_perdus = tk.Label(self, text=f"Nombres de paquets perdus: {len(self.buffer.queue)}", font=("Helvetica", 13, "bold"), fg="white", bg="red", padx=45, pady=10)
        self.paquets_perdus.place(x=250, y=682)

        self.taux_perdus = tk.Label(self, text=f"Taux de paquets perdus: {len(self.buffer.queue)}", font=("Helvetica", 13, "bold"), fg="white", bg="red", padx=45, pady=10)
        self.taux_perdus.place(x=267, y=733)

    def actualise(self):
        pass
    
    def programme(self):
        paquets = self.source.generer_paquet()
        for paquet in paquets:
            self.source.arrive(paquet, self.buffer, self)




if __name__ == "__main__":
    app = App()
    app.mainloop()
