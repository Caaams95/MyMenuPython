import os
import random
import subprocess

import pyautogui as pg
import time
import tkinter as tk
from tkinter import simpledialog

def menu():
    # Créer les boutons avec des tailles fixes
    spam_bouton = tk.Button(fenetre, text="Spam", command=spam, width=15, height=1, bg="#CCD1D1", )
    random_bouton = tk.Button(fenetre, text="Random", command=rand, width=15, height=1, bg="#CCD1D1")
    popup_bouton = tk.Button(fenetre, text="Pop up infinite", command=popup, width=15, height=1, bg="#CCD1D1")
    exit_bouton = tk.Button(fenetre, text="Exit", command=exit, width=15, height=1, bg="#E6B0AA")

    # Afficher les boutons dans la fenêtre
    spam_bouton.pack(pady=1) #pady = espace autour du bouton
    random_bouton.pack(pady=1)
    popup_bouton.pack(pady=1)
    exit_bouton.pack(pady=1)

def remove_all_widgets():
    """Remove all widgets from the main window"""
    for widget in fenetre.winfo_children():
        widget.destroy()

def showMenu():
    remove_all_widgets()
    menu()
    fenetre.title("SpamMessage")

def clearAndReturnButton():
    remove_all_widgets()
    bouton_remove = tk.Button(fenetre, text="Retour", command=showMenu)
    bouton_remove.pack(side=tk.BOTTOM)

def spam():
    clearAndReturnButton()
    fenetre.title("SpamMessage - Spam")

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


def rand():
    clearAndReturnButton()
    fenetre.title("SpamMessage - Random")

    global entry_message
    global label_message
    global bouton_launch

    # Afficher l'Entry pour le message
    label_message = tk.Label(fenetre, text="Entrez une liste de mots séparés par des espaces : ")
    label_message.pack(side=tk.TOP)
    entry_message = tk.Entry(fenetre)
    entry_message.pack(side=tk.TOP)

    # Afficher le bouton pour lancer le spam
    bouton_launch = tk.Button(fenetre, text="Lancer le spam", command=launch_random)
    bouton_launch.pack(side=tk.TOP)

def popup():
    global entry_message
    global label_message
    global bouton_launch

    clearAndReturnButton()
    fenetre.title("SpamMessage - Popup")

    # Afficher l'Entry pour le message
    label_message = tk.Label(fenetre, text="Entrez le message à spammer : ")
    label_message.pack(side=tk.TOP)
    entry_message = tk.Entry(fenetre)
    entry_message.pack(side=tk.TOP)

    # Afficher le bouton pour lancer le spam
    bouton_launch = tk.Button(fenetre, text="Lancer la popup", command=launch_popup)
    bouton_launch.pack(side=tk.TOP)



def launch_popup():
    message = entry_message.get()
    with open("popup.vbs", "w") as f:
        f.write("do\n")
        f.write("msgbox \"" + message + "\"\n")
        f.write("loop")

    #permet de l'ouvrir en asynchrone
    subprocess.Popen("popup.vbs", shell=True)


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

    # showMenuButton()
    lastWindow()
    for i in range(num_repeats):
        pg.write(message)
        pg.press('enter')



def launch_random():
    message = entry_message.get()

    # Fermer les Entries et Labels et lancer le spam
    entry_message.pack_forget()
    label_message.pack_forget()
    bouton_launch.pack_forget()

    if message:
        text = message.split()
        lastWindow()
        for i in range (10):
            a = random.choice(text)
            pg.write("Coucou " + a)
            pg.press('enter')
    else:
        tk.messagebox.showwarning("Attention", "Vous n'avez rien entré.")

def lastWindow():
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('tab')    
    pg.keyUp('alt')    

def exit():
    fenetre.destroy()



# START =========================================

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("SpamMessage")
fenetre.geometry("300x200")  # Définir la taille de la fenêtre

# fenetre.resizable(False, False)

showMenu()

# Démarrer la boucle principale de la fenêtre
fenetre.mainloop()
