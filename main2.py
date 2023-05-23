import tkinter as tk
import pyautogui as pg

color_neutre = "#CCD1D1"

# Définition des fonctions des boutons
def rand():
    print("rand")
    
def popup():
    print("popup")
    
def spam():
    print("spam")    
    
def launch_cmd():
    print("launch_cmd")
    
def menu():
    # Définition des boutons et de leurs commandes associées
    buttons = [
        ("Dorks", dorks, color_neutre),
        ("Spam", spam, color_neutre),
        ("Random", rand, color_neutre),
        ("Illimited Pop up", popup, color_neutre),
        ("Illimited CMD", launch_cmd, color_neutre),
        ("Exit", exit, "#F7967A")
    ]

    # Création des boutons dans la fenêtre principale
    for text, command, color in buttons:
        button = tk.Button(fenetre, text=text, command=command, width=15, height=1, bg=color)
        button.pack(pady=1)


def showMenu():
    # Suppression de tous les widgets de la fenêtre principale
    remove_all_widgets()
    
    # Affichage du menu principal
    menu()
    
    # Définition du titre de la fenêtre
    fenetre.title("Menu")


def remove_all_widgets():
    """Supprime tous les widgets de la fenêtre principale"""
    for widget in fenetre.winfo_children():
        widget.destroy()


def clearAndReturnButton():
    # Suppression de tous les widgets de la fenêtre principale
    remove_all_widgets()
    
    # Création du bouton "Retour"
    bouton_remove = tk.Button(fenetre, text="Retour", command=showMenu)
    bouton_remove.pack(side=tk.BOTTOM)

    
def exit():
    fenetre.destroy()
    
def dorks():
    print("go dorks")

    # Suppression de tous les widgets de la fenêtre principale
    clearAndReturnButton()
    
    # Définition du titre de la fenêtre
    fenetre.title("Menu - Dorks")

    # Définition des entrées de texte : entry_name, label_text
    entries = [
        ("allintext", "allintext : "),
        ("intext", "intext : "),
        ("inurl", "inurl : "),
        ("allinurl", "allinurl : "),
        ("intitle", "intitle : "),
        ("allintitle", "allintitle : "),
        ("site", "site : "),
        ("filetype", "filetype : "),
        ("link", "link : "),
        ("numrange", "numrange : "),
        ("before", "before : "),
        ("after", "after : "),
        ("allinanchor", "allinanchor : "),
        ("allinpostauthor", "allinpostauthor : "),
        ("related", "related : "),
        ("cache", "cache : ")
    ]

    global entries_dict

    entries_dict = {}

    # Création des étiquettes et des champs de saisie
    for entry_name, label_text in entries:
        label = tk.Label(fenetre, text=label_text)
        label.pack(side=tk.TOP)
        entry = tk.Entry(fenetre)
        entry.pack(side=tk.TOP)
        entries_dict[entry_name] = entry

    # Création du bouton de lancement des "Dorks"
    button_launch = tk.Button(fenetre, text="Lancer le Dorks", command=launch_dorks)
    button_launch.pack(side=tk.TOP)
    
    
def launch_dorks():
    print("go launch_dorks")

    url = "https://www.google.com/search?q="

    # Paramètres de requête pour chaque type de "Dork"
    query_params = {
        "allintext": "allintext%3A%22",
        "intext": "intext%3A%22",
        "inurl": "inurl%3A%22",
        "allinurl": "allinurl%3A%22",
        "intitle": "intitle%3A%22",
        "allintitle": "allintitle%3A%22",
        "site": "site%3A%22",
        "filetype": "filetype%3A%22",
        "link": "link%3A%22",
        "numrange": "numrange%3A%22",
        "before": "before%3A%22",
        "after": "after%3A%22",
        "allinanchor": "allinanchor%3A%22",
        "allinpostauthor": "allinpostauthor%3A%22",
        "related": "related%3A%22",
        "cache": "cache%3A%22"
    }

    # Construction de l'URL de recherche en utilisant les valeurs saisies
    for entry_name, entry in entries_dict.items():
        value = entry.get()
        if value:
            param = query_params.get(entry_name, "")
            url += f"{param}{value}%22+"

    if url.endswith("+"):
        url = url[:-1]

    print(url)
    
    
def spam():
    clearAndReturnButton()
    fenetre.title("Menu - Spam")

    entries = [
        ("message", "Entrez le message à spammer : "),
        ("repetition", "Entrez le nombre de répétitions : ")
    ]

    global entries_dict
    entries_dict = {}

    for entry_name, label_text in entries:
        label = tk.Label(fenetre, text=label_text)
        label.pack(side=tk.TOP)
        entry = tk.Entry(fenetre)
        entry.pack(side=tk.TOP)
        entries_dict[entry_name] = entry

    button_launch = tk.Button(fenetre, text="Lancer le spam", command=launch_spam)
    button_launch.pack(side=tk.TOP)


def launch_spam():
    message = entries_dict["message"].get()
    num_repeats = int(entries_dict["repetition"].get())

    for entry in entries_dict.values():
        entry.pack_forget()

    lastWindow()
    for _ in range(num_repeats):
        pg.write(message)
        pg.press('enter') 
        
def lastWindow():
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('tab')    
    pg.keyUp('alt')    

def exit():
    fenetre.destroy() 
    
    
    
    
    
    
    
    
    
    



# Début du programme principal

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Menu")
fenetre.geometry("500x800")  # Définir la taille de la fenêtre

# Affichage du menu principal
showMenu()

# Démarrer la boucle principale de la fenêtre
fenetre.mainloop()
