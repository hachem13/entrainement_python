# coding : utf-8
"""
Création de dictionnaire : dico = {} #vide 
                           dico = {<cle> : <valeur>, ...}
Ajouter un dictionnaire  : dico[<cle>] = <valeur>
suppression              : dico.pop(<cle>)
                           del dico[<cle>]
"""

dico = {"prenom":"hm"}
dico1 = {1:"hm"}
print(dico1[1])
dico1[2] = "mos"
print(dico1)

valeur_supprimer = dico1.pop(2)
print(valeur_supprimer)
print(dico1)

# del dico1[2]
# print(dico1)

# pour vérifier qu'une clé existe
if "prenom" in dico:
    print("prenom existe")
else:
    print("ça n'existe pas")

for key in dico.keys():
    print(key)
for key in dico.values():
    print(key)
for key , valeur in dico.items():
    print("la clé est {} et la valeur est {}".format(key,valeur))

# donner des paramettre a une fonction 
def maFonction(**paramettre):
    print(paramettre)

maFonction(nom = "hm", prnom = "mos")