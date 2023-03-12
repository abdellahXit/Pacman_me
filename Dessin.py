def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import*
from time import time, sleep
from Sacha_bouton import *

fin = 0

"-1 parce que aucun bouton n'a encore été selctionné"
bouton_selectionne = [-1]
corps_bouton_zone = 'inexistant banane'
Liste_couleur_boule = []
passe_zone = 0


def options_interface_dessin():

    return ['canvas', 0, 'taille_grille', 30, 'dimensions', [10, 10], "fonction_retour", avertissement, 'couleur_grille', 'white', 'ecart_bord', 15, 'Liste_couleur', ['black', 'green', 'red', 'black', 'brown', 'purple', 'pink', 'grey', 'blue', 'cyan', 'magenta', 'yellow'],  'Liste_obligation', 'nothing', 'Liste_precision', [], 'fonction_fin', 'rien', 'Big_data_couleur', 'nothing']

def initialistation_interface_dessin(**parametres):
    global canvas, tgrille, dimensions, fonction_retour, couleur_grille, couleur_canvas, ecart_bord, Big_data_couleur, Big_data_objet, Liste_couleur_boule, Liste_obligation, Liste_precision, fonction_fin

    Liste_options = attribution_variables(options_interface_dessin(), parametres)

    "definir toute les variables"
    canvas, tgrille, dimensions, fonction_retour, couleur_grille, ecart_bord, Liste_couleur_boule, Liste_obligation, Liste_precision, fonction_fin, Big_data_couleur = Liste_options[0], Liste_options[1], Liste_options[2], Liste_options[3], Liste_options[4], Liste_options[5], Liste_options[6], Liste_options[7], Liste_options[8], Liste_options[9], Liste_options[10]
    couleur_canvas = 'black'

    "s'il est donné une liste"
    if Big_data_couleur == 'nothing':
        Big_data_couleur = [[0]*dimensions[0]]*dimensions[1]

    else:

        for k in range(2, len(Big_data_couleur)):
            "transformer en la bonne base"
            Liste_couleur = transforamtion_base_nouvelle_base(Big_data_couleur[1], Big_data_couleur[0], Big_data_couleur[k])
            "changer de sens pour pouvoir rajouter des 0 à la fin"
            Liste_couleur.reverse()

            Big_data_couleur[k] = Liste_couleur.copy()

        "enlever les bases"
        Big_data_couleur = Big_data_couleur[2:].copy()

        "arranger la liste par rapport aux dimensions"
        arranger_liste()

        "rechanger de sens puisqu'on l'a fait avant"
        for k in range(len(Big_data_couleur)):

            Big_data_couleur[k].reverse()

    "obligation"
    if Liste_obligation != 'nothing':
        creation_obligation(Liste_obligation[0], Liste_obligation[1:])

    interface_dessin()

def interface_dessin(*parametres):
    global Big_data_objet

    Big_data_objet = [[0] * dimensions[0]] * dimensions[1]

    "longueur boule*6.5"
    place_boule = ((tgrille * dimensions[1])/15)*6.5
    place_bouton = 300

    effacer_bouton('all')
    canvas.delete('all')

    "dimension canvas"
    canvas.config(width=tgrille * dimensions[0] + 2 * ecart_bord + place_boule + place_bouton, height=tgrille * dimensions[1] + 2 * ecart_bord, bg=couleur_canvas)

    rajout_fonction('appuyer', '??', dessinage)

    "grille"
    creation_grille()

    "arranger liste"
    arranger_liste()

    "recréer cases colorées"
    option_changement()

    "boutons"
    creation_boutons(tgrille * dimensions[0] + 2 * ecart_bord, tgrille * dimensions[1], place_boule, place_bouton)

def creation_grille():
    global corps_grille

    corps_grille = []

    "barre verticale"
    for k in range(dimensions[0]+1):
        coord = ecart_bord + tgrille*k, ecart_bord, ecart_bord + tgrille*k, ecart_bord + tgrille*dimensions[1]
        corps_grille += [canvas.create_line(coord, fill=couleur_grille)]

    "barre horizontale"
    for k in range(dimensions[1]+1):
        coord = ecart_bord, ecart_bord + tgrille*k, ecart_bord + tgrille*dimensions[0], ecart_bord + tgrille*k
        corps_grille += [canvas.create_line(coord, fill=couleur_grille)]

def creation_obligation(positions, Liste_obligation):
    global Big_data_couleur, Big_data_objet

    position_x = positions[0]
    position_y = positions[1]

    for y in range(len(Liste_obligation)):

        obligation = Liste_obligation[y]

        for x in range(len(obligation)):

            Liste_couleur = Big_data_couleur[y + position_y].copy()

            Liste_couleur[x + position_x] = -obligation[x] - 1

            Big_data_couleur[y + position_y] = Liste_couleur.copy()

def arranger_liste():
    global Big_data_couleur

    "si option avant, arranger les Big_data par rapport aux dimensions"
    if len(Big_data_couleur) > dimensions[1]:
        Big_data_couleur = Big_data_couleur[:dimensions[1]]
    elif len(Big_data_couleur) < dimensions[1]:
        Big_data_couleur += [[0] * dimensions[0]] * (dimensions[1] - len(Big_data_couleur))

    if len(Big_data_couleur[0]) > dimensions[0]:
        for k in range(len(Big_data_couleur)):
            Liste_couleur = Big_data_couleur[k].copy()
            Liste_couleur = Liste_couleur[:dimensions[0]]
            Big_data_couleur[k] = Liste_couleur.copy()

    "ce paragraphe est différent puisque chaque ligne peuvent être indépendammentes inférieures à la dimension mais pas supérieur : ceci est provoqué par les 0 qui disparaissent lors de la transformation en base 64 par exemple"
    for k in range(len(Big_data_couleur)):
        if len(Big_data_couleur[k]) < dimensions[0]:
            Liste_couleur = Big_data_couleur[k].copy()
            Liste_couleur += [0] * (dimensions[0] - len(Big_data_couleur[k]))
            Big_data_couleur[k] = Liste_couleur.copy()

def option_changement():
    global Big_data_couleur, Big_data_objet

    "créer les cases colorées"
    for y in range(len(Big_data_couleur)):
        Liste_couleur, Liste_objet = Big_data_couleur[y].copy(), Big_data_objet[y].copy()
        for x in range(len(Liste_couleur)):
            if Liste_couleur[x] >= 0:
                couleur = Liste_couleur_boule[Liste_couleur[x]]
            else:
                couleur = Liste_couleur_boule[-Liste_couleur[x] - 1]

            coord = x * tgrille + ecart_bord, y * tgrille + ecart_bord, (x + 1) * tgrille + ecart_bord, (y + 1) * tgrille + ecart_bord
            Liste_objet[x] = canvas.create_rectangle(coord, fill=couleur, outline=couleur_grille)

        Big_data_couleur[y], Big_data_objet[y] = Liste_couleur.copy(), Liste_objet.copy()

def creation_boutons(dimension_x, dimension_y, place_boule, place_bouton):
    global carre_bouton, Liste_bouton

    if dimension_y < 400:
        longueur = dimension_y * 0.2
    else:
        longueur = place_bouton * 0.25

    carre_bouton = ['ecart_x', dimension_x + place_boule + place_bouton * 0.5 - place_bouton*0.1, 'ecart_y', dimension_y * 0.4 + ecart_bord, 'longueur', longueur, 'epaiseur', 4, 'couleur', 'black', 'couleur_activation', 'red', 'couleur_outline', 'white']

    "bouton option"
    Sacha_bouton(canvas=canvas, bouton=text, texte='option', x=dimension_x + place_boule + place_bouton * 0.5, y=dimension_y * 0.02 + ecart_bord, largueur=place_bouton * 0.15, commande=transfert, information=page_option, centrer=1, couleur_texte=Liste_modalite_dessin[13], epaiseur=carre_bouton[7])

    "fleche"
    for k in range(4):
        Sacha_bouton(canvas=canvas, bouton=fleche, carre=1, sens=k, couleur=carre_bouton[9], changement_couleur_activation=carre_bouton[11], x=carre_bouton[1] + (carre_bouton[5]*1.15)*(abs(2-k)-1), y=carre_bouton[3] + (carre_bouton[5]*1.15)*(1 - abs(1-k)), longueur=carre_bouton[5], epaiseur=carre_bouton[7], commande=decaler_dessin, appuyer_relacher_maintenu=3, couleur_outline=carre_bouton[13])

    "boule entre fleche"
    Liste_bouton = [Sacha_bouton(canvas=canvas, bouton=oval, carre=1, centrer=1, couleur=carre_bouton[9], x=carre_bouton[1] + carre_bouton[5]*0.47, y=carre_bouton[3] + carre_bouton[5]/2 - carre_bouton[5]*0.35, longueur=carre_bouton[5]*0.7, commande=activation_zone, couleur_outline=carre_bouton[13], epaiseur=carre_bouton[7], appuyer_relacher_maintenu=1)]

    "allumer ou non le bonton entre les flêches"
    Liste_couleur_activation = [carre_bouton[9], 'red']
    canvas.itemconfigure(Liste_bouton[0], fill=Liste_couleur_activation[passe_zone])

    "bouton suite"
    Sacha_bouton(canvas=canvas, bouton=text, texte='suite', x=dimension_x + place_boule + place_bouton * 0.5, y= dimension_y * 0.98 + - place_bouton * 0.15 + ecart_bord, largueur=place_bouton * 0.15, commande=transfert, information=fonction_fin, centrer=1, couleur_texte=Liste_modalite_dessin[13], epaiseur=carre_bouton[7])

    Liste_modalite = ['longueur', dimension_y / 15, 'ecart_inter_boule', (dimension_y - (dimension_y / 15) * len(Liste_couleur_boule)) / (len(Liste_couleur_boule) - 1)]

    "boules couleurs"
    for k in range(len(Liste_couleur_boule)):
        Liste_bouton += [Sacha_bouton(canvas=canvas, bouton=oval, carre=1, couleur=Liste_couleur_boule[k], couleur_outline='white', x=dimension_x + Liste_modalite[1]*2, y=ecart_bord + k*(Liste_modalite[1]+Liste_modalite[3]), longueur=Liste_modalite[1], commande=activation_couleur)]
    for k in range(len(Liste_precision)):
        Sacha_texte(canvas=canvas, couleur=carre_bouton[13], xt=dimension_x + Liste_modalite[1] * 3.5, yt=ecart_bord + k * (Liste_modalite[1] + Liste_modalite[3]) + (Liste_modalite[1])*0.25, largueur=(Liste_modalite[1])*0.5, epaiseur_texte=(Liste_modalite[1])*0.15, texte=Liste_precision[k])

    "bouton zone"
    Sacha_bouton(canvas=canvas, bouton=zone, x=ecart_bord/2, y=ecart_bord/2, longueur=dimension_x-ecart_bord, largueur=dimension_y+ecart_bord, couleur_outline=couleur_grille, epaiseur=ecart_bord/3, information=2, condition_fonction=valeur_zone, condition_valeur=1, fonction_recadrage_zone=recadrage_zone)

    "pour activer la couleur noire"
    activation_couleur([[Liste_bouton[1]], Liste_couleur_boule[0]], -1, 5)

Liste_modalite_dessin = ['longueur_canvas', 500, 'largueur_canvas', 350, 'largueur_bouton', 30, 'epaiseur_texte_bouton', 2, 'largueur_texte', 30, 'epaiseur_texte', 4, 'couleur_texte', 'white', 'couleur_bouton', 'black']

def page_option(*parametres):

    canvas.config(width=Liste_modalite_dessin[1], height=Liste_modalite_dessin[3])

    "retour"
    Sacha_bouton(canvas=canvas, bouton=text, texte='retour', x=Liste_modalite_dessin[1]/2, y=10, largueur=Liste_modalite_dessin[5], commande=transfert, information=interface_dessin, centrer=1, couleur_texte=Liste_modalite_dessin[13])

    "nombre case"
    Sacha_texte(canvas=canvas, texte='nombre case', xt=Liste_modalite_dessin[1]/2, yt=70, largueur=Liste_modalite_dessin[9], couleur=Liste_modalite_dessin[13], centrer=1, epaiseur_texte=Liste_modalite_dessin[11])

    minimum_dimension = 8

    "dimension x"
    Sacha_texte(canvas=canvas, texte='x', xt=Liste_modalite_dessin[1]*0.35, yt=125, largueur=Liste_modalite_dessin[9]*0.6, couleur=Liste_modalite_dessin[13], epaiseur_texte=Liste_modalite_dessin[11])
    Sacha_bouton(canvas=canvas, bouton=spinbox, texte=spinbox_range(minimum_dimension, 100), x=Liste_modalite_dessin[1]*0.6, y=120, largueur=Liste_modalite_dessin[9]*0.8, commande=variable_dimension_x, centrer=1, couleur_texte=Liste_modalite_dessin[13], information=dimensions[0] - minimum_dimension, couleur=Liste_modalite_dessin[15], couleur_outline=Liste_modalite_dessin[13], changement_couleur_activation='red', appuyer_relacher_maintenu=3, temps_repetition_commande=120)

    "dimension y"
    Sacha_texte(canvas=canvas, texte='y', xt=Liste_modalite_dessin[1]*0.35, yt=175, largueur=Liste_modalite_dessin[9]*0.6, couleur=Liste_modalite_dessin[13], epaiseur_texte=Liste_modalite_dessin[11])
    Sacha_bouton(canvas=canvas, bouton=spinbox, texte=spinbox_range(minimum_dimension, 100), x=Liste_modalite_dessin[1] * 0.6, y=170, largueur=Liste_modalite_dessin[9] * 0.8, commande=variable_dimension_y, centrer=1, couleur_texte=Liste_modalite_dessin[13], information=dimensions[1] - minimum_dimension, couleur=Liste_modalite_dessin[15], couleur_outline=Liste_modalite_dessin[13], changement_couleur_activation='red', appuyer_relacher_maintenu=3, temps_repetition_commande=120)

    "taille grille"
    Sacha_texte(canvas=canvas, texte='taille case', xt=Liste_modalite_dessin[1] / 2, yt=230, largueur=Liste_modalite_dessin[9], couleur=Liste_modalite_dessin[13], centrer=1, epaiseur_texte=Liste_modalite_dessin[11])
    Sacha_bouton(canvas=canvas, bouton=spinbox, texte=spinbox_range(3, 50), x=Liste_modalite_dessin[1]/2, y=290, largueur=Liste_modalite_dessin[9], commande=variable_tgrille, centrer=1, couleur_texte=Liste_modalite_dessin[13], information=tgrille - 3, couleur=Liste_modalite_dessin[15], couleur_outline=Liste_modalite_dessin[13], changement_couleur_activation='red', appuyer_relacher_maintenu=3, temps_repetition_commande=150)

def variable_dimension_x(information):
    global dimensions

    dimensions[0] = information + 8

def variable_dimension_y(information):
    global dimensions

    dimensions[1] = information + 8

def variable_tgrille(information):
    global tgrille

    tgrille = information + 3

def variable_big_data(base, type_variable):

    base_debut = len(Liste_couleur_boule)

    if type(base) == int:
        base_fin = base
    else:
        base_fin = base_debut

    if type(type_variable) != str:
        type_variable = 'liste'

    Big_data = [base_debut, base_fin]

    "chercher l'obligation"
    x_obligation, y_obligation = -1, 0

    for Liste_couleur in Big_data_couleur:

        valeur = ''
        for couleur in Liste_couleur:
            "l'obligation est marqué par des nombres négatifs"
            if couleur < 0:
                "pour ne le faire qu'une seule fois"
                if x_obligation == -1:
                    x_obligation, y_obligation = Liste_couleur.index(couleur), Big_data_couleur.index(Liste_couleur)

                couleur = couleur*(-1) - 1

            valeur += str(couleur)

        Big_data += [transforamtion_base_nouvelle_base(base_debut, base_fin, valeur, type_variable)]

    return Big_data, [len(Big_data_couleur[0]), len(Big_data_couleur)], [x_obligation, y_obligation]

def activation_couleur(commande, k, n_commande, *parametres):
    global bouton_selectionne, couleur_pinceau

    if bouton_selectionne[0] != commande[k * n_commande + 5] and len(bouton_selectionne) == 1:

        bouton_selectionne += commande[k * n_commande + 5]

        couleur_pinceau = commande[k * n_commande + 6]

        for l in range(20):
            canvas.after(10, deplacement_bouton(bouton_selectionne))
            canvas.update()

        bouton_selectionne.pop(0)

def deplacement_bouton(bouton_selectionne):

    canvas.move(bouton_selectionne[0], (tgrille*dimensions[1]/15)/20, 0)

    "tgrille*dimensions[1]/15 = la longueur d'une boule"
    canvas.move(bouton_selectionne[1], -(tgrille*dimensions[1]/15)/20, 0)

def activation_zone(*parametres):
    global passe_zone, corps_bouton_zone

    passe_zone = (passe_zone+1)%2
    Liste_couleur_activation = ['black', 'red']
    canvas.itemconfigure(Liste_bouton[0], fill=Liste_couleur_activation[passe_zone])

    canvas.delete(corps_bouton_zone)
    corps_bouton_zone = "inexistant banane"

def valeur_zone():

    return passe_zone

def dessinage(x_souris, y_souris, touche, Liste_zone, *parametres):
    global Big_data_couleur, Big_data_objet

    x_souris, y_souris = x_souris - ecart_bord, y_souris - ecart_bord
    coord_zone = Liste_zone[0]

    if type(coord_zone) == str:
        limite = [0, 0, dimensions[0], dimensions[1]]
    else:
        limite = []
        for k in range(4):
            limite += [(coord_zone[k] - ecart_bord) // tgrille + k // 2]

    if touche == '??' and x_souris > limite[0] and y_souris > limite[1] and x_souris < tgrille*limite[2] and y_souris < tgrille*limite[3] and (passe_zone == 0 or type(coord_zone) != str):

        if type(Liste_zone[0]) == str:
            "ça ne va dessiner qu'une seule case"
            limite = [x_souris//tgrille, y_souris//tgrille, x_souris//tgrille + 1, y_souris//tgrille + 1]

        for y in range(limite[1], limite[3]):

            for x in range(limite[0], limite[2]):

                "si t'essayes pas de dessiner sur l'obligation"
                if Big_data_couleur[y][x] >= 0:

                    canvas.delete(Big_data_objet[y][x])

                    coord = x*tgrille + ecart_bord, y*tgrille + ecart_bord, (x+1)*tgrille + ecart_bord, (y+1)*tgrille + ecart_bord
                    Big_data_objet[y][x] = canvas.create_rectangle(coord, fill=couleur_pinceau, outline=couleur_grille)

                    Big_data_couleur[y][x] = Liste_couleur_boule.index(couleur_pinceau)

def recadrage_zone(coord):

    "echanger les coordonnées si elles sont dans le mauvais sens coord 0 et 1 doivent être inférieurs à coord 2 et 3"
    for k in range(2):
        if coord[k + 2] < coord[k]:
            coord[k], coord[k + 2] = coord[k + 2], coord[k]

    "vérifier si l'obligation est dans la sélection"
    y = (coord[1] - ecart_bord) // tgrille
    y_max = (coord[3] - ecart_bord) // tgrille + 1

    "y > -9 est juste le cas d'arrêt"
    while y > -9 and y < y_max:

        x = (coord[0] - ecart_bord) // tgrille
        x_max = (coord[2] - ecart_bord) // tgrille + 1

        while x < x_max and y > -10:

            "si Big_data_couleur[y][x] est inférieur à 0, cela veut dire qu'on a trouvé un bout de l'obligation"
            if Big_data_couleur[y][x] < 0:

                position = [x, y]
                borne = [len(Big_data_couleur[0]), len(Big_data_couleur)]

                "k est la direction de la recherche : 0 vers la gauche, 1 vers le haut, 2 vers la droite, 3 vers le bas"
                for k in range(4):
                    "tant qu'on reste dans les bornes et que l'on est sur l'obligation"
                    while position[k % 2] * (-1) ** (k // 2) >= -(borne[k % 2] - 1) * (k // 2) and Big_data_couleur[position[1]][position[0]] < 0:
                        "changer de positionn en x ou y en augmentant ou diminuant"
                        position[k % 2] += (-1) ** (k // 2 + 1)

                    "comme on est en dehors du board ou de l'obligation, un dans le chemin invese"
                    position[k % 2] += (-1) ** (k // 2)

                    if coord[k] * (-1) ** (k // 2) > (position[k % 2] * tgrille + ecart_bord) * (-1) ** (k // 2):
                        coord[k] = (position[k % 2] + 0.5) * tgrille + ecart_bord

                y = -10

            x += 1

        y += 1

    return coord

def decaler_dessin(commande, k, n_commande, Liste_zone):
    global coord_zone, corps_bouton_zone, Big_data_couleur, Big_data_objet

    sens = commande[k*n_commande + 14]

    "déterminer les coordonnées, à partir de la selection ou pas"
    if corps_bouton_zone != 'inexistant banane':
        coord = coord_zone.copy()

    elif Liste_zone[0] == 'inexistant banane':
        coord = [0, 0, len(Big_data_couleur[0]), len(Big_data_couleur)]

    else:
        coord, corps_bouton_zone = Liste_zone[0], Liste_zone[1]

        for k in range(4):
            coord[k] = (coord[k] - ecart_bord) // tgrille + k // 2

    if sens%2 == 0:

        if coord[0] == 0 and sens == 2:
            coord[0] = 1

        if coord[2] == len(Big_data_objet[0]) and sens == 0:
            coord[2] += -1

        for y in range(coord[1], coord[3]):

            for objet in Big_data_objet[y][coord[0]:coord[2]]:
                canvas.move(objet, tgrille*(-1)**(sens//2), 0)

            if sens == 0:
                canvas.delete(Big_data_objet[y][coord[2]])
                Big_data_couleur[y] = Big_data_couleur[y][:coord[0]] + [0] + Big_data_couleur[y][coord[0]:coord[2]] + Big_data_couleur[y][coord[2] + 1:]
                Big_data_objet[y] = Big_data_objet[y][:coord[0]] + [0] + Big_data_objet[y][coord[0]:coord[2]] + Big_data_objet[y][coord[2] + 1:]
            else:
                canvas.delete(Big_data_objet[y][coord[0] - 1])
                Big_data_couleur[y] = Big_data_couleur[y][:coord[0]-1] + Big_data_couleur[y][coord[0]:coord[2]] + [0] + Big_data_couleur[y][coord[2]:]
                Big_data_objet[y] = Big_data_objet[y][:coord[0] - 1] + Big_data_objet[y][coord[0]:coord[2]] + [0] + Big_data_objet[y][coord[2]:]

        coord[0], coord[2] = coord[0] + (-1)**(sens//2), coord[2] + (-1)**(sens//2)
        canvas.move(corps_bouton_zone, tgrille*(-1)**(sens//2), 0)

    else:

        Big_data_couleur_intermediaire = []
        Big_data_objet_intermediaire = []
        for y in range(len(Big_data_couleur)):

            Big_data_couleur_intermediaire += [Big_data_couleur[y][coord[0]:coord[2]]]
            Big_data_objet_intermediaire += [Big_data_objet[y][coord[0]:coord[2]]]

        for Liste_objet in Big_data_objet_intermediaire[coord[1]:coord[3]]:
            for objet in Liste_objet:
                canvas.move(objet, 0, tgrille*(-1)**(sens//2))

        if coord[1] == 0 and sens == 3:
            coord[1] = 1

        if coord[3] == len(Big_data_objet) and sens == 1:
            coord[3] += -1

        if sens == 1:
            for objet in Big_data_objet_intermediaire[coord[3]]:
                canvas.delete(objet)

            "la case supprimé est la case d'index coord[3]"
            Big_data_couleur_intermediaire = Big_data_couleur_intermediaire[:coord[1]] + [[0]*(coord[2]-coord[0])] + Big_data_couleur_intermediaire[coord[1]:coord[3]] + Big_data_couleur_intermediaire[coord[3] + 1:]
            Big_data_objet_intermediaire = Big_data_objet_intermediaire[:coord[1]] + [[0] * (coord[2] - coord[0])] + Big_data_objet_intermediaire[coord[1]:coord[3]] + Big_data_objet_intermediaire[coord[3] + 1:]

        else:
            for objet in Big_data_objet_intermediaire[coord[1] - 1]:
                canvas.delete(objet)

            "la case supprimé est la case d'index coord[1] - 1"
            Big_data_couleur_intermediaire = Big_data_couleur_intermediaire[:coord[1] - 1] + Big_data_couleur_intermediaire[coord[1]:coord[3]] + [[0]*(coord[2]-coord[0])] + Big_data_couleur_intermediaire[coord[3]:]
            Big_data_objet_intermediaire = Big_data_objet_intermediaire[:coord[1] - 1] + Big_data_objet_intermediaire[coord[1]:coord[3]] + [[0] * (coord[2] - coord[0])] + Big_data_objet_intermediaire[coord[3]:]

        for k in range(len(Big_data_couleur)):

            Big_data_couleur[k] = Big_data_couleur[k][:coord[0]] + Big_data_couleur_intermediaire[k] + Big_data_couleur[k][coord[2]:]
            Big_data_objet[k] = Big_data_objet[k][:coord[0]] + Big_data_objet_intermediaire[k] + Big_data_objet[k][coord[2]:]

        coord[1], coord[3] = coord[1] + (-1) ** (sens // 2), coord[3] + (-1) ** (sens // 2)
        canvas.move(corps_bouton_zone, 0, tgrille * (-1) ** (sens // 2))

    if coord[0] == 0 or coord[1] == 0 or coord[2] == len(Big_data_couleur[0]) or coord[3] == len(Big_data_couleur):
        canvas.delete(corps_bouton_zone)
        corps_bouton_zone = 'inexistant banane'

    coord_zone = coord.copy()

def recreation_dessin(canvas, Big_data_dessin, dimension_x, taille_case, ecart_bord, Liste_machin):

    "Liste_machin : figure1, coord1, couleur1, couleur_outline1, epaiseur1, figure2, coord2, ..."

    "figure"
    Liste_figure = ['cercle', canvas.create_oval, 'rectangle', canvas.create_rectangle, 'ligne', canvas.create_line]

    if Big_data_dessin[0] != len(Liste_machin)/5:
        print('pas assez de coordonnées', len(Liste_machin))

    Big_data_objet = []
    Big_data_machin = []

    for y in range(len(Big_data_dessin[2:])):

        Ligne_dessin = transforamtion_base_nouvelle_base(Big_data_dessin[1], Big_data_dessin[0], Big_data_dessin[y + 2], 'str')

        Ligne_dessin = '0'*(dimension_x-len(Ligne_dessin)) + Ligne_dessin

        if len(Ligne_dessin) != dimension_x:
            print('probleme Ligne dessin dans recréation_dessin')

        for x in range(dimension_x):

            identifiant = int(Ligne_dessin[x])

            "s'il y a une figure à déssiner"
            if Liste_machin[identifiant*5] != 'rien':

                "savoir quelle figure c'est : cercle, rectangle..."
                figure = Liste_machin[identifiant*5]
                fonction = Liste_figure[Liste_figure.index(figure) + 1]

                "les coordonnées de la figure"
                coord_figure = Liste_machin[identifiant*5 + 1]
                coord = []
                position = [x, y]
                for k in range(4):
                    coord += [ecart_bord + position[k%2]*taille_case + coord_figure[k]]

                "créer l'objet et garder son identifiant mais je ne parle pas du même identifiant que la variable précedemment défini"
                Big_data_objet += [fonction(coord, width=Liste_machin[identifiant*5 + 4])]

                "changement de couleur"
                if Liste_machin[identifiant*5 + 2] != 'nothing':
                    canvas.itemconfigure(Big_data_objet[-1], fill=Liste_machin[identifiant*5 + 2])

                "changement de couleur outline"
                if Liste_machin[identifiant*5 + 3] != 'nothing':
                    canvas.itemconfigure(Big_data_objet[-1], outline=Liste_machin[identifiant*5 + 3])

            else:
                "identifiant de rien"
                Big_data_objet += [0]

            Big_data_machin += [identifiant]

    return Big_data_machin, Big_data_objet

def dessiner_bouton():

    initialistation_interface_dessin(canvas=canvas, dimensions=[30, 30], taille_grille=25, Liste_couleur=['black', 'grey', 'red'], Liste_precision=['rien', 'gris', 'rouge'], fonction_fin=page_fin)

def page_fin(*parametres):

    print(variable_big_data(3)[0])



#window = Tk()
#canvas = Canvas(window, width=100, height=100, bg='black')
#canvas.pack()

#dessiner_bouton()


#window.mainloop()