import numpy as np
#Creation de la matriceà partir du fichier de base
def init(path_file):
    f = open(path_file, "r")
    width = int(f.readline())
    hight = int(f.readline())
    base = f.readline()
    matrice_base = []
    for i in range(0, hight):
        ligne = base[width * i:width * (i + 1)]  # On découpe la ligne en fonction de la largeur
        ligne = list(ligne)  # On transforme la ligne en liste
        matrice_base.append(ligne)

    for i in range(0, len(matrice_base)):
        for j in range(0, len(matrice_base[i])):
            if matrice_base[i][j] == "0":
                matrice_base[i][j] = "XXX"
            else:
                matrice_base[i][j] = "###"

    return matrice_base

#Fonction d'affichage de base de la matrice
def print_matrice_base(matrice_base):
    for i in range(0, len(matrice_base)):
        for j in range(0, len(matrice_base[i])):
            print("", matrice_base[i][j], "", end="")
        print()

#Permet de trouver la case disponible la plus en haut a gauche
def find_dispo(matrice_base):
    for i in range(0,len(matrice_base)):
        for j in range(0,len(matrice_base[i])):
            if matrice_base[i][j]=="XXX":
                return i,j

#Permet de vérifier si son voisin de droite est dispo, fonction recursive jusqu'a trouver un élément bloquant
def neighourg_x(x,y,matrice_base,nb_x):
    if matrice_base[y][x] == "XXX" :
        if x < len(matrice_base[y])-1:
            if matrice_base[y][x+1] == "XXX":
                nb_x = neighourg_x(x+1,y,matrice_base,nb_x+1)
    return nb_x



#Permet de vérifier si son voisin du bas est dispo, fonction recursive jusqu'a trouver un élément bloquant
def neighourg_y(x,y,matrice_base,nb_y):
    if matrice_base[y][x] == "XXX" :
        if y < len(matrice_base)-1:
            if matrice_base[y+1][x] == "XXX":
                nb_y = neighourg_y(x,y+1,matrice_base,nb_y+1)
    return nb_y


# Permet de verifier l'intégrité du carré découvert par les neighourg
def matrice_true(matrice_min):
    larg = len(matrice_min)
    for i in range(0,len(matrice_min-1)):
        for j in range (0,len(matrice_min[i]-1)):
            if matrice_min[i][j] != "XXX":
                larg=min(i,j,larg)
    return(larg)

def CreateKmax(matrice_base):
    matriceKmax=[matrice_base]
    for y in range(0, len(matrice_base)):
        for x in range(0, len(matrice_base[y])):
            nb_y = neighourg_y(x, y, matrice_base, 0)
            nb_x = neighourg_x(x, y, matrice_base, 0)
            larg_square = min(nb_x, nb_y) + 1
            matriceKmax[x][y][larg_square]
    return matriceKmax

def print_matriceKmax(Kmax_Matrice):
    for i in range(0, len(Kmax_Matrice)):
        for j in range(0, len(Kmax_Matrice[i])):
            for k in range(0,len(Kmax_Matrice[i][j])):
                print("", Kmax_Matrice[i][j][k], "", end="")
        print()

def main():
    matrice_base = init("s7.txt")
    print_matrice_base(matrice_base)
    Kmax_Matrice = CreateKmax(matrice_base)


    print()
    print_matriceKmax(Kmax_Matrice)
    print(Kmax_Matrice[1][1][1])



main()
