#coding: utf-8

class Robot:
    """
    classe qui défini un Robot
    """

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):#methode standard
        print("{} a dit : {}".format(self.nom,message))
    
    
    
#programme principal
R1 = Robot("toto", 33)

R1.parler("bonjour !")
R1.parler("Comment allez vous !")


#methode de class
class Robot1:
    """
    classe qui défini un Robot
    """
    materiaux = "Métal"
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):#methode standard
        print("{} a dit : {}".format(self.nom,message))
    
    def changerMateriaux(cls, nouveauMateriaux): #cls = methode de class
        Robot1.materiaux = nouveauMateriaux

    changerMateriaux = classmethod(changerMateriaux)# importante pour la methode de class
#programme principal
R1 = Robot1("toto", 33)

print("matériaux actuelle {}".format(Robot1.materiaux))

Robot1.changerMateriaux("Acier")

print("matériaux changer {}".format(Robot1.materiaux))

# méthode statique

class Robot2:
    """
    classe qui défini un Robot
    """
    materiaux = "Métal"
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self, message):#methode standard
        print("{} a dit : {}".format(self.nom,message))
    
    def changerMateriaux(cls, nouveauMateriaux): #cls = methode de class
        Robot2.materiaux = nouveauMateriaux

    changerMateriaux = classmethod(changerMateriaux)# importante pour la methode de class

    def definition():
        print("les Robots sont des machines")# methode statique 

    definition = staticmethod(definition)

#programme principal
R1 = Robot1("toto", 33)

print("matériaux actuelle {}".format(Robot2.materiaux))

Robot2.changerMateriaux("Acier")

print("matériaux changer {}".format(Robot2.materiaux))

Robot2.definition()