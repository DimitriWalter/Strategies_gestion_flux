import flet
from flet import ElevatedButton, Icon, IconButton, Page, Row, Slider, Text, TextField, UserControl, icons, Container, alignment
import random
import threading
import time
import numpy as np


thread = None
lambda_value_shared = 1
lancement = True
perte = 0




# Classe Source
class Source:
    def __init__(self, id):
        self.id = id


# Classe Paquet
class Paquet:
    def __init__(self, source, taille):
        self.source = source
        self.taille = taille

    def paquet_suivant(self,paquet):
        return paquet


    

# Classe Buffer
class Buffer:
    def __init__(self, capacite):
        self.capacite = capacite
        self.file = []

    def arrivee(self, paquet):
        global perte
        if len(self.file) < self.capacite:
            self.file.append(paquet)
        else:
            print(f"Paquet de la source {paquet.source.id}, de taille {paquet.taille} rejeté (buffer plein)")
            perte +=1

    def transmission(self):
        if self.file:
            return self.file.pop(0)
        else:
            return None
        





# Interface graphique avec Flet et visualisation du buffer
def main(page: Page):
    page.title = "Réseau de communication"
    page.vertical_alignment = "center"
    
    # Paramètres
    global lancement
    global perte
    lambda_value = 1
    buffer_capacite = 13
    buffer = Buffer(buffer_capacite)
    sources = [Source(i+1) for i in range(5)]
    taux_transmission_lien = 10
    global thread


    # Éléments de l'interface
    text_lambda = Text(f"Taux d'arrivée (λ) : {lambda_value}")
    slider_lambda = Slider(min=0.1, max=5, value=lambda_value, on_change=lambda e: update_lambda(e.control.value))
    text_buffer = Text(f"Buffer (capacité {buffer_capacite})")
    buffer_container = Container(
        content=Row([
            Container(bgcolor="red",padding = 5,border_radius=5,
                      content = Text(str(p.taille),size = 15),data = p)
            for p in buffer.file
        ], spacing=5),
        width=440,
        height = 60,
        bgcolor = "black",
        border_radius=5,
        padding=5,
        alignment = alignment.center
    )
    

    def update_text():
        buffer_container.content.controls = [
                Container(bgcolor = "red", padding=5, border_radius= 5,
                     content = Text(str(p.taille),size = 16),data = p)
                for p in buffer.file
        ]
        
        buffer_container.content.spacing = 5
        buffer_container.update()
        page.update()


    def arrivee_handler(e):
        source = random.choice(sources)
        paquet = Paquet(source, random.randint(1,50))
        if paquet.taille <= taux_transmission_lien :
                print(f"Paquet de la source {source.id}, de taille {paquet.taille} transmis")
        else:
            buffer.arrivee(paquet)
            update_text()

    def transmission_handler(e):
        global perte
        paquet = buffer.transmission()
        if paquet != None:
            print(f"Paquet de la source {paquet.source.id}, de taille {paquet.taille} transmis")
            update_text()
        else:
            print("Buffer vide")


    def transmission_handler2(e):
        paquet = buffer.transmission()
        time.sleep(1)
        if paquet:
            print(f"Paquet de la source {paquet.source.id}, de taille {paquet.taille} transmis")
            update_text()
        else:
            print("Buffer vide")

    

    def update_lambda(new_lambda):
        global lambda_value_shared, thread
        lambda_value_shared = new_lambda
        text_lambda.value = f"Taux d'arrivée (λ) : {lambda_value_shared}"
        if thread is not None:
            thread.join()
        thread = threading.Thread(target=arrivee_thread)
        thread.start()
        page.update()

    # Thread pour simuler l'arrivée périodique des paquets selon une loi de Poisson
    def arrivee_thread():
        global lambda_value_shared, lancement
        while lancement == True:
            # Générer un temps d'attente selon une loi exponentielle de paramètre lambda
            temps_attente = np.random.poisson(lambda_value_shared)
            time.sleep(temps_attente)
            arrivee_handler(None)

    
    def stop(e):
        global lancement
        lancement = False
        time.sleep(2)
        print(f"Le nombre de paquets perdus est de {perte}.")


    def arrivee_thread2():
        global lambda_value_shared, lancement, perte
        while lancement == True:
            time.sleep(1)
            transmission_handler2(None)

    thread1 = threading.Thread(target=arrivee_thread)
    thread2 = threading.Thread(target= arrivee_thread2)

    thread1.start()
    thread2.start()

    

    page.add(
        Row(
            [
                text_lambda,
                slider_lambda,
                ElevatedButton("Arrivée", on_click=arrivee_handler),
                ElevatedButton("Transmission", on_click=transmission_handler),
                ElevatedButton("STOP", on_click = stop),
                text_buffer,
                buffer_container
            ],
            alignment="center",
        )
    )

flet.app(target=main)