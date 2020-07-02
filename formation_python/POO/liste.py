#coding : utf-8

#Création d'une liste
inventaire = [] # liste vide
inventaire1 = [1, 2, 3, "voiture"] # liste avec des élements 
inventaire2 = ["arc"]* 10 #multiplication de l'élément de la liste
inventaire3 = ["arc", "éper", "bouclier"] #liste criossante
"""i = 0
while i < len(inventaire3):
    i += 1
    print(inventaire3[i])
"""
for valeur in inventaire3:
    print(valeur)



print(inventaire)
print(inventaire1)
print(inventaire2)
print(inventaire3[2]) # pour afficher l'element dans la liste
print(inventaire3[2:]) # afficher les deux premeiers elements
print(inventaire3[:3]) # afficher les deux dérnier éléments
print(inventaire3[:-2]) # afficher le deuxiéme élément a partir de la fin 
print(inventaire3[::2]) # 3 ème élément deux par deux
inventaire3[2] = "bouclier d'acier"
print(inventaire3[:]) # pour changer un élement de la liste
# pour vérifier un élément de la liste
if "bouclier d'acier" in inventaire3:
    print("je possede un bouclier")
else:
    print("je ne possede pas un bouclier")

# ajouter un élement dans une liste en fin de liste
inventaire4 = []
inventaire4.append("monster")
print(inventaire4[:])

# ajouter un élement dans une liste avec la position
inventaire5 = ["arc", "bouclier", "monteau", "epée"]
inventaire5.insert(2, "postion")
print(inventaire5[:])

# pour supprimer 
inventaire5.remove("arc")
print(inventaire5) # ou del inventaire5[0]

# pour retourner l'index dans une liste 
print("index est :", inventaire5.index("epée"))

# pour trié la liste
inventaire5.sort()
print(inventaire5[:])

# mettre à l'envere les élements d'une liste
inventaire5.reverse()
print(inventaire5[:])

# compter le nombre d'élément dans la liste
inventaire6 = ["arc", "potion", "potion", "potion", "epée"]
inventaire6.count("potion")
print("nombre de potion est :", inventaire6.count("potion"))

# pour vider la liste
inventaire6.clear()
print(inventaire6[:])

# pour passer d'une liste a une chaine de caractére 
inventaire7 = ["bonjour", "comment", "va", "tu", "?"]
phrase = " ".join(inventaire7)
print(phrase)

# pour copier une liste
import copy

liste1 = ["arc", "bouclier", "monteau", "epée"]
# Ne copie pas la liste -> liste2 = liste1
liste2 = copy.deepcopy(liste1)

print("liste1 : ", liste1[:])
print("liste1 : ", liste2[:])

liste2.append("potion")

print("liste1 : ", liste1[:])
print("liste1 : ", liste2[:])

# ajoute une liste à une autre

liste3 = ["arc", "bouclier", "monteau", "epée"]
liste4 = ["fleche", "potion", "parchemain"]
liste3.extend(liste4)
print(liste3[:])
liste5 = liste3 + liste4
print(liste5[:])

# comment parcourir la liste avec l'indice et la valeur (tuple)

for indice_object, valeur_objet in enumerate(liste3) :
    print("Element d'indice {} -> {} ".format(indice_object, valeur_objet))
