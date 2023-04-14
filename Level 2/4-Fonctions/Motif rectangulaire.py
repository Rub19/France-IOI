def AfficheLignes(nbColonnes, motif ):
    for i in range(nbColonnes):
        print(motif, end="")
    print()    






nbLignes = int(input())
nbColonnes = int(input())
motif = input() 

for i in range (nbLignes):
    AfficheLignes(nbColonnes, motif)