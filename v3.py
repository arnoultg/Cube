import datetime
#On import le Fichier initial :
f = open("s5.txt", "r")

#On créé les var hauteur et largeur :
largeur = int(f.readline())
hauteur = int(f.readline())
print("largeur:", largeur)
print("hauteur:", hauteur)

#On créé les matrices afin de travailler dessus
ligne = f.readline()
grid = []

for i in range(hauteur):
    grid.append([j for j in ligne[i * largeur:i * largeur + largeur]])

for i in grid:
    print(*i)

square_answer = []

#Fonction recursive qui fait tout
def TestValidationCarre(pos, visited, actual_square, min_square, square):
    global hauteur, largeur, square_answer
    if actual_square >= min_square:
        # On resort ca n'as pas de sens de continue
        return min_square
    if pos[0] > hauteur - 1:
        # On sort de la grille, donc on renvoie la valeur du point actuel
        square_answer = square
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

# on génére le temps nécéssaire pour le calcul
first_time = datetime.datetime.now()
result_square = TestValidationCarre([0, 0], [], 0, largeur * hauteur, [])
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
for i in grid:
    for j in i:
        print("{:^3}".format(j), end="")
    print("\n")



