from random import randint

def deplacement_objet(canvas, corps, x, y):

    canvas.move(corps, -canvas.coords(corps)[0], -canvas.coords(corps)[1])
    canvas.move(corps, x, y)

def extirpation(Liste, *parametres):

    if len(parametres) == 1:
        return Liste[parametres[0]]
    elif len(parametres) == 0:
        print('t vraiment perdu, précise la liste, je vais pas le faire à ta place petite crapule')
    elif not ':' in parametres or len(parametres) == 3 and (parametres[1] != ':' or type(parametres[0]) != int or type(parametres[2]) != int) or len(parametres) > 3 or type(parametres[0]) != int and type(parametres[1]) != int:
        print('ça marche comme une liste ignorant')
    else:
        parametres_changeable = []
        for k in parametres:
            parametres_changeable.append(k)

        if parametres_changeable[0] == ':':
            parametres_changeable = [0] + parametres_changeable
        elif parametres_changeable[1] == ':' and len(parametres) == 2:
            parametres_changeable = parametres_changeable + [len(Liste)]

        return Liste[parametres_changeable[0]:parametres_changeable[2]]

def Sacha_random(Liste):

    return Liste[randint(0, len(Liste) - 1)]

def suppr(Liste, index):

    return Liste[:index] + Liste[index+1:]

def spinbox_range(*parametres):

    if len(parametres) > 2 or len(parametres) == 0:
        print('spinbox_range :', 'pas possible mon coco')
    else:
        if len(parametres) == 1:
            debut = 0
        else:
            debut = parametres[0]

        fin = parametres[len(parametres)-1]

        Liste = []
        for k in range(debut, fin):
            Liste.append(str(k))

        return Liste

Liste_double_hexadecimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '&', 'é', 'è']

def transforamtion_base_nouvelle_base(base, nouvelle_base, valeur, *type_variable):

    if nouvelle_base > len(Liste_double_hexadecimal):
        nouvelle_base = len(Liste_double_hexadecimal)
        print('bon tu déconnes avec la nouvelle base que tu as mise mais je l ai rectifié rien que pour tes beaux yeux')

    if type(valeur) == list:
        for k in range(len(valeur)):
            valeur[k] = str(valeur[k])
    elif type(valeur) != str:
        valeur = str(valeur)

    "transformation en décimal"
    t = 0
    for k in range(len(valeur)):
        "verification"
        if Liste_double_hexadecimal.index(valeur[-k-1]) >= base:
            print('tu t es trompé de base mon loulou')
            break

        t += Liste_double_hexadecimal.index(valeur[-k-1]) * base ** k

    "transformation en nouvelle base"
    valeur = []
    while t != 0:
        valeur.append(t%nouvelle_base)
        t = t // nouvelle_base

    "ajustement par rapport à ce qu'il y a dans *parametre"
    if len(type_variable) > 0:
        t = valeur.copy()

        if type_variable[0] == 'str':
            valeur = ''
            for k in range(len(t)):
                valeur += Liste_double_hexadecimal[t[-k-1]]
        elif type_variable[0] == 'int' and nouvelle_base <= 10:
            valeur = 0
            for k in range(len(t)):
                valeur = valeur*10 + t[-k-1]
        else:
            valeur.reverse()
    else:

        valeur.reverse()

    return valeur