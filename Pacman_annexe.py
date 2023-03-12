from Dessin import *

def variables_importantes(v1, v2, v3):
    global tpm, Liste_dimension, canvas#, Liste_differents_labyrinthe, labyrinthe

    tpm = v1
    Liste_dimension = v2
    canvas = v3
    #Liste_differents_labyrinthe = v4
    #labyrinthe = v5

def collision_mur_fantome(xf, yf, Big_data_figure, temps_sortie, temps_minuteur, cage_fantome):

    mfd, mfb, mfg, mfh = 1, 1, 1, 1

    "égal à 2 signifie qu'il y a un mur et 4 mur rouge"
    if xf-tpm < 0 or Big_data_figure[int((yf // tpm)*Liste_dimension[0] + xf//tpm-1)] != 2 and (Big_data_figure[int((yf // tpm)*Liste_dimension[0] + xf//tpm-1)] != 4 or temps_sortie < temps_minuteur):
        mfg = 0
    if xf+tpm >= Liste_dimension[0]*tpm or Big_data_figure[int((yf // tpm)*Liste_dimension[0] + xf//tpm + 1)] != 2 and (Big_data_figure[int((yf // tpm)*Liste_dimension[0] + xf//tpm + 1)] != 4 or temps_sortie < temps_minuteur):
        mfd = 0
    if yf-tpm < 0 or Big_data_figure[int((yf // tpm - 1)*Liste_dimension[0] + xf//tpm)] != 2 and (Big_data_figure[int((yf // tpm - 1)*Liste_dimension[0] + xf//tpm)] != 4 or temps_sortie < temps_minuteur):
        mfh = 0
    if yf+tpm >= Liste_dimension[1]*tpm or Big_data_figure[int((yf // tpm + 1)*Liste_dimension[0] + xf//tpm)] != 2 and (Big_data_figure[int((yf // tpm + 1)*Liste_dimension[0] + xf//tpm)] != 4 or temps_sortie < temps_minuteur and xf//tpm != cage_fantome[0]):
        mfb = 0

    return [mfd, mfb, mfg, mfh]

def collision_mur_pacman(xpm, ypm, Big_data_figure):

    md, mb, mg, mh = 1, 1, 1, 1
    "4 par rapport aux murs rouges et 2 aux murs bleus"
    if xpm-tpm < 0 or Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm-1)] != 2 and Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm-1)] != 4:
        mg = 0
    if xpm+tpm >= Liste_dimension[0]*tpm or Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm+1)] != 2 and Big_data_figure[int(((ypm//tpm)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm+1)] != 4:
        md = 0
    if ypm-tpm < 0 or Big_data_figure[int(((ypm//tpm-1)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm)] != 2 and Big_data_figure[int(((ypm//tpm-1)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm)] != 4:
        mh = 0
    if ypm+tpm >= Liste_dimension[1]*tpm or Big_data_figure[int(((ypm//tpm+1)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm)] != 2 and Big_data_figure[int(((ypm//tpm+1)%Liste_dimension[1])*Liste_dimension[0] + xpm/tpm)] != 4:
        mb = 0

    return [md, mb, mg, mh]

def collision_pacman_fantôme(xpm, ypm, xf, yf, ecartpm_mur, ecartf_murx, ecartf_mury, temps_bonus, Liste_fantome, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome, direction, Liste_sonde, distance_globe_oculaire, arret_jeu):

    "fantome est à la droite de pacman, gauche, bas, haut"
    if xpm + tpm*0.9 - ecartpm_mur >= xf + ecartf_murx and xpm + ecartpm_mur <= xf + tpm*0.9 - ecartf_murx and ypm + tpm*0.9 - ecartpm_mur >= yf + ecartf_mury and ypm + ecartpm_mur <= yf + tpm*0.9 - ecartf_mury:

        if temps_bonus == 0:
            return 2, 0, direction
        else:
            "changements couleurs fantomes"
            for k in range(5):
                canvas.itemconfigure(Liste_fantome[(9 + k) % 12], fill=Liste_couleur_corps_fantome[-2], outline=Liste_couleur_corps_fantome[-2])
            for k in range(2):
                canvas.itemconfigure(Liste_fantome[k + 7], fill=Liste_globe_oculaire_fantome[2], outline=Liste_globe_oculaire_fantome[5])

            deplacement_yeux(Liste_fantome, direction, distance_globe_oculaire, 1)

            "si le changement de sens est compatible avec les coordonnées"
            if (Liste_sonde[int((yf//tpm)*Liste_dimension[0] + xf//tpm)]%10 - 1)%2 == direction%2:
                direction = Liste_sonde[int((yf//tpm)*Liste_dimension[0] + xf//tpm)]%10 - 1
            else:
                coord = [xf, yf]
                coord[direction%2] += tpm
                xf, yf = coord[0], coord[1]

                direction = Liste_sonde[int((yf // tpm) * Liste_dimension[0] + xf // tpm)] % 10 - 1

            deplacement_yeux(Liste_fantome, direction, distance_globe_oculaire, 0)

            return arret_jeu, 1, direction
    else:
        return arret_jeu, 0, direction


def creation_labyrinthe(Liste_labyrinthe):

    "boule"
    tboule = tpm * (3 / 17)
    Liste_machin = ['cercle', [(tpm - tboule) / 2, (tpm - tboule) / 2, (tpm + tboule) / 2, (tpm + tboule) / 2], 'white', 'nothing', 2]

    "rien"
    Liste_machin += ['rien', 0, 0, 0, 0]

    "mur normal"
    Liste_machin += ['rectangle', [0, 0, tpm, tpm], 'nothing', 'blue', 2]

    "bonus"
    tbonus = tpm * (9 / 20)
    Liste_machin += ['cercle', [(tpm - tbonus)/2, (tpm - tbonus)/2, (tpm + tbonus)/2, (tpm + tbonus)/2], 'white', 'nothing', 2]

    "mur fantome"
    Liste_machin += ['rectangle', [0, 0, tpm, tpm], 'nothing', 'red', 2]

    Liste_dimension = Liste_labyrinthe[2]

    Big_data_figure, Big_data_objet = recreation_dessin(canvas, Liste_labyrinthe[1], Liste_dimension[0], tpm, tpm*0, Liste_machin)

    bandelette = tpm / 2
    coordlimd = Liste_dimension[0]*tpm, 0, Liste_dimension[0]*tpm + bandelette, Liste_dimension[1]*tpm
    canvas.create_rectangle(coordlimd, fill='red')

    return bandelette, Big_data_figure, Big_data_objet

def creation_corps_fantome(Liste_coordonnees_fantomes, nombre_fantome):

    Liste_fantome = [0] * 12 * nombre_fantome
    Liste_fantome_direction = [1] * nombre_fantome

    for dfg in range(nombre_fantome):

        coord_f = Liste_coordonnees_fantomes[dfg]
        Liste_fantome, ecartf_murx, ecartf_mury, diametre_cape, distance_globe_oculaire, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome = corps_fantome(dfg, coord_f[0], coord_f[1], Liste_fantome, Liste_fantome_direction[dfg])

    return Liste_fantome, ecartf_murx, ecartf_mury, diametre_cape, distance_globe_oculaire, Liste_fantome_direction, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome

def corps_fantome(dfg, xf, yf, Liste_fantome, direction):

    fl = tpm / 2
    fL = tpm / 4 * 2.5
    tcf = fL / 2
    diametre_cape = fL / 5
    ecartf_mury = (tpm - tcf - fl) / 2
    ecartf_murx = (tpm - fL) / 2
    tfeye = tpm / 5
    ecartfeye_eye = tpm / 13
    ecartfeye_f = (fL - 2 * tfeye - ecartfeye_eye) / 2
    tgo = tpm / 13
    tbouche = fL / 5
    ecart_fantome_bouche = (fL - tbouche * 3) / 2
    ybouche = tpm / 4

    Liste_couleur_corps_fantome = ['red', 'blue', 'pink', 'orange', 'purple', 'brown', 'white', 'green', 'yellow', 'blue', 'black', 'white']
    Liste_globe_oculaire_fantome = ['blue', 'white', 'black', 'bordure', 'black', 'white']

    "crane"
    coord = xf + ecartf_murx, yf + ecartf_mury, xf + ecartf_murx + fL, yf + ecartf_mury + fL
    Liste_fantome[12 * dfg] = canvas.create_arc(coord, fill=Liste_couleur_corps_fantome[dfg], extent=180, start=0)
    "corps"
    coord = xf + ecartf_murx, yf + tcf + ecartf_mury, xf + ecartf_murx + fL, yf + tcf + fl + ecartf_mury - diametre_cape*0.58
    Liste_fantome[1 + 12 * dfg] = canvas.create_rectangle(coord, fill=Liste_couleur_corps_fantome[dfg], outline=Liste_couleur_corps_fantome[dfg])

    "bas (cape ou vaguelette)"
    for k in range(3):
        coord = xf + ecartf_murx + 2 * k * diametre_cape, yf + tpm - ecartf_mury - diametre_cape, xf + ecartf_murx + diametre_cape + 2 * k * diametre_cape, yf + tpm - ecartf_mury
        Liste_fantome[k + 2 + 12 * dfg] = canvas.create_arc(coord, fill="black", extent=180, start=0)

    "yeux"
    nfeye = 0
    for k in range(2):
        coord = xf + ecartf_murx + ecartfeye_f + nfeye, yf + ecartf_mury + tcf - tfeye / 2, xf + ecartf_murx + ecartfeye_f + tfeye + nfeye, yf + ecartf_mury + tcf + tfeye / 2
        Liste_fantome[k + 5 + 12 * dfg] = canvas.create_oval(coord, fill='white')
        "globe occulaire"
        coord = xf + ecartf_murx + ecartfeye_f + nfeye + (tfeye - tgo) / 2, yf + ecartf_mury + tcf + tgo - tfeye / 2, xf + ecartf_murx + ecartfeye_f + nfeye + tgo / 2 + tfeye / 2, yf + ecartf_mury + tcf + tgo*2 - tfeye /2
        Liste_fantome[k + 7 + 12 * dfg] = canvas.create_oval(coord, fill=Liste_globe_oculaire_fantome[0], outline=Liste_globe_oculaire_fantome[4])
        nfeye += tfeye + ecartfeye_eye

    "bouche"
    for k in range(3):
        start = (k % 2) * 180
        coord = xf + ecartf_murx + ecart_fantome_bouche, yf + ecartf_mury - tbouche / 2 + tcf + ybouche, xf + ecartf_murx + ecart_fantome_bouche + tbouche, yf + ecartf_mury + tbouche + tcf + ybouche
        Liste_fantome[k + 9 + 12 * dfg] = canvas.create_arc(coord, outline=Liste_couleur_corps_fantome[dfg], width=1, extent=180, start=start)
        ecart_fantome_bouche = ecart_fantome_bouche + tbouche

    deplacement_yeux(Liste_fantome[dfg*12:(dfg+1)*12], direction, (tfeye - tgo) / 2, 0)

    return Liste_fantome, ecartf_murx, ecartf_mury, diametre_cape, (tfeye - tgo) / 2, Liste_couleur_corps_fantome, Liste_globe_oculaire_fantome

def creation_pacman(xpm, ypm, couleur_pacman, couleur_oeil_pacman):

    ob = 359
    md, mb, mg, mh = 0, 1, 0, 1

    ecartpm_mur, tpmc, ecartpmeye, teye, Liste_pacman = creation_pacman_annexe(xpm, ypm, ob, couleur_pacman, couleur_oeil_pacman, 0, 0)

    return Liste_pacman, ecartpm_mur, ecartpmeye, tpmc, teye, [md, mb, mg, mh], ob

def creation_pacman_annexe(xpm, ypm, ob, couleur_pacman, couleur_oeil_pacman, start, bonus):

    Liste_dtpmtpmc = [tpm * (2 / 5), tpm / 4]
    ecartpm_mur = Liste_dtpmtpmc[bonus] / 2
    tpmc = tpm - Liste_dtpmtpmc[bonus]
    ecartpmeye = tpmc / 5
    teye = [tpmc / 6, tpmc / 4]

    coordpm = xpm + ecartpm_mur, ypm + ecartpm_mur, xpm + tpmc + ecartpm_mur, ypm + tpmc + ecartpm_mur
    coordpmeye = xpm + ecartpmeye + ecartpm_mur, ypm + ecartpmeye + ecartpm_mur, xpm + ecartpmeye + teye[bonus] + ecartpm_mur, ypm + ecartpmeye + teye[bonus] + ecartpm_mur

    Liste_pacman = [canvas.create_arc(coordpm, fill=couleur_pacman, extent=ob, start=start)]
    Liste_pacman += [canvas.create_arc(coordpmeye, fill=couleur_oeil_pacman, extent=ob, start=start)]

    return ecartpm_mur, tpmc, ecartpmeye, teye, Liste_pacman

def deplacement(Liste_corps, coord, sens, vitesse):

    if coord >= tpm * (Liste_dimension[sens % 2] - 0.5):
        "bord droite ou bas"
        coord = deplacement_annexe(Liste_corps, coord, sens + 2, tpm * Liste_dimension[sens % 2] - vitesse)
    elif coord <= -tpm / 2:
        "bord gauche ou haut"
        coord = deplacement_annexe(Liste_corps, coord, sens + 2, tpm * Liste_dimension[sens % 2] - vitesse)
    else:
        "normal"
        coord = deplacement_annexe(Liste_corps, coord, sens, vitesse)

    return coord

def deplacement_annexe(Liste_corps, coord, sens, distance):

    coord += distance * (-1) ** (sens // 2)

    for k in Liste_corps:
        "lorsque sens est paire, on se déplace sur x"
        if sens%2 == 0:
            canvas.move(k, distance * (-1) ** (sens//2), 0)
        else:
            canvas.move(k, 0, distance * (-1) ** (sens // 2))

    return coord

def direction_aleatoire(Liste_obstacle, direction_demi_tour):

    Liste = []

    for index in range(4):
        if index == direction_demi_tour:
            Liste += [index]
        elif Liste_obstacle[index] == 0:
            Liste += [index]*10

    return Sacha_random(Liste)

def deplacement_minuteur(position, temps_minuteur, Liste_minuteur, temps):

    "ancien"
    for ligne in Liste_minuteur[1 + position * 10 + int(('00' + str(int(temps_minuteur)))[-3 + position])]:
        canvas.move(ligne, 0, -5 * tpm)

    "nouveau"
    for ligne in Liste_minuteur[1 + position * 10 + int(('00' + str(int(temps_minuteur + temps / 1000)))[-3 + position])]:
        canvas.move(ligne, 0, 5 * tpm)

    return temps_minuteur, Liste_minuteur

def deplacement_oeil(corps_oeil, sens, distance, k):
    "k=0 aller vers la bonne position, k=1 retour en haut à droite du pacman"

    if sens == 3:
        canvas.move(corps_oeil, 0, distance*(-1)**k)
    elif sens > 0:
        canvas.move(corps_oeil, distance*(-1)**k, 0)

def deplacement_yeux(Liste_fantome, sens, distance, k):
    "k=0 aller vers la bonne position, k=1 retour au millieu de l'oeil"

    for p in range(2):
        if sens % 2 == 0:
            canvas.move(Liste_fantome[p + 7], distance * (-1) ** ((sens + k * 2) // 2), 0)
        else:
            canvas.move(Liste_fantome[p + 7], 0, distance * (-1) ** ((sens + k * 2) // 2))

def inverser_direction(direction):
    "direction : 0, 1, 2, 3"

    return (direction+2)%4

def La_sonde(Liste_mur_rouge, Big_data_figure, Liste_dimension):

    "xs, ys, direction retour"
    Liste_avancement = [Liste_mur_rouge[0], Liste_mur_rouge[1], 1]

    "[0] * nombre de cases en x * nombre de cases en y"
    Liste_sonde = [0] * Liste_dimension[0] * Liste_dimension[1]
    "mur rouge marque"
    Liste_sonde[Liste_avancement[1] * Liste_dimension[0] + Liste_avancement[0]] = 2

    while Liste_avancement != []:

        "Liste_avancement[2] est la direction demi tour qu'il faut éviter"
        for direction in suppr([0, 1, 2, 3], Liste_avancement[2]):

            "xs + 1, ys + 1, xs - 1, ys - 1"
            coord_sonde = Liste_avancement[:2]
            coord_sonde[direction % 2] += (-1) ** (direction // 2)

            "les bords"
            if coord_sonde[direction%2] == Liste_dimension[direction%2]:
                coord_sonde[direction%2] = 0
            elif coord_sonde[direction%2] == -1:
                coord_sonde[direction%2] = Liste_dimension[direction%2] - 1

            "les coordonnées apppartient-elles à un mur et est-ce qu'on est déjà passé par là ?"
            if Big_data_figure[coord_sonde[1] * Liste_dimension[0] + coord_sonde[0]] != 2 and Liste_sonde[coord_sonde[1] * Liste_dimension[0] + coord_sonde[0]] == 0:

                Liste_avancement += coord_sonde + [inverser_direction(direction)]
                "NE PAS ENLEVER LE PLUS + 1, pour une question de visibilité, de lecture de liste"
                Liste_sonde[coord_sonde[1] * Liste_dimension[0] + coord_sonde[0]] = inverser_direction(direction) + 1

                if False:
                    coord = coord_sonde[0] * tpm + 10, coord_sonde[1] * tpm + 10, coord_sonde[0] * tpm + 20, coord_sonde[1] * tpm + 20
                    canvas.create_rectangle(coord, fill='red')
                    canvas.update()
                    sleep(1)

        Liste_avancement = Liste_avancement[3:]

    return Liste_sonde

def retour_au_bercaille(xf, yf, Liste_sonde):

    return Liste_sonde[int((yf//tpm)*Liste_dimension[0] + xf//tpm)]%10 - 1