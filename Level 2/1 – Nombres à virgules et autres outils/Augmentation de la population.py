from math import *
populationActuelle = int(input())
croissancePourcent = float(input())
populationFuture = floor( populationActuelle * (1 + croissancePourcent / 100) )
print(populationFuture)