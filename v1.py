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
                print(" X ", end="")
            else:
                print(" . ", end="")
        print()




def filling(square):
    for x in range(0, len(square)):
        for y in range(0,len(square[i])):
            if square[x][y] == "0":
                

def neighourg(x,y,square):
    if square[x][y] == "0":
        if square[x+1][y] == "0":
            neighourg(x+1,y,square)
        else:
            if square[x][y+1] == "0":
                


            



def main():
    square = init("s1.txt")
    print_square(square)
main()
    

