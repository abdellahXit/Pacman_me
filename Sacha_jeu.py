from tkinter import*
from Dessin import *
from Sacha_bouton import *

window = Tk()
canvas = Canvas(window, width=5, height=5, bg='white')
canvas.pack()

def page_dessin(*parametres):

    Big_data_couleur = 'nothing'
    dimensions = [10, 10]

    Liste_precision  =['vide', 'mur']
    Liste_couleur=['black', 'blue']

    initialistation_interface_dessin(canvas=canvas, dimensions=dimensions, taille_grille=40, Liste_couleur=Liste_couleur, Liste_precision=Liste_precision, fonction_fin=fonction_dessin_retour, Big_data_couleur=Big_data_couleur)

def fonction_dessin_retour(*parametres):

    Liste_terrain = variable_big_data(64, 'str')

    print(Liste_terrain)

def creation_terrain():
    global Big_data_objet

    canvas.config(width=300, height=300)

    ecart_bord = 0
    taille_case = 40
    Liste_dimension = [10, 10]
    Liste_terrain = [2, 64, 'fè', 'd9', '8f', '80', '80', '90', '90', '96', '96', 'fè']

    "rien"
    Liste_machin = ['rien', 0, 0, 0, 0]

    "mur normal"
    Liste_machin += ['rectangle', [0, 0, taille_case, taille_case], 'black', 'pink', 2]

    Big_data_figure, Big_data_objet = recreation_dessin(canvas, Liste_terrain, Liste_dimension[0], taille_case, ecart_bord, Liste_machin)

def jeu():

    creation_terrain()

    event_en_tout_genre(canvas)

    rajout_fonction('appuyer', Liste_touche[0], activation_deplacement, Liste_touche[1], activation_deplacement)
    rajout_fonction('relacher', Liste_touche[0], desactivation_deplacement, Liste_touche[1], desactivation_deplacement)

def activation_deplacement(x_souris, y_souris, touche_event, *parametres):
    global deplacement

    deplacement = (-1)**(1-Liste_touche.index(touche_event))
    deplacement_reference = deplacement

    vitesse = 5

    while deplacement == deplacement_reference:

        for objet in Big_data_objet:

            canvas.move(objet, vitesse*deplacement, 0)

        canvas.update()
        sleep(0.1)

def desactivation_deplacement(*parametres):
    global deplacement

    deplacement = 0

def deplacement


Liste_touche = ['d', 'q']
deplacement = 0

#page_dessin()
jeu()

window.mainloop()