import numpy as np

def init():
    f = open("s2.txt", "r")
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

def test_all(matrice_base):
    mini_square = 1000000000
    matrice_mini = []
    #matrice_mini = filling(matrice_base,2,9)
    for i in range(0, len(matrice_base)):
        for j in range(0,len(matrice_base[i])):
            matrice_base = filling(matrice_base,j,i)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                print()
                print_matrice_base(matrice_base)
                print("Nombre de carré : ",count(matrice_base))
            matrice_base = init()


    return matrice_mini

def filling(matrice_base,x_base,y_base):
    # x_test = 1
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
    nb_square = 100
    for x in range(0,len(matrice_base[y_base])-x_base):
            nb_y = neighourg_y((x+x_base),(y_base),matrice_base,0)
            nb_x = neighourg_x((x+x_base),(y_base),matrice_base,0)
            larg_square = min(nb_x,nb_y)+1
            matrice_min = []
            for k in range(0, larg_square):
                matrice_min.append(matrice_base[(y_base)+k][(x+x_base):larg_square+(x+x_base)])
            taille_mat = matrice_true(matrice_min)
            for k in range(0, taille_mat):
                for p in range(0, taille_mat):
                    matrice_base[(y_base)+k][(x+x_base)+p] = nb_square
            nb_square += 1

    for y in range(0, len(matrice_base)):
        for x in range(0,len(matrice_base[y])):
            nb_y = neighourg_y(x,(y+y_base)%len(matrice_base),matrice_base,0)
            nb_x = neighourg_x(x,(y+y_base)%len(matrice_base),matrice_base,0)
            larg_square = min(nb_x,nb_y)+1
            matrice_min = []
            for k in range(0, larg_square):
                matrice_min.append(matrice_base[(y+y_base)%len(matrice_base)+k][x:larg_square+x])
            taille_mat = matrice_true(matrice_min)
            for k in range(0, taille_mat):
                for p in range(0, taille_mat):
                    matrice_base[(y+y_base)%len(matrice_base)+k][x+p] = nb_square
            nb_square += 1
    return matrice_base
            
                

def matrice_true(matrice_min):
    break_point = []
    larg = len(matrice_min)
    for i in range(0,len(matrice_min)):
        for j in range (0,len(matrice_min[i])):
            if matrice_min[i][j] != "XXX":
                break_point.append([i,j])
    
    for i in range(0,len(break_point)):
        break_point[i] = max(break_point[i])
    
    for i in range(0,len(break_point)):
        larg = min(break_point[i],larg)
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
    liste_square = []
    for i in range(0, len(matrice_base)):
        liste_square +=matrice_base[i]

    return(len(np.unique(liste_square))-1)

def main():
    matrice_base = init()
    print_matrice_base(matrice_base)
    nb_square = 100
    matrice_final = test_all(matrice_base)
    print()
    print_matrice_base(matrice_final)
    print("Nombre de carré : ",count(matrice_final))
    

main()
    

