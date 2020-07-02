#coding: utf-8

"""
une variable        : doit commancer par une lettre
                      ne pas contenir de caractéres spéciaux
                      ne pas contenir d'éspace
                      utiliser des _
type standard       : entier numerique int()
                      nombre floatton float()
                      chaine de caractére str()
                      booléen bool()
                      autre (liste, dictionnaire, tuple ...)

fonction vue        : print()                       -> afficher à l'écran
                      input()                       -> lire au clavier
                      type()                        -> retourne le type d'une donnée
                      int(), float(), str(), bool() -> pour caster une donnée (la convertir)
                      str.format()                  -> formater une chaine
"""

agePersonne = 14
agePersonne1 = "25" # on peut pas faire des calcules sur les str
prixHT = 125.3
continuerPartie = False

print(type(agePersonne))
print(type(agePersonne1))
print(type(prixHT))
print(type(continuerPartie))
print("Age de la personne", agePersonne)

# 1er méthode
text = "l'age de la personne est :{} et le prix est :{} euros"
print(text.format(agePersonne, prixHT))
# 2ème méthode
print("l'age de la personne est :{} et le prix est :{} euros".format(agePersonne, prixHT))

# saisie d'information
nomJoueur = input("veuillez entrée un nom : ")
print("Bienvenue !", nomJoueur)

# caster une donnée

prixHT = input("entrée votre prixHT : ")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT * 20 / 100) 

print("prixTTC est : ", prixTTC) 

