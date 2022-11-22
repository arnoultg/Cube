def init(path_file):
    f = open(path_file, "r")
    width = int(f.readline())
    hight = int(f.readline())
    base = f.readline()
    square = []
    for i in range(0, hight):
        ligne = base[width*i:width*(i+1)] # On découpe la ligne en fonction de la largeur
        ligne = list(ligne) # On transforme la ligne en liste
        square.append(ligne)
    return square


def print_square(square):
    for i in range(0, len(square)):
        for j in range(0, len(square[i])):
            if square[i][j] == "0":
                square[i][j] = "X"
                print(" X ", end="")
            else:
                square[i][j] = "."
                print(" . ", end="")
        print()




def filling(square):
    nb_y = neighourg_y(3,0,square,0)
    nb_x = neighourg_x(3,0,square,0)


    print(nb_y,nb_x)
    # for y in range(0, len(square)):
    #     for x in range(0,len(square[y])):
    #         if square[y][x] == "0":
    #             nbx,nby = neighourg(x,y,square,0,0)
    #             #print(nbx,nby)
                

def neighourg_x(x,y,square,nb_x):
    if square[y][x] == "X" :
        if x <= len(square):
            if square[y][x+1] == "X":
                nb_x = neighourg_x(x+1,y,square,nb_x+1)
    return nb_x


def neighourg_y(x,y,square,nb_y):
    if square[y][x] == "X" :
        if y <= len(square):
            if square[y+1][x] == "X":
                nb_y = neighourg_y(x,y+1,square,nb_y+1)
    return nb_y



def main():
    square = init("s1.txt")
    print_square(square)
    filling(square)
main()
    

