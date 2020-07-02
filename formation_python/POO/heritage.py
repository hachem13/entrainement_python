#coding: utf-8
"""
fonction utile : 
    isanstance(<objet>, <class>)            : vérifie que l'objet est de la class enseignée
    issubclass(<class_fille>, <class_mere>) : vérifie qu'une class est fille d'une autre
"""
#class mere
class vehicule:
    def __init__(self, nomVehicule, quantiteCarburant):
        self.nomVehicule = nomVehicule
        self.carburant = quantiteCarburant
    def seDpalacer(self):
        print("Le vehicule {} se déplace ...".format(self.nomVehicule))

#class fille
class voiture(vehicule):
    def __init__(self, nomVoiture, quantite, puissance ):#pas obliger de mettre les même attributs de mere
        vehicule.__init__(self,nomVoiture, quantite)
        self.puissance = puissance
    def seDpalacer(self): # on peut redefinir la methode depalacer
        print("je roule sur la route ...")

#class petite fille
class voitureSportif(voiture):
    def __init__(self, nomVoiture, quantite, puissance):
        voiture.__init__(self, nomVoiture, quantite, puissance)
    def seDpalacer(self):
        print("je roule très vite")


class avion(vehicule):
    def __init__(self, nomAvion, quantite, puissance, transport):
        vehicule.__init__(self, nomAvion, quantite)
        self.puissance = puissance
        self.transport = transport
    def seDpalacer(self):
        print("je survole les airs ...")

# comment verifier qu'un objet fait parite d'une class fille

class Animal:
    def __init__(self, nom):
        self.nom = nom
    
    def manger(self):
        print(self.nom, "mange ...")

class Reptile(Animal):
    def __init__(self, nom, regimeAlimentaire):
        Animal.__init__(self, nom)
        self.regime = regimeAlimentaire
    def manger(self):
        print("le reptile mange")




# programme principale
"""
V1 = vehicule("peugeot 207", 90)
V2 = vehicule("F22 Raptor", 2400)
print(V1.nom)
print(V2.nom)
"""
"""
voiture1 = voiture("ferrari", 100, 500)
voiture1.seDpalacer()
print(voiture1.puissance, 'CH')

avion1 = avion("Bowing 747", 3000, 3000, "personne")
avion1.seDpalacer()
print(avion1.puissance, "CH")

voitureSportif1 = voitureSportif("seat leon", 150, 200)
voitureSportif1.seDpalacer()
print(voitureSportif1.puissance, "CH")
"""

lezard = Reptile("lezard", "grenouille")
lezard.manger()
print(lezard.regime)
if isinstance(lezard, Animal):
    print("lezard est un animal")
if issubclass(Reptile, Animal):
    print("Reptile hérite d'Animal")