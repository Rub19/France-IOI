from math import ceil

CONST_masse_1_sac = 60 
CONST_prix_1_sac = 45 
masse_ciment = float(input()) 
nb_sacs = ceil(masse_ciment / CONST_masse_1_sac)
prix_ciment = nb_sacs * CONST_prix_1_sac 
print(prix_ciment)