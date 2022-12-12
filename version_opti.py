import datetime
import numpy as np

#Fonction recursive qui fait tout
def TestValidationCarre(pos, visited, actual_square, min_square, square):
    global hauteur, largeur, square_answer
    if actual_square >= min_square:
        # On resort ca n'as pas de sens de continue
        return min_square

    if pos[0] > hauteur - 1:
        # On sort de la grille, donc on renvoie la valeur du point actuel
        square_answer = square
        if actual_square < min_square:
            print(actual_square)
        return actual_square

    #Décalage sur la grille
    new_pos = pos.copy()
    if new_pos[1] + 1 >= largeur:
        new_pos[0] += 1
        new_pos[1] = 0
    else:
        new_pos[1] += 1
    # Si on tombe sur un point de la matrice pleine
    if grid[pos[0]][pos[1]] == "1":
        # on relance la fonction
        return TestValidationCarre(new_pos, visited, actual_square, min_square, square)

    if pos not in visited:
        # Si la possition dans la matrice est déja visited, on test :
        i = pos[0]
        j = pos[1]
        long = 0
        long = min(largeur - j - 1, hauteur - i - 1)
        while long != -1:
            tmp_visit = []
            is_square = True
            for h in range(i, i + long + 1):
                for w in range(j, j + long + 1):
                    # Si le point n'est pas visité, et qu'il n'est pas visité et = a 1 alors on dis que le carré est visité
                    if grid[h][w] != "1" and [h, w] not in visited:
                        tmp_visit += [[h, w]]
                    else:
                        #le carré n'est pas un carré et on break ( trouvé un point de matrice non ecrivable), donc on break le for
                        is_square = False
                        break

            if is_square:
                #Si le carré est valide, on relance pour généré un carré plus petit
                min_square = TestValidationCarre(new_pos, visited + tmp_visit[1:], actual_square + 1, min_square, square + [tmp_visit])
            long -= 1


    else:
        # sinon on relance avec un carré plus petit
        min_square = TestValidationCarre(new_pos, visited, actual_square, min_square, square)

    # On retourne la valeur du carré optimun trouvé
    return min_square

def print_matrice_base(matrice_base):
    for i in matrice_base:
        for j in i:
                print("{:^4}".format(j), end="")
        print("\n")

def opti(matrice_base):
    mini_square = 1000000000
    matrice_mini = []
    nb_square = 100
    for i in range(0, len(matrice_base)):
        for j in range(0,len(matrice_base[i])):
            matrice_base,nb_square = filling_first_line(matrice_base,j,i,nb_square)
            matrice_base,nb_square = filling(matrice_base,j,i,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                # print()
                # print_matrice_base(matrice_base)
                # print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()
    
    for i in range(0, len(matrice_base)):
        for j in range(0,len(matrice_base[i])):
            matrice_base,nb_square = filling(matrice_base,j,i,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                # print()
                # print_matrice_base(matrice_base)
                # print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()
    for i in reversed(range(0, len(matrice_base))):
        for j in reversed(range(0,len(matrice_base[i]))):
            matrice_base,nb_square = filling_first_line(matrice_base,j,i,nb_square)
            matrice_base,nb_square = filling(matrice_base,j,i,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                print()
                print_matrice_base(matrice_base)
                print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()

    for i in reversed(range(0, len(matrice_base))):
        for j in reversed(range(0,len(matrice_base[i]))):
            matrice_base,nb_square = filling(matrice_base,j,i,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                print()
                print_matrice_base(matrice_base)
                print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()

    for i in range(0, len(matrice_base[0])):
        for j in range(0,len(matrice_base)):
            matrice_base,nb_square = filling_first_line(matrice_base,i,j,nb_square)
            matrice_base,nb_square = filling(matrice_base,i,j,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                print()
                print_matrice_base(matrice_base)
                print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()
    
    for i in range(0, len(matrice_base[0])):
        for j in range(0,len(matrice_base)):
            matrice_base,nb_square = filling(matrice_base,i,j,nb_square)

            if mini_square > count(matrice_base):
                mini_square = count(matrice_base)
                matrice_mini = matrice_base
                print()
                print_matrice_base(matrice_base)
                print("Nombre de carré : ",count(matrice_base))
            nb_square = 100
            matrice_base, largeur, hauteur = init()
    return matrice_mini


def filling_first_line(matrice_base,x_base,y_base,nb_square):
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
    return matrice_base,nb_square

def filling(matrice_base,x_base,y_base,nb_square):
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
    return matrice_base, nb_square
            
                

def matrice_true(matrice_min):
    break_point = []
    larg = len(matrice_min)
    for i in range(0,len(matrice_min)):
        for j in range (0,len(matrice_min[i])):
            if matrice_min[i][j] != "0":
                break_point.append([i,j])
    
    for i in range(0,len(break_point)):
        break_point[i] = max(break_point[i])
    
    for i in range(0,len(break_point)):
        larg = min(break_point[i],larg)
    return(larg)
def neighourg_x(x,y,matrice_base,nb_x):
    if matrice_base[y][x] == "0" :
        if x < len(matrice_base[y])-1:
            if matrice_base[y][x+1] == "0":
                nb_x = neighourg_x(x+1,y,matrice_base,nb_x+1)
    return nb_x


def neighourg_y(x,y,matrice_base,nb_y):
    if matrice_base[y][x] == "0" :
        if y < len(matrice_base)-1:
            if matrice_base[y+1][x] == "0":
                nb_y = neighourg_y(x,y+1,matrice_base,nb_y+1)
    return nb_y

def count(matrice_base):
    liste_square = []
    for i in range(0, len(matrice_base)):
        liste_square +=matrice_base[i]

    return(len(np.unique(liste_square))-1)

def init():
    #On import le Fichier initial :
    f = open("s5.txt", "r")

    #On créé les var hauteur et largeur :
    largeur = int(f.readline())
    hauteur = int(f.readline())

    #On créé les matrices afin de travailler dessus
    ligne = f.readline()
    grid = []

    for i in range(hauteur):
        grid.append([j for j in ligne[i * largeur:i * largeur + largeur]])
    
    return grid, largeur, hauteur

# on génére le temps nécéssaire pour le calcul
first_time = datetime.datetime.now()
grid, largeur, hauteur = init()
print(largeur,hauteur)
matrice_final = opti(grid)

print_matrice_base(matrice_final)
print("Nombre de carré mini optimisation : ",count(matrice_final))
print()

min_square_opti = count(matrice_final)
square_answer = []

result_square = TestValidationCarre([0, 0], [], 0, min_square_opti, [])
print("Min Square:", result_square)
second_time = datetime.datetime.now()
print("Seconds:", second_time - first_time)
cpt = 0
# on Remplace les points de la matrice par 1 ou . selon si il sont égaux a 1 ou 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            grid[i][j] = "."

# On compte le nombre de carré pour remplir la matrice
for i in square_answer:
    for j in i:
        grid[j[0]][j[1]] = cpt
    cpt += 1


# On affiche la grille complete
print_matrice_base(grid)


