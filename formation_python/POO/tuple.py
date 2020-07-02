# coding: utf-8

""" 
(!) tuple         : conteneur immuable (dont on peut pas modifier la valeur)
Création de tuple : mon_tuple = ()       #vide
                    mon_tupel = 16,      # seule valeur 
                    mon_tuple = (14,)    # pareil qu'audessus
                    mon_tuple = (14, 33) # plusieurs valeurs
accées au valeur  : mon_tuple[X]         # valeur d'indice X

2 raison pour utiliser le tuple : affectation multiple, retour multiple de fonction 
"""

monTuple = (45,22)
print(type(monTuple))
print(monTuple[0])

# créee mes deux variable
nombre1, nombre2 = (14, 33)  
print(nombre1)
print(nombre2)

nombre1 = 22
print(nombre1)


def get_player_position():
    posX = 22
    posY = 33
    return (posX, posY)

# programme principale
coordX = 0
coordY = 0

print("position du joueur: ({}/{}) ".format(coordX, coordY))

coordX, coordY = get_player_position()

print("position du joueur: ({}/{}) ".format(coordX, coordY))



