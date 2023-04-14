from math import *
 
taxeActuelle = float(input())
taxeFuture = float(input())
prixLegume = float(input())
nouveauPrix = prixLegume / ( 1 + taxeActuelle / 100) * (1 + taxeFuture / 100)
nouveauPrix = round(nouveauPrix * 100) / 100
print(nouveauPrix)