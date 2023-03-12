from time import time, sleep
from Sacha_texte import *
from Sacha_fonction import *

commande = []
n_commande = 19
corps_bouton_zone = -1
coord_zone = 'inexistant banane'
activation_check = -1
"corps barre, Liste texte"
numero_saisie_texte_activer = -1
Fonction_appuye = []
Fonction_relache = []
saisie_texte_variable = -1

#window = Tk()
#canvas = Canvas(window, width=800, height=800, bg='black')
#canvas.pack()

def appuyer(event):
    global x_souris_initial, y_souris_initial, activation_check, coord_zone, saisie_texte_variable

    touche_event = event.keysym
    x_souris, y_souris = event.x, event.y

    if saisie_texte_variable != -1:
        commande_saisie_texte(touche_event)

    "fonction à bouton"
    for k in range(int(len(commande)/n_commande)):
        if k >= int(len(commande) / n_commande):
            break
        Liste = commande[k*n_commande:(k+1)*n_commande]
        command, touche, x, y, longueur, corps_bouton, couleur, changement_couleur_activation, temps_changement_couleur_activation, appuyer_relacher_maintenu, largueur, touche_annexe, bouton, temps_repetition_commande, sens, condition_fonction, condition_valeur, information = Liste[0], Liste[1], Liste[2], Liste[3], Liste[4], Liste[5], Liste[6], Liste[7], Liste[8], Liste[9], Liste[10], Liste[11], Liste[12], Liste[13], Liste[14], Liste[15], Liste[16], Liste[18]

        if touche_event == touche and x_souris > x and y_souris > y and x_souris < x + longueur and y_souris < y + largueur and condition_fonction() == condition_valeur:
            if bouton == zone:
                x_souris_initial, y_souris_initial = x_souris, y_souris
            else:
                enclenchement(k, Liste, 0)
                if appuyer_relacher_maintenu != 2:
                    event_activation(k, Liste)
                else:
                    activation_check = k

    "fonction sans bouton"
    k = 0

    while k < len(Fonction_appuye):
        if Fonction_appuye[k] == touche_event or Fonction_appuye[k] == 'all':
            Fonction_appuye[k+1](x_souris, y_souris, touche_event, [coord_zone, corps_bouton_zone])

        k += 2

    #if coord_zone != 'inexistant banane':
        #canvas.delete(corps_bouton_zone)
        #coord_zone = 'inexistant banane'

def relacher(event):
    global fin, coord_zone, corps_bouton_zone, activation_check, commande, saisie_texte_variable

    touche_event = event.keysym
    x_souris, y_souris = event.x, event.y
    fin = 1

    for k in range(int(len(commande) / n_commande)):
        if k >= int(len(commande) / n_commande):
            break
        Liste = commande[k * n_commande:(k + 1) * n_commande]
        command, touche, x, y, longueur, corps_bouton, couleur, changement_couleur_activation, temps_changement_couleur_activation, appuyer_relacher_maintenu, largueur, touche_annexe, bouton, temps_repetition_commande, sens, condition_annexe, condition_associe, fonction_recadrage_zone, information = Liste[0], Liste[1], Liste[2], Liste[3], Liste[4], Liste[5], Liste[6], Liste[7], Liste[8], Liste[9], Liste[10], Liste[11], Liste[12], Liste[13], Liste[14], Liste[15], Liste[16], Liste[17], Liste[18]
        if touche_event == touche and x_souris > x and y_souris > y and x_souris < x + longueur and y_souris < y + largueur and condition_annexe() == condition_associe:
            if appuyer_relacher_maintenu == 2 and activation_check == k:
                event_activation(k, Liste)
                activation_check = -1
            elif bouton == zone:

                canvas.delete(corps_bouton_zone)

                coord_zone = fonction_recadrage_zone([x_souris_initial, y_souris_initial, x_souris, y_souris])
                corps_bouton_zone = canvas.create_rectangle(coord_zone, outline=couleur, width=information)
                #canvas.update()

        elif appuyer_relacher_maintenu == 2 and activation_check == k:
            enclenchement(k, Liste, 1)

    activation_check = -1

    if saisie_texte_variable != -1 and touche_event == '??':
        if saisie_texte_variable[-1] == -1:
            "si on vient d'appuyer sur la saisie"
            saisie_texte_variable = saisie_texte_variable[:-1]
        else:
            "supprimer la saisie"
            commande[saisie_texte_variable[1] * n_commande + 18] = ''
            saisie_texte_variable = -1

    k = 0
    while k < len(Fonction_relache):
        if Fonction_relache[k] == touche_event or Fonction_relache[k] == 'all':
            Fonction_relache[k+1](x_souris, y_souris, touche_event, [coord_zone, corps_bouton_zone])

        k += 2

def event_activation(k, Liste):
    global fin, activation_check

    command, touche, x, y, longueur, corps_bouton, couleur, changement_couleur_activation, temps_changement_couleur_activation, appuyer_relacher_maintenu, largueur, touche_annexe, bouton, temps_repetition_commande, sens, condition_annexe, condition_associe, information = Liste[0], Liste[1], Liste[2], Liste[3], Liste[4], Liste[5], Liste[6], Liste[7], Liste[8], Liste[9], Liste[10], Liste[11], Liste[12], Liste[13], Liste[14], Liste[15], Liste[16], Liste[18]

    "maintenu"
    if appuyer_relacher_maintenu == 3:
        fin = 0
        while fin == 0:
            canvas.after(temps_repetition_commande, command(commande, k, n_commande, [coord_zone, corps_bouton_zone]))

            canvas.update()

            "le programme bug sans ce petit rajout qui n'a aucun sens, qui n'a pas de réel but"
            l = canvas.create_oval(-5, -3, -4, -6)
            canvas.delete(l)
    else:
        canvas.after(temps_changement_couleur_activation, command(commande, k, n_commande, [coord_zone, corps_bouton_zone]))

    enclenchement(k, Liste, 1)

def enclenchement(k, Liste, direction):

    "direction signifie si c'est l'activation du bouton ou la fin de son activation"
    "0 signifie activation, 1..."
    command, touche, x, y, longueur, corps_bouton, couleur, changement_couleur_activation, temps_changement_couleur_activation, appuyer_relacher_maintenu, largueur, touche_annexe, bouton, temps_repetition_commande, sens, condition_annexe, condition_associe, information = Liste[0], Liste[1], Liste[2], Liste[3], Liste[4], Liste[5], Liste[6], Liste[7], Liste[8], Liste[9], Liste[10], Liste[11], Liste[12], Liste[13], Liste[14], Liste[15], Liste[16], Liste[17]

    for l in range(len(corps_bouton)):
        if bouton == text:
            if l != 0:
                canvas.move(corps_bouton[l], 1 * (-1) ** direction, 1 * (-1) ** direction)
        elif changement_couleur_activation != 'pas de changement couleur':
            canvas.itemconfigure(corps_bouton[l], fill=commande[k * n_commande + 7 - direction])

    canvas.update()

def event_en_tout_genre(canvas):

    canvas.focus_set()
    canvas.bind('<KeyPress>', appuyer)
    canvas.bind("<Button-1>", appuyer)
    canvas.bind("<KeyRelease>", relacher)
    canvas.bind("<ButtonRelease-1>", relacher)

def plus(*parametres):

    x, y, largueur, longueur, epaiseur = parametres[1], parametres[2], parametres[3], parametres[4], parametres[5]

    corps_bouton = [0]*2
    for k in range(2):
        coord = x + (longueur/2)*k, y + (largueur/2)*(1-k), x + longueur - (longueur/2)*k, y + largueur/2 + (largueur/2)*k
        corps_bouton[k] = canvas.create_line(coord, width=epaiseur)

    return corps_bouton, 0, len(corps_bouton), longueur

def moins(*parametres):

    sens, x, y, largueur, longueur, epaiseur, couleur = parametres[0]%2, parametres[1], parametres[2], parametres[3], parametres[4], parametres[5], parametres[6]

    coord = x + (longueur/2)*sens, y + (largueur/2)*(1-sens), x + longueur - (longueur/2)*sens, y + largueur/2 + (largueur/2)*sens
    corps_bouton = [canvas.create_line(coord, width=epaiseur)]

    return corps_bouton, 0, len(corps_bouton), longueur

def oval(*parametres):

    x, y, largeur, longueur, epaiseur, couleur = parametres[1], parametres[2], parametres[3], parametres[4], parametres[5], parametres[6]

    coord = x, y, x + longueur, y + largeur
    corps_bouton = [canvas.create_oval(coord, width=epaiseur)]

    return corps_bouton, 0, len(corps_bouton), longueur

def fleche(*parametres):

    sens, x, y, largeur, longueur, epaiseur = parametres[0]%4, parametres[1], parametres[2], parametres[3], parametres[4], parametres[5]

    "sens : 0, 1, 2, 3 --> droite, bas, gauche, haut"
    coord = [(x + (1 - abs(1-(sens+1)//2))*longueur, y + (abs(1-(sens+1)//2))*largeur), (x + (sens//2)*longueur, y + (sens//2)*largeur), (x + (abs(2 - sens)/2)*longueur, y + (1 - abs(1-sens)/2)*largeur)]
    corps_bouton = [canvas.create_polygon(coord, width=epaiseur)]

    return corps_bouton, 0, len(corps_bouton), longueur

def pause(*parametres):

    x, y, largeur, longueur, epaiseur = parametres[1], parametres[2], parametres[3], parametres[4], parametres[5]

    corps_bouton = []
    for k in range(2):
        coord = x + 0.5*epaiseur*(-1)**k + longueur*k, y, x + 0.5*epaiseur*(-1)**k + longueur*k, y + largeur
        corps_bouton.append(canvas.create_line(coord, width=epaiseur))

    return corps_bouton, 0, len(corps_bouton), longueur

def text(*parametres):

    x, y, largueur, epaiseur, texte, couleur_texte = parametres[1], parametres[2], parametres[3], parametres[5], parametres[7], parametres[8]

    longueur = calcul_de_taille_texte(texte, largueur - epaiseur*4)

    coord = x, y, x + longueur + epaiseur, y + largueur

    corps_bouton = enfoncement(coord)
    corps_bouton += [canvas.create_rectangle(coord)]
    corps_bouton += Sacha_texte(canvas=canvas, xt=x+epaiseur*2, yt=y+epaiseur*2, largueur=largueur - epaiseur*4, epaiseur_texte=epaiseur, texte=texte, couleur=couleur_texte)

    return corps_bouton, 1, 2, longueur

def enfoncement(coord):

    coord_enfoncement = coord[0], coord[1], coord[2] + 1, coord[3] + 1
    corps_bouton = [canvas.create_rectangle(coord_enfoncement, outline='grey', width=1)]

    return corps_bouton

def spinbox(*parametres):

    x, y, largueur, epaiseur, Liste_texte, couleur_texte, information, couleur_annexe = parametres[1], parametres[2], parametres[3], parametres[5], parametres[7], parametres[8], parametres[9], parametres[10]

    largueur_texte = largueur - epaiseur*2

    longueur = 0
    "la longueur égale à la longueur du texte le plus grand"
    for texte in Liste_texte:
        longueur_texte = calcul_de_taille_texte(texte, largueur_texte)
        if longueur < longueur_texte + epaiseur + largueur*2:
            "epaiseur pour les bords, 2*largueur pour les deux flêches"
            longueur = longueur_texte + epaiseur + largueur*2

    "petite case des flêches"
    coord = x + longueur - 2 * largueur, y, x + longueur, y + largueur
    corps_bouton = [canvas.create_rectangle(coord, width=0, fill=couleur_annexe, outline='pink')]

    ecart = 0.15
    for k in range(2):
        "flêches"
        corps, rien, rien, rien = fleche(k * 2, x + longueur + largueur * (ecart - k - 1), y + largueur * ecart, largueur * (1 - ecart * 2), largueur * (1 - ecart * 2), epaiseur)
        corps_bouton += corps

    "case où sont affichés les textes"
    coord = x, y, x + longueur - 2*largueur, y + largueur
    corps_bouton += [canvas.create_rectangle(coord, width=0, fill=couleur_annexe)]

    "texte"
    corps_bouton += Sacha_texte(canvas=canvas, xt=x + epaiseur + longueur/2 - largueur, yt=y+epaiseur*1, largueur=largueur_texte - epaiseur, epaiseur_texte=epaiseur, texte=Liste_texte[information], couleur=couleur_texte, centrer=1)

    return corps_bouton, 1, 3, longueur

def commande_spinbox(*parametres):

    commande, k, n_commande = parametres[0], parametres[1], parametres[2]

    y, largueur, Liste_informations = commande[k*n_commande + 3], commande[k*n_commande + 10], commande[k*n_commande + 18]
    sens = Liste_informations[0]

    if sens == 2:
        k += 1

    Liste_informations = commande[k*n_commande + 18]
    command, corps_bouton, information, Liste_texte, epaiseur, couleur_texte = Liste_informations[1], Liste_informations[2], Liste_informations[3], Liste_informations[4], Liste_informations[5], Liste_informations[6]
    longueur = canvas.coords(corps_bouton[0])[2] - canvas.coords(corps_bouton[0])[0]

    information = (information + (-1)**(sens//2))%len(Liste_texte)

    effacage_texte(corps_bouton[1:])
    corps_texte = Sacha_texte(canvas=canvas, xt=canvas.coords(corps_bouton[0])[0] + epaiseur + longueur/2, yt=y + epaiseur, largueur=largueur - epaiseur * 3, epaiseur_texte=epaiseur, texte=Liste_texte[information], couleur=couleur_texte, centrer=1)

    commande[k*n_commande + 18] = [0, command, [corps_bouton[0]] + corps_texte, information, Liste_texte, epaiseur, couleur_texte]

    try:
        command(int(Liste_texte[information]))
    except:
        command(information)


def saisie_texte(*parametres):

    x, y, largueur, longueur, epaiseur, couleur_texte, couleur_annexe = parametres[1], parametres[2], parametres[3], parametres[4], parametres[5], parametres[8], parametres[10]

    if longueur < largueur:
        print("saisie texte : la longueur doit être supérieur à la longueur")

    "case où l'on écrit"
    coord = x, y, x + longueur - largueur, y + largueur
    corps_bouton = [canvas.create_rectangle(coord, width=epaiseur, fill='white')]

    "case cadena"
    coord = x + longueur - largueur, y + 2, x + longueur, y + largueur - 2
    corps_bouton += [canvas.create_rectangle(coord, width=epaiseur, outline='white')]

    "carre du cadena"
    coord = x + longueur - largueur*0.8, y + largueur*0.3, x + longueur - largueur*0.2, y + largueur*0.9
    corps_bouton += [canvas.create_rectangle(coord, width=epaiseur, fill='white')]

    "boucle du cadena"
    coord = x + longueur - largueur * 0.7, y + largueur * 0.1, x + longueur - largueur * 0.35, y + largueur * 0.55
    corps_bouton += [canvas.create_oval(coord, width=epaiseur, outline='white')]

    return corps_bouton, 0, 0, longueur

def activation_saisie_texte(com, k, n_commande, *parametres):
    global commande, numero_saisie_texte_activer

    Liste = com[k*n_commande:(k+1)*n_commande]
    x, y, largueur = Liste[2], Liste[3], Liste[10]

    ecart = 3
    coord = x + ecart, y + ecart / 2, x + ecart, y + largueur - ecart
    "-1 pour préciser qu'il vient d'être créer"
    commande[k*n_commande + 18] = [canvas.create_line(coord, fill='black'), '']

    numero_saisie_texte_activer = k

    canvas.update()

def commande_saisie_texte(x_souris, y_souris, touche_event, *parametres):
    global saisie_texte_variable, commande

    Liste_caractere, rien = définir_Liste_caractere()
    barre = saisie_texte_variable[0]

    largueur_texte = (canvas.coords(barre)[3] - canvas.coords(barre)[1]) * 0.75

    #if

    if touche_event == '??':
        "tout effaçer"
        canvas.delete(barre)
        for k in range(2, len(saisie_texte_variable)):
            corps_lettre = saisie_texte_variable[k]
            effacage_texte(corps_lettre)

    elif touche_event == 'BackSpace':
        "effacer un caractère"
        Liste_lettre = commande[saisie_texte_variable[1] * n_commande + 18]
        canvas.move(barre, -calcul_de_taille_texte(Liste_lettre[-1], largueur_texte), 0)

        effacage_texte(saisie_texte_variable[-1])
        saisie_texte_variable = saisie_texte_variable[:-1]
        commande[saisie_texte_variable[1] * n_commande + 18] = Liste_lettre[:-1]

    elif touche_event in Liste_caractere:
        "ecrire un caractère"
        epaiseur_texte = largueur_texte * 0.2
        commande[saisie_texte_variable[1] * n_commande + 18] += touche_event
        saisie_texte_variable += [Sacha_texte(canvas=canvas, xt=canvas.coords(barre)[0], yt=canvas.coords(barre)[1] + epaiseur_texte, texte=touche_event, largueur=largueur_texte, couleur='black', epaiseur_texte=epaiseur_texte)]

        canvas.move(barre, calcul_de_taille_texte(touche_event, largueur_texte), 0)

def zone(*parametres):
    global appuyer_relacher_maintenu

    x, y, largueur, longueur, epaiseur = parametres[1], parametres[2], parametres[3], parametres[4], parametres[5]

    appuyer_relacher_maintenu = 4

    coord = x, y, x + longueur, y + largueur
    corps_bouton = [canvas.create_rectangle(coord, width=epaiseur)]

    return corps_bouton, 0, len(corps_bouton), longueur

def Sacha_bouton(**parametres):
    global commande, canvas, appuyer_relacher_maintenu

    Liste_options = ['canvas', 0, 'x', 50, 'y', 50, 'longueur', 60, 'largueur', 60, 'epaiseur', 2, 'couleur', 'pas de couleur', 'touche', '??', 'commande', avertissement, 'changement_couleur_activation', 'pas de changement couleur', 'temps_changement_couleur_activation', 200, 'sens', 0, 'appuyer_relacher_maintenu', 2, 'carre', 0, 'touche_annexe', 'a', 'bouton', plus, 'epaiseur_annexe', 1, 'epaiseur_texte', 8, 'texte', 'texte', 'taille_texte', 20, 'temps_repetition_commande', 200, 'couleur_outline', 'pas de couleur', 'condition_fonction', valeur_commande_annexe, 'condition_valeur', 0, 'centrer', 0, 'couleur_texte', 'pink', 'information', 0, 'couleur_annexe', 'black', 'fonction_recadrage_zone', fonction_recadrage_zone_par_default]
    Listes_options_valeurs = attribution_variables(Liste_options, parametres)

    canvas, x, y, longueur, largeur, epaiseur, couleur, touche, command, changement_couleur_activation, temps_changement_couleur_activation, sens, appuyer_relacher_maintenu, carre, touche_annexe, bouton, epaiseur_annexe, epaiseur_texte, texte, taille_texte, temps_repetition_commande, couleur_outline, condition_fonction, condition_valeur, centrer, couleur_texte, information, couleur_annxe, fonction_recadrage_zone = Listes_options_valeurs[0], Listes_options_valeurs[1], Listes_options_valeurs[2], Listes_options_valeurs[3], Listes_options_valeurs[4], Listes_options_valeurs[5], Listes_options_valeurs[6], Listes_options_valeurs[7], Listes_options_valeurs[8], Listes_options_valeurs[9], Listes_options_valeurs[10], Listes_options_valeurs[11], Listes_options_valeurs[12], Listes_options_valeurs[13], Listes_options_valeurs[14], Listes_options_valeurs[15], Listes_options_valeurs[16], Listes_options_valeurs[17], Listes_options_valeurs[18], Listes_options_valeurs[19], Listes_options_valeurs[20], Listes_options_valeurs[21], Listes_options_valeurs[22], Listes_options_valeurs[23], Listes_options_valeurs[24], Listes_options_valeurs[25], Listes_options_valeurs[26], Listes_options_valeurs[27], Listes_options_valeurs[28]

    event_en_tout_genre(canvas)

    if appuyer_relacher_maintenu > 3:
        appuyer_relacher_maintenu = 1

    if carre != 0:
        largeur = longueur

    corps_bouton, debut, fin, longueur = bouton(sens, x, y, largeur, longueur, epaiseur, couleur, texte, couleur_texte, information, couleur_annxe)

    if centrer == 1:
        for k in corps_bouton:
            #canvas.move(k, -(canvas.coords(corps_bouton[0])[2]-canvas.coords(corps_bouton[0])[0])/2, 0)
            canvas.move(k, -longueur / 2, 0)
        x += -longueur / 2

    if couleur_outline != 'pas de couleur':
        for k in corps_bouton[debut:fin]:
            canvas.itemconfigure(k, outline=couleur_outline)

    if couleur != 'pas de couleur':
        for k in corps_bouton[debut:fin]:
            canvas.itemconfigure(k, fill=couleur)
    elif changement_couleur_activation != 'pas de changement couleur':
        print("probleme pour le bouton", bouton, ": s'il y a un changement de couleur, alors tu dois définir la couleur")

    if bouton == zone:
        couleur = couleur_outline

    if bouton == saisie_texte:
        repetition = 2
        Liste_rajout = ['x', x + longueur - largeur, 'y', y, 'longueur', largeur, 'largueur', largeur, 'command', command, 'corps_bouton', corps_bouton[1:], 'bouton', text, 'information', 'rien']
        longueur, command, corps_bouton, information = longueur - largeur, activation_saisie_texte, [corps_bouton[0]], []

        rajout_fonction(['appuyer', 'relache'][appuyer_relacher_maintenu-1], 'all', commande_saisie_texte)

    elif bouton == spinbox:
        repetition = 2
        Liste_rajout = ['x', x + longueur - largeur, 'y', y, 'longueur', largeur, 'largueur', largeur, 'command', commande_spinbox, 'corps_bouton', [corps_bouton[1]], 'bouton', spinbox, 'information', [0, command, corps_bouton[3:], information, texte, epaiseur, couleur_texte]]
        x, longueur, command, corps_bouton, information = x + longueur - 2*largeur, largeur, commande_spinbox, [corps_bouton[2]], [2]

    else:
        repetition = 1

    for k in range(repetition):
        commande = commande + [command, touche, x, y, longueur, corps_bouton, couleur, changement_couleur_activation, temps_changement_couleur_activation, appuyer_relacher_maintenu, largeur, touche_annexe, bouton, temps_repetition_commande, sens, condition_fonction, condition_valeur, fonction_recadrage_zone, information]
        try:
            x, y, longueur, largueur, command, corps_bouton, bouton, information = Liste_rajout[1], Liste_rajout[3], Liste_rajout[5], Liste_rajout[7], Liste_rajout[9], Liste_rajout[11], Liste_rajout[13], Liste_rajout[15]
        except:
            break

    return corps_bouton

def rajout_fonction(fonction, *parametres):
    global Fonction_appuye, Fonction_relache

    if fonction != 'appuyer' and fonction != 'relacher':
        print('précise tout d abord appuyer ou relacher')

    elif len(parametres)%2 == 1:
        print('il faut à chaque fois préciser la touche et la fonction')

    else:
        for k in range(int(len(parametres)/2)):
            if type(parametres[k*2]) != str:
                print(k, 'il faut à chaque fois préciser la touche puis une fonction, ainsi de suite')

        if fonction == 'appuyer':

            for k in range(int(len(parametres)/2)):
                Fonction_appuye += [parametres[k*2]]
                Fonction_appuye += [parametres[k*2+1]]

        else:

            for k in range(int(len(parametres)/2)):
                Fonction_relache += [parametres[k*2]]
                Fonction_relache += [parametres[k*2+1]]

def options_bouton():

    print('bouton plus :', 'canvas, x, y, taille, largueur, couleur, touche, command, changement_couleur_activation, temps_changement_couleur_activation')
    print('bouton moins :', 'canvas, x, y, taille, largueur, couleur, touche, command, changement_couleur_activation, temps_changement_couleur_activation, sens')

def valeur_commande_annexe():

    return 0

def fonction_recadrage_zone_par_default(*parametres):

    return parametres[0]

def avertissement(*parametres):

    print('définie une commande loustique')

def ko(*parametres):
    print('I DID IT')

def dimension_zone(*parametres):
    global relation_bouton_zone

    relation_bouton_zone = 1
    print('dimension', coord_zone)

def transfert(commande, k, n_commande, *parametres):

    effacer_bouton('all')
    canvas.delete('all')

    "information"
    commande[k * n_commande + 18](commande, k, n_commande, *parametres)

def effacer_bouton(*k):
    global commande, bouton_zone, Fonction_appuye, activation_check

    'without puis k'

    if 'all' in k or 'without' in k:
        for l in range(int(len(commande)/n_commande)):
            Liste_corps_bouton = commande[l * n_commande + 5]
            for corps_bouton in Liste_corps_bouton:
                canvas.delete(corps_bouton)

        if 'without' in k:
            "k[k.index('without')+1]    =     le k de k*n_commande"
            commande = commande[k[k.index('without')+1]*n_commande : (k[k.index('without')+1] + 1)*n_commande]
        else:
            activation_check = -1

        commande = []
        Fonction_appuye = []
    else:
        for l in k:
            Liste_corps_bouton = commande[l * n_commande + 5]
            for corps_bouton in Liste_corps_bouton:
                canvas.delete(corps_bouton)

            commande = commande[:l*n_commande] + commande[(l+1)*n_commande:]


#Sacha_bouton(canvas=canvas)
#Sacha_bouton(canvas=canvas, bouton=zone, x=200, y=200, longueur=200, carre=1)

#window.mainloop()