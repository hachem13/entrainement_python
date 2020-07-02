#coding: utf-8

class Robot:
    """
    classe des Robots
    """
    def __init__ (self):
        print("création d'un robot")#, self) self l'objet appel lui même
        self.name = "Robot toto"
        self.age = 1

print("lancement du programme")

R1 = Robot()
print("nom de R1 -> {}".format(R1.name))
R2 = Robot()


class Robot1:
    """
    #classe des robots
    """
    def __init__ (self, name, age):
        print("création d'un robot")#, self) self l'objet appel lui même
        self.name = name
        self.age = age

print("lancement du programme")

R1 = Robot1("toto", 1)
print("nom de R1 -> {}, sont age {}".format(R1.name, R1.age))

R2 = Robot1("coco", 23)
print("nom de R2 -> {}, sont age {}".format(R2.name, R2.age))

# on peut changer l'attribut 
R1.name = "jojo"
print("nom de R1 -> {}, sont age {}".format(R1.name, R1.age))

#attribut de class

class Machine:
    """
    classe des Robots
    """
    MachineCrees = 0

    def __init__ (self, name, age):
        print("création d'un robot")#, self) self l'objet appel lui même
        self.name = name
        self.age = age
        Machine.MachineCrees += 1

print("lancement du programme")

R1 = Machine("tutu", 2)
print("Robots Existants: {}".format(Machine.MachineCrees))

R2 = Machine("lulu", 3)
print("Robots Existants: {}".format(Machine.MachineCrees))