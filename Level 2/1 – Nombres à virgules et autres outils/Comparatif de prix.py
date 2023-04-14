nb_légumes = int(input())
for _ in range(nb_légumes):
   poids = float(input()) 
   âge = float(input())   
   prix = float(input())  
   prix_au_kilo = prix / poids 
   print(prix_au_kilo)