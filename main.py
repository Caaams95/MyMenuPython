import random
import pyautogui as pg
import time
import tkinter as tk
from tkinter import simpledialog


def spam():
    global entry_message
    global entry_repeats
    global label_message
    global label_repeats
    global bouton_launch

    # Afficher l'Entry pour le message
    label_message = tk.Label(fenetre, text="Entrez le message à spammer : ")
    label_message.pack(side=tk.TOP)
    entry_message = tk.Entry(fenetre)
    entry_message.pack(side=tk.TOP)

    # Afficher l'Entry pour le nombre de répétitions
    label_repeats = tk.Label(fenetre, text="Entrez le nombre de répétitions : ")
    label_repeats.pack(side=tk.TOP)
    entry_repeats = tk.Entry(fenetre)
    entry_repeats.pack(side=tk.TOP)

    # Afficher le bouton pour lancer le spam
    bouton_launch = tk.Button(fenetre, text="Lancer le spam", command=launch_spam)
    bouton_launch.pack(side=tk.TOP)

def launch_spam():
    # Récupérer les entrées utilisateur
    message = entry_message.get()
    num_repeats = int(entry_repeats.get())

    # Fermer les Entries et Labels et lancer le spam
    entry_message.pack_forget()
    entry_repeats.pack_forget()
    label_message.pack_forget()
    label_repeats.pack_forget()
    bouton_launch.pack_forget()

    lastWindow()
    for i in range(num_repeats):
        pg.write(message)
        pg.press('enter')


def rand():
    time.sleep(1)
    text=('Cams', 'Fnny')
    lastWindow()
    for i in range (10):
        a = random.choice(text)
        pg.write("Coucou " + a)
        pg.press('enter')


def lastWindow():
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('tab')    
    pg.keyUp('alt')    

def exit():
    fenetre.destroy()

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("SpamMessage")
fenetre.geometry("300x200")  # Définir la taille de la fenêtre
# fenetre.resizable(False, False)
 
# Créer les boutons avec des tailles fixes
bouton1 = tk.Button(fenetre, text="Spam", command=spam, width=15, height=1)
bouton2 = tk.Button(fenetre, text="random", command=rand, width=15, height=1)
bouton3 = tk.Button(fenetre, text="exit", command=exit, width=15, height=1)

# Afficher les boutons dans la fenêtre
bouton1.pack()
bouton2.pack()
bouton3.pack()

# Démarrer la boucle principale de la fenêtre
fenetre.mainloop()