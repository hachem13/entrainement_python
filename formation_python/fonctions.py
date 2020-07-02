#coding : utf-8
"""
fonction vue    : print(), input()
                  type(), int(), float(), str(), bool()
"""
# pour afficher ce qu'il y as dans le print
print("bonjour a tous !")

# fonciton input()
age = input("quel age as tu ? ")
age = int(age)

print("tu as {} ans".format(age))

# creér ça propre fonction
def dire_bonjour():
    print("Hello tous le monde")
#je ne suis plus dans la fonction
dire_bonjour()

def dire(nomPersonne, messagePersonne):
    print("{} : {}".format(nomPersonne, messagePersonne))

dire("hm", "bonjour à tous")
dire(messagePersonne = "bonjour à tous", nomPersonne = "hm" )

#nombre infini d'arguments *
def show_inventory(*list_items):
    for item in list_items:
        print(item)

show_inventory("épée")
show_inventory("épée", "arc", "potion", "cap")

# valeur de retour 
def calculer_somme(nombre1, nombre2):
    return nombre1 + nombre2

print(calculer_somme(5, 16))

def comparer_nombres(nombre1, nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 == nombre2:
        return "égalité"
    else:
        return nombre2
print(comparer_nombres(12, 3))
print(comparer_nombres(3, 3))
print(comparer_nombres(12, 14))

#fonction lambda
a = lambda: print("bonjour !")
a()

TTC = lambda prixHT : prixHT + (prixHT * 20 / 100)
print(TTC(24))

calculer = lambda a, b : a + b
print(calculer(22, 12))