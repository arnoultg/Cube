def couverture_minimale(zone, largeur, hauteur, x, y, couverture):
    # Si on a parcouru toute la zone, on retourne la taille de la couverture
    if x == largeur and y == hauteur:
        return len(couverture)
    # Si on est sorti des limites de la zone, on retourne la taille maximale possible de la couverture
    if x > largeur or y > hauteur:
        return largeur * hauteur
    # Si la case actuelle est un trou ou si elle a déjà été couverte, on passe à la case suivante
    if zone[hauteur-y][x-1] == "1" or (x, y) in couverture:
        if x == largeur:
            return couverture_minimale(zone, largeur, hauteur, 1, y+1, couverture)
        else:
            return couverture_minimale(zone, largeur, hauteur, x+1, y, couverture)
    # Sinon, on explore les deux possibilités : couvrir ou ne pas couvrir la case actuelle
    else:
        # Si on couvre la case actuelle, on ajoute cette case à la couverture et on passe à la case suivante
        couverture1 = couverture.copy()
        couverture1.append((x, y))
        if x == largeur:
            res1 = couverture_minimale(zone, largeur, hauteur, 1, y+1, couverture1)
        else:
            res1 = couverture_minimale(zone, largeur, hauteur, x+1, y, couverture1)
        # Si on ne couvre pas la case actuelle, on passe directement à la case suivante
        if x == largeur:
            res2 = couverture_minimale(zone, largeur, hauteur, 1, y+1, couverture)
        else:
            res2 = couverture_minimale(zone, largeur, hauteur, x+1, y, couverture)
        # On retourne la couverture minimale des deux possibilités
        return min(res1, res2)

# Lecture du fichier d'instance

with open("s1.txt") as f:
    largeur = int(f.readline())
    hauteur = int(f.readline())
    base = f.readline()
    matrice_base = []
    for i in range(0, hauteur):
        ligne = base[largeur*i:largeur*(i+1)] # On découpe la ligne en fonction de la largeur
        ligne = list(ligne) # On transforme la ligne en liste
        matrice_base.append(ligne)


# Appel de la fonction d'exploration exhaustive
couverture = []
print(couverture_minimale(matrice_base, largeur, hauteur, 1, 1, couverture))
