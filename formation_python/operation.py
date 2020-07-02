#coding: utf-8

"""
Opérateur en Python     : + (addition)
                          - (soustraction)
                          * (multiplication)
                          / (division)
                          % (modulo " le reste de la division")
                    
variable = variable + X c'est la même chose que variable += X
variable = variable - X c'est la même chose que variable -= X
variable = variable * X c'est la même chose que variable *= X
variable = variable / X c'est la même chose que variable /= X
"""

calcule = 5 / 2
calcule = int(calcule)
calcule2 = 5 % 2
print("résultat :", calcule, "reste", calcule2)

calcule3 = 5 + 3 * 7
print(calcule3)

#ce n'est pas pareille que 
calcule4 = (5 + 3) * 7
print(calcule4)

# modification de certaine valeurs
niveauPersonnage =  input("niveau de départ: ")
niveauPersonnage = int(niveauPersonnage)
print("le niveau du personnage ", niveauPersonnage)

print("Combat réussi le niveau du personnage augmente ! ")
niveauPersonnage += 1 
print("le niveau du personnage ", niveauPersonnage)


