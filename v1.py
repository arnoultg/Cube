import numpy as np

def init(path_file):
    f = open(path_file, "r")
    width = int(f.readline())
    hight = int(f.readline())
    base = f.readline()
    matrice_base = []
    for i in range(0, hight):
        ligne = base[width*i:width*(i+1)] # On découpe la ligne en fonction de la largeur
        ligne = list(ligne) # On transforme la ligne en liste
        matrice_base.append(ligne)
    
    for i in range(0, len(matrice_base)):
        for j in range(0, len(matrice_base[i])):
            if matrice_base[i][j] == "0":
                matrice_base[i][j] = "XXX"
            else:
                matrice_base[i][j] = "###"

    return matrice_base


def print_matrice_base(matrice_base):
    for i in range(0, len(matrice_base)):
        for j in range(0, len(matrice_base[i])):
                print("",matrice_base[i][j],"", end="")
        print()




def filling(matrice_base,nb_square):
    # x_test = 0
    # y_test = 0
    # nb_y = neighourg_y(x_test,y_test,matrice_base,0)
    # nb_x = neighourg_x(x_test,y_test,matrice_base,0)
    # larg_square = min(nb_x,nb_y)+1
    # #print(larg_square)
    # matrice_min = []
    # for i in range(0, larg_square):
    #     matrice_min.append(matrice_base[y_test+i][x_test:larg_square+x_test])
    
    # taille_mat = matrice_true(matrice_min)
    # for i in range(0, taille_mat):
    #     for j in range(0, taille_mat):
    #         matrice_base[y_test+i][x_test+j] = nb_square
    # nb_square += 1


    for y in range(0, len(matrice_base)):
        for x in range(0,len(matrice_base[y])):
            nb_y = neighourg_y(x,y,matrice_base,0)
            nb_x = neighourg_x(x,y,matrice_base,0)
            larg_square = min(nb_x,nb_y)+1
            #print(larg_square)
            matrice_min = []
            for i in range(0, larg_square):
                matrice_min.append(matrice_base[y+i][x:larg_square+x])
            
            taille_mat = matrice_true(matrice_min)
            for i in range(0, taille_mat):
                for j in range(0, taille_mat):
                    matrice_base[y+i][x+j] = nb_square
            nb_square += 1
        
            
                

def matrice_true(matrice_min):
    larg = len(matrice_min)
    for i in range(0,len(matrice_min)):
        for j in range (0,len(matrice_min[i])):
            if matrice_min[i][j] != "XXX":
                larg=min(i,j)
                break
    #print(larg)
    return(larg)



def neighourg_x(x,y,matrice_base,nb_x):
    if matrice_base[y][x] == "XXX" :
        if x < len(matrice_base[y])-1:
            if matrice_base[y][x+1] == "XXX":
                nb_x = neighourg_x(x+1,y,matrice_base,nb_x+1)
    return nb_x


def neighourg_y(x,y,matrice_base,nb_y):
    if matrice_base[y][x] == "XXX" :
        if y < len(matrice_base)-1:
            if matrice_base[y+1][x] == "XXX":
                nb_y = neighourg_y(x,y+1,matrice_base,nb_y+1)
    return nb_y

def count(matrice_base):
    nb_square = 0
    liste_square = []
    for i in range(0, len(matrice_base)):
        liste_square +=matrice_base[i]

    return(len(np.unique(liste_square))-1)

def main():
    matrice_base = init("s1.txt")
    print_matrice_base(matrice_base)
    nb_square = 100
    filling(matrice_base,nb_square)
    print()
    print_matrice_base(matrice_base)
    print("Nombre de carré : ",count(matrice_base))
main()
    

