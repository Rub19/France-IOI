def AfficherLigne(caractere, longueur): 
    for i in range(longueur):
        print(caractere, end="")
        print()


longueur = int(input())

AfficherLigne("x", longueur)
AfficherLigne("#", longueur)
AfficherLigne("i", longueur)