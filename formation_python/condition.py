#coding: utf-8

"""
opérateurs de comparaison : == (égal à)
                            !+ (différent de)
                            > (plus grand que)
                            < (plus petit que)
                            >= (plus grand ou égal)
                            <= (plus petit ou égal)

mot clé des conditions     : if / elif / else

condition multiple         : and (Et)
                             or (Ou)
                             in /  not in (Dans / Pas dans)
"""

identifiant = "hm"
motDePass = "azerty"

print("interface de connexion")

user_id = input("entrée votre identifiant: ")
user_password = input("entrée votre mot de pass: ")

#print("vous êtes connecter Bienvenue !", user_id)

# faire une condition 

if user_id == identifiant and user_password == motDePass:
    print("vous êtes connecter Bienvenue !", user_id)

print("je ne suis plus dans la condition ")

lettre_hasard = "b"
if lettre_hasard in "aeiouy" :
    print("c'est une voyelle")
else:
    print("c'est une consonne")

age = 24
if age == 18:
    print("Tu vient d'être majeur ")
elif age == 50:
    print("Tu vient d'avoir 50 ans")
elif age == 60:
    print("Tu vient d'avoir 60 ans")
else:
    print("Tu as ", age, "ans")

# valeur bouléen
jeuCharger = True # True est tjr vrai (=1)

if jeuCharger:
    print("le jeu est en marche")
else:
    print("le jeu a été quité")

jeuCharger = False # True est tjr vrai (=0)

if not jeuCharger:
    print("le jeu est éteint")
else:
    print("le jeu est lancer")

# faire des condition sur une fourchette
"""
age > 0 et age <= 80 --> 0 < age <= 80
"""
age = input("veuillez entrée votre age : ")
age = int(age)
if 0 < age <= 80 :
    print("l'age est validé")
else:
    print("l'age n'est pas valid")
