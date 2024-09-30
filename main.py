#### Imports et définition des variables globales
#import random

""" uighiugi"""

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode = 'r',  encoding='utf8') as f :
        r = f.readlines()
        for elt in r :
            l.append( [ int( elt[i:i+2] ) for i in range(0, len(elt), 3) ])
    return l

def get_list_k(data, k):
    """ uhiuh"""
    return data[k]

def get_first(l):
    """ oihihoihn """
    return l[0]

def get_last(l):
    """hg ouhuh """
    return l[-1]

def get_max(l):
    """uhoiug"""
    maxi = l[0]
    for elt in l[1:]:
        maxi = max(maxi, elt)

    return maxi

def get_min(l):
    """ iugigi """
    mini = l[0]
    for elt in l[1:]:
        mini = min(mini, elt)
    return mini

def get_sum(l):
    """ iugig"""
    som = 0
    for elt in l:
        som = som + elt

    return som



#### Fonction principale


def main():
    """ uigig """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
