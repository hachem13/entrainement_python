#coding : utf-8

"""
Gérer les exceptions : try/except (+else, finally)
type exception       : ValueError
                       NameError
                       TypeError
                       ZeroDivisionError
                       OsError
                       AssertionError
"""

ageUtilisateur = input("Quel age as tu ?")
try:
    ageUtilisateur = int(ageUtilisateur)
except:
    print("l'age est indiqué est incorrect")
else:
    print("tu as", ageUtilisateur, "ans")
finally:
    print("Fin de programme")

nombre1 = 120
nombre2 = input("choisir le nombre pour diviser: ")
try: 
    nombre2 = int(nombre2)
    print("resultat = {}".format(nombre1 / nombre2)) 
except ZeroDivisionError:
    print("vous ne pouvez pas diviser par zéro")
except ValueError:
    print("Vous devez rentrer un nombre")
except:
    print("Valeur incorrect")
else:
    print("bravo, tu as noté un nombre valide")
finally:
    print("Fin du programme ...")


#lever d'exception à la main 
try:
    age = input("Quel age as tu ?: ")
    age = int(age)

    if age > 25:
        raise ValueError
except:
    print("j'ai attraper ton exception")

# assertion
try:
    age = input("Quel age as tu ?: ")
    age = int(age)

    assert age > 25 # je veut que age est plus grand que 25
except AssertionError:
    print("j'ai attraper l'assertion")

