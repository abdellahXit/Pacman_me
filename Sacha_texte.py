from time import time, sleep

def définir_Liste_caractere():

    Liste_caractere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Liste_caractere = Liste_caractere + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Liste_caractere = Liste_caractere + [':', '.', ' ']


    Liste_fonction = [a, b, c, d, e, f, g, h, i, j, j, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    Liste_fonction += [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
    Liste_fonction += [deux_points, point, espace]

    return Liste_caractere, Liste_fonction

def options_texte():

    return ['canvas', 0, 'texte', 'texte', 'xt', 30, 'yt', 30, 'largueur', 20, 'epaiseur_texte', 4, 'couleur', 'red', 'couleur_changement', ['white'], 'repetition', 1, 'temps_changement_couleur', 1, 'centrer', 0]

def Sacha_texte(**parametres):
    global canvas

    Liste_options = options_texte()

    Listes_options_valeurs = attribution_variables(Liste_options, parametres)

    Liste_couleur = [0]
    canvas, texte_a_prendre, xt, yt, tecriture, Ltexte, Liste_couleur[0], repetition, temps, centrer = Listes_options_valeurs[0], Listes_options_valeurs[1], Listes_options_valeurs[2], Listes_options_valeurs[3], Listes_options_valeurs[4]/2, Listes_options_valeurs[5], Listes_options_valeurs[6], Listes_options_valeurs[8], Listes_options_valeurs[9], Listes_options_valeurs[10]
    Liste_couleur += Listes_options_valeurs[7]

    Liste_caractere, Liste_fonction = définir_Liste_caractere()

    Liste_texte = []
    k = 0
    place_lettre = 0

    while k != len(texte_a_prendre):

        Liste_lettre = Liste_fonction[Liste_caractere.index(texte_a_prendre[k])](tecriture, Ltexte)

        plusieurs_traits = 0
        while type(Liste_lettre[plusieurs_traits]) != type('str'):

            try:
                Liste_texte.append(canvas.create_arc(Liste_lettre[plusieurs_traits+2], outline=Liste_couleur[0], width=Ltexte, start=int(Liste_lettre[plusieurs_traits]), extent=int(Liste_lettre[plusieurs_traits+1])))
                plusieurs_traits += 2
            except:
                if Liste_lettre[plusieurs_traits] == -1:
                    Liste_texte.append(canvas.create_oval(Liste_lettre[plusieurs_traits+1], outline=Liste_couleur[0], width=Ltexte))
                    plusieurs_traits += 1
                else:
                    Liste_texte.append(canvas.create_line(Liste_lettre[plusieurs_traits], fill=Liste_couleur[0], width=Ltexte))

            canvas.move(Liste_texte[-1], xt + place_lettre*tecriture, yt)

            plusieurs_traits += 1

        #canvas.update()
            #sleep(0.2)

        place_lettre += float(Liste_lettre[-1])
        k += 1

    if centrer != 0:
        for k in Liste_texte:
            canvas.move(k, -place_lettre*tecriture/2, 0)

    for k in range(repetition-1):
        canvas.after(temps, changement_couleur_texte(Liste_texte, Liste_couleur, k))
        canvas.update()

    return Liste_texte

def changement_couleur_texte(Liste_texte, Liste_couleur, k):

    for l in range(len(Liste_texte)):
        try:
            canvas.itemconfigure(Liste_texte[l], outline =Liste_couleur[(k+1)%len(Liste_couleur)])
        except:
            canvas.itemconfigure(Liste_texte[l], fill=Liste_couleur[(k + 1) % len(Liste_couleur)])

def calcul_de_taille_texte(texte, largueur):

    Liste_caractere, Liste_fonction = définir_Liste_caractere()
    place_lettre = 0

    for k in texte:
        Liste_lettre = Liste_fonction[Liste_caractere.index(k)](largueur/2, 2)
        place_lettre += float(Liste_lettre[-1])

    return place_lettre*largueur/2

def effacage_texte(Liste_texte):

    for k in range(len(Liste_texte)):
        canvas.delete(Liste_texte[0])
        Liste_texte.pop(0)

def a(tecriture, Ltexte):

    coord_A1 = 0, 2.1 * tecriture, 1 * tecriture, 0
    coord_A2 = 2 * tecriture, 2.1 * tecriture, 1 * tecriture, 0
    coord_A3 = 0.4 * tecriture, 1.4 * tecriture, 1.6 * tecriture, 1.4 * tecriture

    return [coord_A1, coord_A2, coord_A3, '2.8']

def b(tecriture, Ltexte):

    coord_B1 = -1 * tecriture, 0 * tecriture, 1 * tecriture, 1 * tecriture
    coord_B2 = -1 * tecriture, 1 * tecriture, 1 * tecriture, 2 * tecriture

    return [270, 180, coord_B1, 270, 180, coord_B2, '2']

def c(tecriture, Ltexte):

    coord_C = 0 * tecriture, 0, 2 * tecriture, 2 * tecriture+0.01

    return [50, 260, coord_C, '2.3']

def d(tecriture, Ltexte):

    coord_D1 = 0 * tecriture, 0, 0 * tecriture, 2 * tecriture + Ltexte / 2.5
    coord_D2 = - 1.3 * tecriture, 0 * tecriture, 1.3 * tecriture, 2 * tecriture

    return [coord_D1, 270, 180, coord_D2, '2']

def e(tecriture, Ltexte):

    coord_E1 = 0 * tecriture, 0, 0 * tecriture, 2 * tecriture
    coord_E2 = 0 * tecriture - Ltexte*0.3, 0, 1.4 * tecriture, 0
    coord_E3 = 0 * tecriture, tecriture, 0.8 * tecriture, tecriture
    coord_E4 = 0 * tecriture - Ltexte*0.3, 2 * tecriture, 1.4 * tecriture, 2 * tecriture

    return [coord_E1, coord_E2, coord_E3, coord_E4, '2.2']

def f(tecriture, Ltexte):

    coord_F1 = 0 * tecriture, 0, 0 * tecriture, 2 * tecriture
    coord_F2 = 0 * tecriture - Ltexte / 2, 0, 1.4 * tecriture, 0
    coord_F3 = 0 * tecriture, tecriture, 0.8 * tecriture, tecriture

    return [coord_F1, coord_F2, coord_F3, '1.9']

def g(tecriture, Ltexte):

    coord_G1 = 0 * tecriture, 0.2 * tecriture, 0 * tecriture, 2 * tecriture
    coord_G2 = 0 * tecriture - Ltexte / 2, 0.1 * tecriture, 2 * tecriture, 0.1 * tecriture
    coord_G3 = 0 * tecriture - Ltexte / 2, 2 * tecriture, 2 * tecriture, 2 * tecriture
    coord_G4 = 2 * tecriture - Ltexte / 2, 1 * tecriture, 2 * tecriture - Ltexte / 2, 2 * tecriture
    coord_G5 = 0.8 * tecriture, 1.05 * tecriture, 2 * tecriture, 1.05 * tecriture

    return [coord_G1, coord_G2, coord_G3, coord_G4, coord_G5, '3']

def h(tecriture, Ltexte):

    coord_H1 = 0 * tecriture, 0 * tecriture - Ltexte/2, 0 * tecriture, 2 * tecriture + Ltexte/2
    coord_H2 = 0 * tecriture, 1 * tecriture, 1.5 * tecriture, 1 * tecriture
    coord_H3 = 1.5 * tecriture, 0 * tecriture - Ltexte/2, 1.5 * tecriture, 2 * tecriture + Ltexte/2

    return [coord_H1, coord_H2, coord_H3, '2.5']

def i(tecriture, Ltexte):

    coord_I = 0 * tecriture, - Ltexte / 2,  0 * tecriture, 2.2 * tecriture

    return [coord_I, '1.1']

def j(tecriture, Ltexte):

    coord_1 = 0 * tecriture, 0 * tecriture, 2.4 * tecriture, 0 * tecriture
    coord_2 = 1.2 * tecriture, 0 * tecriture, 1.2 * tecriture, 1.8 * tecriture

    coord_3 = 0.2 * tecriture, 1.6 * tecriture, 1.2 * tecriture, 2 * tecriture

    return [coord_1, coord_2, 180, 180, coord_3, '2.8']

def k(tecriture, Ltexte):

    return ['3']

def l(tecriture, Ltexte):

    coord_L1 = 0 * tecriture - Ltexte / 2, 2 * tecriture, 1.4 * tecriture, 2 * tecriture
    coord_L2 = 0 * tecriture, - Ltexte / 2, 0 * tecriture, 2 * tecriture

    return [coord_L1, coord_L2, '2.2']

def m(tecriture, Ltexte):

    coord_M1 = 0 * tecriture, 0, 0 * tecriture, 2 * tecriture + Ltexte / 2.5
    coord_M2 = 0 * tecriture, 0.05 * tecriture, 1 * tecriture, 1.2 * tecriture
    coord_M3 = 1.8 * tecriture, 0.05 * tecriture, 0.8 * tecriture, 1.2 * tecriture
    coord_M4 = 1.9 * tecriture, 0, 1.9 * tecriture, 2 * tecriture + Ltexte / 2.5

    return [coord_M1, coord_M2, coord_M3, coord_M4, '3']

def n(tecriture, Ltexte):

    coord_N1 = 0 * tecriture, 2.1 * tecriture, 0 * tecriture, 0
    coord_N2 = 0 * tecriture, 0.05 * tecriture, 1.8 * tecriture, 2.03 * tecriture
    coord_N3 = 1.8 * tecriture, 0 * tecriture, 1.8 * tecriture, 2.1 * tecriture

    return [coord_N1, coord_N2, coord_N3, '2.8']


def o(tecriture, Ltexte):

    coord_O = 0 * tecriture, 0, 2 * tecriture, 2 * tecriture

    return [-1, coord_O, '3']

def p(tecriture, Ltexte):

    coord_P1 = 0 * tecriture, 2.1 * tecriture, 0 * tecriture, - 0.05 * tecriture
    coord_P2 = - 0.9 * tecriture, - 0.05 * tecriture, 0.9 * tecriture, 1.2 * tecriture

    return [coord_P1, 270, 180, coord_P2, '1.8']

def q(tecriture, Ltexte):

    coord_Q1 = 0 * tecriture, 0, 2 * tecriture, 2 * tecriture
    coord_Q2 = 1.1 * tecriture, 1.1 * tecriture, 2.05 * tecriture, 2.05 * tecriture

    return [-1, coord_Q1, coord_Q2, '3']

def r(tecriture, Ltexte):

    coord_R1 = 0 * tecriture, 0, 0 * tecriture, 2 * tecriture + Ltexte / 2.5
    coord_R2 = - 0.9 * tecriture, 0, 1 * tecriture, 1.1 * tecriture
    coord_R3 = 0.5 * tecriture, 1.1 * tecriture, 1 * tecriture, 2 * tecriture + Ltexte / 2.5

    return [coord_R1, 270, 180, coord_R2, coord_R3, '2.1']

def s(tecriture, Ltexte):

    coord_S1 = 0 * tecriture, 0 * tecriture, 1.3 * tecriture, 0 * tecriture
    coord_S2 = 0 * tecriture, 0, 0 * tecriture, 1 * tecriture
    coord_S3 = 0 * tecriture, 1 * tecriture, 1.3 * tecriture, 1 * tecriture
    coord_S4 = 1.2 * tecriture, 1 * tecriture, 1.2 * tecriture, 2 * tecriture
    coord_S5 = 0 * tecriture, 2 * tecriture, 1.3 * tecriture, 2 * tecriture

    return [coord_S1, coord_S2, coord_S3, coord_S4, coord_S5, '2.5']

def t(tecriture, Ltexte):

    coord_T1 = 0 * tecriture, 0, 2 * tecriture, 0
    coord_T2 = 1 * tecriture, 0, 1 * tecriture, 2.2 * tecriture

    return [coord_T1, coord_T2, '2.7']

def u(tecriture, Ltexte):

    coord_U1 = 0 * tecriture, 0 * tecriture, 0 * tecriture, 2 * tecriture
    coord_U2 = 0 * tecriture, 1.8 * tecriture, 1.1 * tecriture, 2 * tecriture
    coord_U3 = 1.1 * tecriture, 0 * tecriture, 1.1 * tecriture, 2 * tecriture

    return [coord_U1, 180, 180, coord_U2, coord_U3, '2.3']

def v(tecriture, Ltexte):

    coord_V1 = 0 * tecriture, - 0.1 * tecriture, 1 * tecriture, 2 * tecriture
    coord_V2 = 1 * tecriture, 2 * tecriture, 2 * tecriture, - 0.1 * tecriture

    return [coord_V1, coord_V2, '3']

def w(tecriture, Ltexte):

    return ['3']

def x(tecriture, Ltexte):

    coord_X1 = 0 * tecriture, 0, 2 * tecriture, 2 * tecriture
    coord_X2 = 2 * tecriture, 0, 0 * tecriture, 2 * tecriture

    return [coord_X1, coord_X2, '2.8']

def y(tecriture, Ltexte):

    coord_Y1 = 0 * tecriture, 0, 0.8 * tecriture, tecriture
    coord_Y2 = 0.8 * tecriture, tecriture, 0.8 * tecriture, 2 * tecriture
    coord_Y3 = 0.8 * tecriture, tecriture, 1.6 * tecriture, 0

    return [coord_Y1, coord_Y2, coord_Y3, '2.5']

def z(tecriture, Ltexte):

    coord_Z1 = 0 * tecriture, 0, 2 * tecriture, 0
    coord_Z2 = 2 * tecriture, 0, 0 * tecriture, 2 * tecriture
    coord_Z3 = 0 * tecriture, 2 * tecriture, 2 * tecriture, 2 * tecriture

    return [coord_Z1, coord_Z2, coord_Z3, '3']

def c0(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte),bibliothèque_h(tecriture, Ltexte), bibliothèque_g(tecriture, Ltexte)] + c1(tecriture, Ltexte)

def c1(tecriture, Ltexte):

    coord_1 = 1 * tecriture, 0, 1 * tecriture, 2 * tecriture

    return [coord_1, '2']

def c2(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte), bibliothèque_c(tecriture, Ltexte), bibliothèque_f(tecriture, Ltexte), bibliothèque_b(tecriture, Ltexte), bibliothèque_g(tecriture, Ltexte), '2']

def c3(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte), bibliothèque_f(tecriture, Ltexte), bibliothèque_g(tecriture, Ltexte)] + c1(tecriture, Ltexte)

def c4(tecriture, Ltexte):

    return [bibliothèque_a(tecriture, Ltexte), bibliothèque_f(tecriture, Ltexte)] + c1(tecriture, Ltexte)

def c5(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte), bibliothèque_a(tecriture, Ltexte), bibliothèque_f(tecriture, Ltexte), bibliothèque_d(tecriture, Ltexte), bibliothèque_g(tecriture, Ltexte), '2']

def c6(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte), bibliothèque_h(tecriture, Ltexte), bibliothèque_f(tecriture, Ltexte), bibliothèque_d(tecriture, Ltexte), bibliothèque_g(tecriture, Ltexte), '2']

def c7(tecriture, Ltexte):

    return [bibliothèque_e(tecriture, Ltexte)] + c1(tecriture, Ltexte)

def c8(tecriture, Ltexte):

    return [bibliothèque_h(tecriture, Ltexte)] + c3(tecriture, Ltexte)

def c9(tecriture, Ltexte):

    return [bibliothèque_a(tecriture, Ltexte)] + c3(tecriture, Ltexte)

def deux_points(tecriture, Ltexte):

    coord_deux_points_1 = 0 * tecriture, 0.8 * tecriture, 0 * tecriture, 1.2 * tecriture

    return [coord_deux_points_1] + point(tecriture, Ltexte)

def point(tecriture, Ltexte):

    coord_deux_points_2 = 0 * tecriture, 1.8 * tecriture, 0 * tecriture, 2.2 * tecriture

    return [coord_deux_points_2, '1']

def espace(tecriture, Ltexte):

    return ['1.8']

def bibliothèque_a(tecriture, Ltexte):

    return 0 * tecriture, 0, 0 * tecriture, 1 * tecriture

def bibliothèque_b(tecriture, Ltexte):

    return 0 * tecriture, 1 * tecriture, 0 * tecriture, 2 * tecriture

def bibliothèque_c(tecriture, Ltexte):

    return 1 * tecriture, 0, 1 * tecriture, 1 * tecriture

def bibliothèque_d(tecriture, Ltexte):

    return 1 * tecriture, 1 * tecriture, 1 * tecriture, 2 * tecriture

def bibliothèque_e(tecriture, Ltexte):

    return 0 * tecriture, 0 * tecriture, 1 * tecriture, 0 * tecriture

def bibliothèque_f(tecriture, Ltexte):

    return 0 * tecriture, 1 * tecriture, 1 * tecriture, 1 * tecriture

def bibliothèque_g(tecriture, Ltexte):

    return 0 * tecriture, 2 * tecriture, 1 * tecriture, 2 * tecriture

def bibliothèque_h(tecriture, Ltexte):

    return 0 * tecriture, 0, 0 * tecriture, 2 * tecriture

def attribution_variables(Liste_options, parametres):

    Listes_options_valeurs = []

    for k in parametres:
        if not k in Liste_options:
            print(k, ': cette option n existe pas mon petit bonhomme', parametres)

    for k in range(int(len(Liste_options) / 2)):
        try:
            #if type(parametres[Liste_options[k * 2]]) == type(Liste_options[k * 2 + 1]) or type(parametres[Liste_options[k * 2]]) == float or type(parametres[Liste_options[k * 2]]) == int or k == 0:
            Listes_options_valeurs.append(parametres[Liste_options[k * 2]])
            #else:
                #Listes_options_valeurs.append(Liste_options[k * 2 + 1])
               # print('vérifie le type de la variable', Liste_options[k * 2], '  potatoes !!!')
        except:
            if k == 0:
                print('précise le canvas mon coco')
            Listes_options_valeurs.append(Liste_options[k * 2 + 1])

    return Listes_options_valeurs



#window = Tk()
#canvas = Canvas(window, width=1000, height=200, bg='black')
#canvas.pack()

#Sacha_texte(canvas=canvas, texte='victoire', xt=100, yt=100, taille_texte=20, epaiseur_texte=10, couleur='white', couleur_clignotement='red', temps_clignotement=100, repetition=11)



#window.mainloop()