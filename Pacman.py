def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import*
from time import time, sleep
import math
#from Sacha_bouton import *
from Pacman_annexe import *
#meoooow

"début variable qui ne changeront jamais"

labyrinthe = 1
modalite_labyrinthe = 5

"nom, labyrinthe, dimensions, cage aux fantômes, nombre_fantome"
Liste_differents_labyrinthe = ['test', [5, 64, '38he', 'Wem', '38AN', '37kH', '37kH', '38he', 'Wem', '38he'], [9, 8], [4, 2], 2]
Liste_differents_labyrinthe += ['classic', [5, 64, '2aOPc4yu', '1L1rBmWé', '1RpjXn2y', '2lIZ7vR0', '1L1rmteR', '1RoV15ey', '1L3J6CVi', '2aCpècsg', '15NO2XD9', '15NRXAHs', '2aCbkn9h', '15jgdxèè', '2aCc2zyg', '15NO2XD9', '2aCc2zyg', '1L1rBmWé', '1RpjXn2y', '2hdWyfgC', '269LB&62', '1L3J6CVi', '1RAHwvBm', '1L1rmteR', '2aOPc4yu'], [19, 23], [9, 9], 4]
Liste_differents_labyrinthe += ['plagiat', [5, 64, 'TdsCJOtX', 'bnCfUA', 'Tcxvdi9P', 'HnzIYY9m', 'Jyj6ofbK', 'J6BAhw2I', 'Jc7fKv6N', 'HnNukmWU', 'TcyF8IRC', 'HnNIWaXF', 'JxlLQRq3', 'Hscépn98', 'STlgkkB3', 'rS12rmnc', 'rNmZfèrl', 'SUf463yi', 'bnCfUA', 'STkpLcfK', 'HrèXS9qX', 'JxsxYp3K', 'HnzHOqOA', 'TdsCJOtX'], [21, 22], [10, 8], 4]
Liste_differents_labyrinthe += ['impossible', [5, 64, 'oAscW&G3i', 'y5qyWLm1m', 'hXN9kywV2', 'hXROuaE&V', 'xVwi823l0', 'hP3gyK0X3', 'hNfK1ADG7', '8utIC5énV', 'hRdNopEIW', 'xVrP8cXLS', 'hRdNGsutw', 'xVpèjmo0j', 'oAscW&G3i'], [23, 13], [11, 7], 6]
Liste_differents_labyrinthe += ['remy', [5, 64, 'jWiKqC', 'bnC8fk', 'b&8m0N', 'bVmKeB', 'bVmUI3', 'bY&Ibw', 'bnJikw', 'bSgbOI', 'bRIOTa', 'bSéréR', 'bSUidZ', 'bT9WYu', 'bRIOyE', 'bnC8fk', 'hDOv&Z'], [15, 15], [4, 2], 5]


Liste_sortie_fantome = [0, 1, 2, 3, 4, 5, 6]

Liste_temps_attendue = [11, 9, 7, 5, 3, 1]
temps_reel = 14

langue = 0

place_droite = 250

tpm=30

Liste_couleur_pacman = ['yellow', 'red']
Liste_couleur_oeil_pacman = ['black', 'yellow']


"fin variable qui ne changeront jamais"

Liste_dimension = Liste_differents_labyrinthe[labyrinthe*4 + 2].copy()

def variable_debut_jeu():
    global Liste_dimension, Liste_coordonnees_fantomes, coordpm, vpm, Liste_bercaille, temps_bonus, position_cape, temps_minuteur, temps_attendue, temps_bonus_annexe

    Liste_dimension = Liste_differents_labyrinthe[labyrinthe*modalite_labyrinthe + 2].copy()
    Liste_mur_rouge = Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 3].copy()

    coordpm = [Liste_mur_rouge[0] * tpm, (Liste_mur_rouge[1] + 4) * tpm]

    nombre_fantome = Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 4]
    Liste_bercaille = [0] * nombre_fantome
    Liste_coordonnees_fantomes = [[Liste_mur_rouge[0] * tpm, (Liste_mur_rouge[1]+2) * tpm]] * nombre_fantome

    temps_attendue = Liste_temps_attendue[nombre_fantome - 1]
    temps_bonus = 0
    temps_bonus_annexe = 3
    temps_minuteur = 0
    vpm = tpm / 20

    position_cape = 0

    variables_importantes(tpm, Liste_dimension, canvas)

def fantome_annexe(coord_f, direction, bercaille, temps_sortie, Liste_fantome, dfg):
    global arret_jeu

    Liste_mur_rouge = Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 3].copy()
    xf, yf = coord_f[0], coord_f[1]

    if bercaille == 1 and coord_f[direction%2]%(tpm/16) == 0:
        "lorsqu'il s'est fait manger"
        vf = tpm/8
    elif xf == Liste_mur_rouge[0]*tpm and yf <= (Liste_mur_rouge[1]+0.5)*tpm and yf >= (Liste_mur_rouge[1]-0.5)*tpm + vpm/4:
        "quand il sort de sa tanière"
        vf = vpm/4
    elif temps_bonus != 0 or coord_f[direction%2]%vpm == vpm/2:
        "bonus"
        vf = vpm/2
    else:
        "normal"
        vf = vpm

    if coord_f[direction%2]%tpm == 0:

        deplacement_yeux(Liste_fantome, direction, distance_globe_oculaire, 1)

        coordonnees_mur_rouge = Liste_differents_labyrinthe[labyrinthe*modalite_labyrinthe+3]

        if xf == coordonnees_mur_rouge[0] * tpm and yf == (coordonnees_mur_rouge[1]+1) * tpm and temps_sortie <= temps_minuteur:
            "sortie de la tanière"
            direction = 3
            bercaille = 0
            if temps_bonus == 0:
                transformation_bonus_fantome(0, bercaille, Liste_fantome, dfg)
            else:
                transformation_bonus_fantome(1, bercaille, Liste_fantome, dfg)

        elif xf == coordonnees_mur_rouge[0] * tpm and yf == (coordonnees_mur_rouge[1] - 1) * tpm and direction == 3:
            "fin de sorite de la tanière"
            direction = randint(1, 2)*2 - 2

        elif bercaille == 1:
            "si pacman venère a mangé le fantome"
            direction = retour_au_bercaille(coord_f[0], coord_f[1], Liste_sonde)

        else:
            Liste_obstacle = collision_mur_fantome(xf, yf, Big_data_figure, temps_sortie, temps_minuteur, Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 3])

            if Liste_obstacle != [1, 0, 1, 0] and Liste_obstacle != [0, 1, 0, 1]:
                "direction aléatoire"
                direction = direction_aleatoire(Liste_obstacle, inverser_direction(direction))

        deplacement_yeux(Liste_fantome, direction, distance_globe_oculaire, 0)

    "deplacement du corps + changement des coordonnées"
    coord_f[direction%2] = deplacement(Liste_fantome, coord_f[direction%2], direction, vf)

    if bercaille == 0:
        arret_jeu, bercaille, direction = collision_pacman_fantôme(coordpm[0], coordpm[1], coord_f[0], coord_f[1], ecartpm_mur, ecartf_murx, ecartf_mury, temps_bonus, Liste_fantome, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome, direction, Liste_sonde, distance_globe_oculaire, arret_jeu)

    return coord_f, direction, bercaille

def fantome():
    global Liste_fantome_direction, Liste_coordonnees_fantomes, Liste_bercaille, position_cape

    position_cape += diametre_cape / 10
    if position_cape == diametre_cape:
        position_cape = -diametre_cape

    for dfg in range(len(Liste_fantome_direction)):

        coord_f = Liste_coordonnees_fantomes[dfg].copy()
        direction = Liste_fantome_direction[dfg]
        bercaille = Liste_bercaille[dfg]

        coord_f, Liste_fantome_direction[dfg], Liste_bercaille[dfg] = fantome_annexe(coord_f, direction, bercaille, Liste_sortie_fantome[dfg], Liste_fantome[dfg*12:(dfg+1)*12], dfg)
        Liste_coordonnees_fantomes[dfg] = coord_f.copy()

        for k in range(3):
            canvas.move(Liste_fantome[k + 2 + 12 * dfg], diametre_cape / 10, 0)
            if position_cape == -diametre_cape:
                canvas.move(Liste_fantome[k + 2 + 12 * dfg], -2*diametre_cape, 0)

    minuteur()

    canvas.update()

def gestion_pacman(coordp, sens):
    global temps_bonus, nb, ob, coordpm, ecartpm_mur, Liste_obstacle, Big_data_figure, Big_data_objet

    "déplace pacman + change coordonnées en fonction"
    coordpm[sens%2] = deplacement(Liste_pacman, coordp[sens%2], sens, vpm)

    xpm, ypm = coordpm[0], coordpm[1]

    "manger"
    if xpm % tpm == 0 and ypm % tpm == 0:
        "boule : 0, bonus : 3, d'où le %3"
        if Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm / tpm)]%3 == 0:

            if Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm / tpm)] == 3:
                "bonus"
                if temps_bonus == 0:
                    transformation_bonus(xpm, ypm, sens, 1)

                temps_bonus = temps_bonus_annexe

            canvas.delete(Big_data_objet[int((ypm // tpm) * Liste_dimension[0] + xpm / tpm)])
            "rien : 1"
            Big_data_figure[int((ypm // tpm) * Liste_dimension[0] + xpm // tpm)] = 1
            Big_data_objet[int((ypm // tpm) * Liste_dimension[0] + xpm / tpm)] = 0

        Liste_obstacle = collision_mur_pacman(coordpm[0], coordpm[1], Big_data_figure)

        ob = 359
    else:
        "ouverture bouche"
        if coordpm[sens%2] % tpm == tpm / 2:
            ob = 269
        elif coordpm[sens%2] % tpm < tpm / 2:
            ob += (180*vpm/tpm)*(-1)**(sens//2+1)
        elif coordpm[sens%2] % tpm > tpm / 2:
            ob += (180*vpm/tpm)*(-1)**(sens//2)
        else:
            print('shit')

    "le 180 signifie 90*2, 90 fait rérence à la différence entre 359 et 269"
    canvas.itemconfigure(Liste_pacman[0], extent=ob, start=(360-sens*180-ob)/2)

    if temps_bonus != 0:
        temps_bonus += -temps_reel / 1000
        if temps_bonus <= 0:
            "fin bonus"
            temps_bonus = 0

            transformation_bonus(xpm, ypm, sens, 0)

    fantome()

    canvas.update()

def transformation_bonus(xpm, ypm, sens, bonus):
    global ecartpm_mur, tpmc, ecartpmeye, teye, Liste_pacman

    "transformation par effaçage et recréation"
    "transformation pacman pour devenir venère"
    for k in range(2):
        canvas.delete(Liste_pacman[k])

    ecartpm_mur, tpmc, ecartpmeye, teye, Liste_pacman = creation_pacman_annexe(xpm, ypm, ob, Liste_couleur_pacman[bonus], Liste_couleur_oeil_pacman[bonus], (360 - sens * 180 - ob) / 2, bonus)
    deplacement_oeil(Liste_pacman[1], sens, (tpmc - 2 * ecartpmeye - teye[0]), 0)

    "changements couleurs fantomes"
    for dfg in range(Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 4]):
        transformation_bonus_fantome(bonus, Liste_bercaille[dfg], Liste_fantome[dfg*12:(dfg+1)*12], dfg)

def transformation_bonus_fantome(bonus, bercaille, Liste_fantome, dfg):

    if bercaille == 0:
        for k in range(2):
            canvas.itemconfigure(Liste_fantome[k], fill=Liste_couleur_corps_fantome[dfg - (dfg+3)*bonus], outline=Liste_couleur_corps_fantome[dfg - (dfg+3)*bonus])
            canvas.itemconfigure(Liste_fantome[k + 7], fill=Liste_globe_oculaire_fantome[bonus], outline=Liste_globe_oculaire_fantome[4 + 1*bonus])
        for k in range(3):
            canvas.itemconfigure(Liste_fantome[k + 9], fill=Liste_couleur_corps_fantome[dfg - (dfg + 1) * bonus], outline=Liste_couleur_corps_fantome[dfg - (dfg + 1) * bonus])

def minuteur():
    global temps_minuteur, Liste_minuteur

    if int(temps_minuteur) != int(temps_minuteur + temps_reel / 1000):

        for k in range(2):
            temps_minuteur, Liste_minuteur = deplacement_minuteur(k+1, temps_minuteur, Liste_minuteur, temps_reel)

        "complication : une minute est égale à 60 secondes et pas 100"
        if ('00' + str(int(temps_minuteur)))[-2:] == '59':
            temps_minuteur += 40

            temps_minuteur, Liste_minuteur = deplacement_minuteur(0, temps_minuteur, Liste_minuteur, temps_reel)

            for k in range(4):
                temps_minuteur, Liste_minuteur = deplacement_minuteur(1, 70-temps_reel/2000 + k*10, Liste_minuteur, temps_reel)

    temps_minuteur += temps_reel / 1000

def activationpac(sens):
    global prio

    while prio == -1 and arret_jeu == 0:
        canvas.after(temps_attendue, fantome())

    deplacement_oeil(Liste_pacman[1], sens, (tpmc - 2 * ecartpmeye - teye[0]), 1)
    sens = prio
    deplacement_oeil(Liste_pacman[1], sens, (tpmc - 2 * ecartpmeye - teye[0]), 0)

    while 0 in Big_data_figure and arret_jeu == 0 and Liste_obstacle[sens] == 0 and (prio == sens or (Liste_obstacle[inverser_direction(sens)] == 1 or prio != inverser_direction(sens)) and (ob < 359 or Liste_obstacle[(sens+1)%4] == 1 or prio != (sens+1)%4) and (ob < 359 or Liste_obstacle[(sens+3)%4] == 1 or prio != (sens+3)%4)):
        canvas.after(temps_attendue, gestion_pacman(coordpm, sens))

    if prio == sens and arret_jeu == 0:
        prio = -1

    return sens

def fin():

    canvas.delete(Liste_pacman[1])

    if 0 in Big_data_figure:

        ob = 359
        sens = 0
        while ob != 15:
            ob = ob-1
            canvas.itemconfigure(Liste_pacman[0], extent=ob, start=(360 - sens * 180 - ob) / 2)
            canvas.update()
            sleep(0.001)

        Liste_langue = ['game over', 'perdu']

    else:
        Liste_langue = ['victory', 'victoire']

    Sacha_texte(canvas=canvas, texte=Liste_langue[langue], xt=Liste_dimension[0]*tpm / 2 * 1.05, yt=(Liste_dimension[1]*tpm-Liste_modalite[9]*2)/2, largueur=tpm*0.7, epaiseur_texte=tpm*0.13, couleur='red', couleur_changement=['white'], repetition=7, temps_changement_couleur=300, centrer=1)

    commande, k, n_commande = [page_accueil], -1, 18
    transfert(commande, k, n_commande)

window = Tk()
canvas = Canvas(window, width=5, height=5, bg='black')
canvas.pack()

def clavier(*parametre):
    global prio

    Liste = ['d', 's', 'q', 'z']
    prio = Liste.index(parametre[2])

def jeu_concret(*parametres):
    global arret_jeu, prio

    print("jeu concret")

    effacer_bouton('all')

    Liste_langue = ['ready', 'pret']
    pret = Sacha_texte(canvas=canvas, texte=Liste_langue[langue], xt=Liste_dimension[0]*tpm / 2 * 1.05, yt=(Liste_dimension[1]*tpm-Liste_modalite[9]*2)/2, largueur=Liste_modalite[9]*2, epaiseur_texte=Liste_modalite[11]*2, couleur='red', couleur_changement=['white'], repetition=5, temps_changement_couleur=500, centrer=1)

    for ligne in pret:
        canvas.delete(ligne)

    Sacha_bouton(canvas=canvas, commande=page_pause, couleur=Liste_modalite[5], texte='pause', bouton=text, couleur_texte=Liste_modalite[7], x=Liste_dimension[0] * tpm + place_droite / 2, y=(Liste_dimension[1] * tpm - Liste_modalite[9]) / 2, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)
    rajout_fonction('appuyer', 'd', clavier, 's', clavier, 'q', clavier, 'z', clavier)

    arret_jeu = 0

    if temps_minuteur == 0:
        sens = 0
        prio = - 1
    else:
        sens = prio

    while 0 in Big_data_figure and arret_jeu == 0:
        sens = activationpac(sens)

    if arret_jeu != 1:
        fin()

" Les différents pages "

Liste_modalite = ['longueur canvas', 460, 'largueur canvas', 400, 'couleur_bouton', 'black', 'couleur_texte_bouton', 'white', 'largueur_texte', 24, 'epaiseur_texte', 3, 'largueur bouton', 30, 'couleur_texte', 'white']

def page_accueil(*parametres):

    canvas.config(width=Liste_modalite[1], height=Liste_modalite[3])

    Liste_langue = ['maze', 'labyrinthe', 'play', 'jouer']

    Liste_nom = []
    for k in range(len(Liste_differents_labyrinthe)//modalite_labyrinthe):
        Liste_nom += [Liste_differents_labyrinthe[modalite_labyrinthe*k]]

    "labyrinthe"
    Sacha_texte(canvas=canvas, texte=Liste_langue[langue], xt=Liste_modalite[1] / 2, yt=10, largueur=Liste_modalite[9], epaiseur_texte=Liste_modalite[11], couleur='white', centrer=1)
    "spinbox nom labyrinthe"
    Sacha_bouton(canvas=canvas, commande=recuperer_labyrinthe, bouton=spinbox, texte=Liste_nom, x=Liste_modalite[1]/2, y=60, largueur=30, appuyer_relacher_maintenu=2, centrer=1, couleur=Liste_modalite[5], couleur_outline=Liste_modalite[7], couleur_texte=Liste_modalite[7], changement_couleur_activation='red', epaiseur_texte=Liste_modalite[11], information=labyrinthe)

    "bouton pour modifier labyrinthe"
    Sacha_bouton(canvas=canvas, commande=transfert, information=page_dessin, couleur=Liste_modalite[5], couleur_outline=Liste_modalite[7], bouton=oval, x=Liste_modalite[1]/2, y=100, longueur=Liste_modalite[13], carre=1, epaiseur=Liste_modalite[11], appuyer_relacher_maintenu=2, changement_couleur_activation='red', centrer=1)

    "jouer"
    Sacha_bouton(canvas=canvas, commande=transfert, information=page_jeu, couleur=Liste_modalite[5], texte=Liste_langue[langue+2], bouton=text, couleur_texte=Liste_modalite[7], x=Liste_modalite[1]/2, y=180, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)

    "option"
    Sacha_bouton(canvas=canvas, commande=transfert, information=page_option, couleur=Liste_modalite[5], texte='options', bouton=text, couleur_texte=Liste_modalite[7], x=Liste_modalite[1] / 2, y=250, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)

    "créer labyrinthe"
    Sacha_bouton(canvas=canvas, commande=transfert, information=page_dessin, couleur=Liste_modalite[5], texte='creer labyrinthe', bouton=text, couleur_texte=Liste_modalite[7], x=Liste_modalite[1] / 2, y=330, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)

def page_jeu(*parametres):
    global bandelette, Big_data_figure, Big_data_objet, Liste_sonde, Liste_minuteur, Liste_fantome, ecartf_murx, ecartf_mury, diametre_cape, distance_globe_oculaire, Liste_fantome_direction, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome, Liste_pacman, ecartpm_mur, ecartpmeye, tpmc, teye, Liste_obstacle, ob, corps_minuteur

    print("page jeu")

    variable_debut_jeu()

    canvas.config(width=Liste_dimension[0] * tpm + place_droite, height=Liste_dimension[1] * tpm)

    bandelette, Big_data_figure, Big_data_objet = creation_labyrinthe(Liste_differents_labyrinthe[labyrinthe*modalite_labyrinthe:(labyrinthe+1)*modalite_labyrinthe])
    Liste_sonde = La_sonde(Liste_differents_labyrinthe[labyrinthe*modalite_labyrinthe+3], Big_data_figure, Liste_dimension)

    "debut minuteur"

    print("debut minuteur")

    Liste_minuteur = [Sacha_texte(canvas=canvas, texte=':', xt=(Liste_dimension[0] - 0.4)*tpm + place_droite/2, yt=Liste_dimension[1] * tpm*0.1 - tpm*0.3, largueur=tpm*2, epaiseur_texte=Liste_modalite[11]*3, couleur='red')]

    for position in range(3):

        if position > 0:
            position += 0.7

        for chiffre in range(10):
            Liste_minuteur += [Sacha_texte(canvas=canvas, texte=str(chiffre), xt=(Liste_dimension[0] - 2.2 + position*1.5) * tpm + place_droite / 2, yt=(Liste_dimension[1] * tpm) * 0.1 - 5*tpm, largueur=tpm*2, epaiseur_texte=Liste_modalite[11] * 3, couleur='red')]

    for position in range(3):
        numero = Liste_minuteur[1 + position*10]
        for ligne in numero:
            canvas.move(ligne, 0, 5*tpm)

    "fin minuteur"

    Liste_fantome, ecartf_murx, ecartf_mury, diametre_cape, distance_globe_oculaire, Liste_fantome_direction, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome = creation_corps_fantome(Liste_coordonnees_fantomes, Liste_differents_labyrinthe[labyrinthe*modalite_labyrinthe+4])
    Liste_pacman, ecartpm_mur, ecartpmeye, tpmc, teye, Liste_obstacle, ob = creation_pacman(coordpm[0], coordpm[1], Liste_couleur_pacman[0], Liste_couleur_oeil_pacman[0])

    jeu_concret()

def page_pause(*parametres):
    global arret_jeu

    arret_jeu = 1

    effacer_bouton('all')

    ecart = tpm*1.5

    Sacha_bouton(canvas=canvas, commande=transfert, information=page_accueil, couleur=Liste_modalite[5], texte='menu', bouton=text, couleur_texte=Liste_modalite[7], x=Liste_dimension[0] * tpm + place_droite / 2, y=(Liste_dimension[1] * tpm - Liste_modalite[9]) / 2 - ecart, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)

    Liste_langue = ['resume', 'reprendre']
    Sacha_bouton(canvas=canvas, commande=jeu_concret, couleur=Liste_modalite[5], texte=Liste_langue[langue], bouton=text, couleur_texte=Liste_modalite[7], x=Liste_dimension[0] * tpm + place_droite / 2, y=(Liste_dimension[1] * tpm - Liste_modalite[9]) / 2 + ecart, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)


def page_option(*parametres):

    canvas.config(width=Liste_modalite[1], height=Liste_modalite[3])

    Liste_langue = ['return', 'retour', 'language', 'langue', 'interface size', 'taille interface']

    "menu"
    Sacha_bouton(canvas=canvas, commande=transfert, information=page_accueil, couleur=Liste_modalite[5], texte='menu', bouton=text, couleur_texte=Liste_modalite[7], x=Liste_modalite[1] / 2, y=10, largueur=Liste_modalite[13], epaiseur=Liste_modalite[11], centrer=1, appuyer_relacher_maintenu=2)

    "langue"
    Sacha_texte(canvas=canvas, texte=Liste_langue[langue + 2], xt=Liste_modalite[1] / 2, yt=70, largueur=Liste_modalite[9], epaiseur_texte=Liste_modalite[11], couleur=Liste_modalite[15], centrer=1)
    Sacha_bouton(canvas=canvas, commande=recuperer_langue, bouton=spinbox, texte=['english', 'francais'], x=Liste_modalite[1] / 2, y=110, largueur=30, appuyer_relacher_maintenu=2, centrer=1, changement_couleur_activation='red', epaiseur_texte=Liste_modalite[11], couleur_texte=Liste_modalite[7], information=langue)

    "tpm"
    Sacha_texte(canvas=canvas, texte=Liste_langue[langue + 4], xt=Liste_modalite[1] / 2, yt=200, largueur=Liste_modalite[9], epaiseur_texte=Liste_modalite[11], couleur=Liste_modalite[15], centrer=1)
    Sacha_bouton(canvas=canvas, commande=taille_interface, bouton=spinbox, texte=spinbox_range(1, 6), x=Liste_modalite[1] / 2, y=245, largueur=30, appuyer_relacher_maintenu=3, centrer=1, couleur='black', changement_couleur_activation='red', epaiseur_texte=Liste_modalite[11], couleur_texte=Liste_modalite[7], information=int(tpm/5)-4)

def page_dessin(commande, k, n_commande, *parametres):

    Liste_activation = [text, oval]
    Big_data_couleur = ['nothing', Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 1].copy()]
    dimensions = [[10, 10], Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 2]]
    cage_fantome = Liste_differents_labyrinthe[labyrinthe * modalite_labyrinthe + 3]
    positon_obligation = [[2, 2], [cage_fantome[0]-2, cage_fantome[1]]]

    bouton = commande[k * n_commande + 12]
    activation = Liste_activation.index(bouton)

    obligation = [positon_obligation[activation], [2, 2, 4, 2, 2], [2, 1, 1, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2]]
    initialistation_interface_dessin(canvas=canvas, dimensions=dimensions[activation], taille_grille=40, fonction_retour=page_accueil, Liste_couleur=['black', 'grey', 'blue', 'yellow', 'red'], Liste_obligation=obligation, Liste_precision=['boule', 'rien', 'mur', 'bonus', 'mur f'], fonction_fin=page_fin_dessinage, Big_data_couleur=Big_data_couleur[activation])

def page_fin_dessinage(*parametres):
    global plan_labyrinthe, dimensions, position_cage_fantome, nom_labyrinthe, n_fantome

    "recupérer le plan du labyrinthe"
    plan_labyrinthe, dimensions, position_cage_fantome = variable_big_data(64, 'str')

    position_cage_fantome[0] += 2

    nom_labyrinthe = str(len(Liste_differents_labyrinthe)//modalite_labyrinthe)
    n_fantome = 3

    canvas.config(width=Liste_modalite[1], height=Liste_modalite[3]-80, bg='black')

    #"retour"
    #Sacha_bouton(canvas=canvas, bouton=text, texte='retour', x=Liste_modalite[1]/2, y=40, largueur=Liste_modalite[13], commande=transfert, information=interface_dessin, centrer=1, couleur=Liste_modalite[5], couleur_texte=Liste_modalite[7])

    "nom labyrinthe"
    Sacha_texte(canvas=canvas, texte='nom labyrinthe', xt=Liste_modalite[1] / 2, yt=30, largueur=Liste_modalite[9] * 0.8, couleur=Liste_modalite[15], centrer=1, epaiseur_texte=Liste_modalite[11])
    Sacha_bouton(canvas=canvas, bouton=saisie_texte, x=Liste_modalite[1] / 2, y=70, longueur=250, largueur=Liste_modalite[9], centrer=1, appuyer_relacher_maintenu=1, commande=recuperer_nom_labyrinthe)

    "nombre_fantome"
    Sacha_texte(canvas=canvas, texte='nombre fantome', xt=Liste_modalite[1] / 2, yt=130, largueur=Liste_modalite[9]*0.8, couleur=Liste_modalite[15], centrer=1, epaiseur_texte=Liste_modalite[11])
    Sacha_bouton(canvas=canvas, bouton=spinbox, texte=spinbox_range(1, 7), x=Liste_modalite[1] / 2, y=175, largueur=Liste_modalite[13], commande=recuperer_nfantome, centrer=1, couleur=Liste_modalite[5], couleur_texte=Liste_modalite[7], information=n_fantome - 1, couleur_outline=Liste_modalite[7], changement_couleur_activation='red', appuyer_relacher_maintenu=3, temps_repetition_commande=150)

    "fin"
    Sacha_bouton(canvas=canvas, bouton=text, texte='fin', x=Liste_modalite[1] / 2, y=260, largueur=Liste_modalite[13], commande=transfert, information=rajout_labyrinthe, centrer=1, couleur=Liste_modalite[5], couleur_texte=Liste_modalite[7])

    return plan_labyrinthe, dimensions, position_cage_fantome

def rajout_labyrinthe(*parametres):
    global Liste_differents_labyrinthe

    print('Liste_differents_labyrinthe +=', [nom_labyrinthe, plan_labyrinthe, dimensions, position_cage_fantome, n_fantome])
    Liste_differents_labyrinthe += [nom_labyrinthe, plan_labyrinthe, dimensions, position_cage_fantome, n_fantome]

    page_accueil()

" Récupérer Variable "

def recuperer_labyrinthe(information):
    global labyrinthe

    labyrinthe = information

def recuperer_langue(information):
    global langue

    langue = information

    commande, k, n_commande = [page_option], -1, 18
    transfert(commande, k, n_commande)

def recuperer_nfantome(information):
    global n_fantome

    n_fantome = information

def recuperer_nom_labyrinthe(commande, k, n_commande, *parametres):
    global nom_labyrinthe

    nom_labyrinthe = commande[(k-1)*n_commande + 18]

def taille_interface(information):
    global tpm

    tpm = information*5

page_accueil()

window.mainloop()