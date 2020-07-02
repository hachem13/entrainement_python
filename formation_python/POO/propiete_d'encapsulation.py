#coding: utf-8
"""
prorpiété : maniere de manipuler/contrôler des attributs
            principe d'encapsulation
"""

class Robot:
    """
    cette class représente un robot
    """

    def __init__(self, nom, age):
        print("création de robot")
        self.nom = nom
        self._age = age
    def _getage(self):
        if self._age <= 1:
            return "{} {}".format(self._age, "an")
        else:
            return "{} {}".format(self._age, "ans")
        """
        try:
            return self._age
        except:
            print("l'age n'éxiste pas !")
        """
    def _setage(self, nouvelAge):
        if nouvelAge < 0:
            self._age = 0
        else:
            self._age = nouvelAge
    
    def _delage(self):
        del self._age

    # property(<getter>, <setter>, <deleter>, <helper>)   
    age = property(_getage, _setage, _delage, "je suis l'age du robot")

# programme principal    

R1 = Robot("toto", 1)

print(R1.age)

R1.age = -5

print(R1.age)

R1.age = 12

print(R1.age)

del R1.age

print(R1.age)

help(Robot.age)


print("{} a {}".format(R1.nom, R1.age))