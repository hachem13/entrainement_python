# coding : utf-8
import math
"""
from math import sqrt -> pour importer que la fonction sqrt
from math import *    -> pour importer toutes les fonctions de math
"""
resultat = math.sqrt(100)
print(resultat)

sinus = math.sin(45)
print(sinus)

import player

player.au_revoir()
player.parler("hm", "bonjour tous le monde")

"""
from player import au_revoir pour importer un seule module
from player import parler
au_revoir()
parler("hm", "bonjour tous le monde")
"""

"""
from includes.player import au_revoir  pour importer le module a partir d'un fichier
au_revoir()

import includes.player
includes.player.au_revoir()

import includes.player as player renomer le nom du module
player.au_revoir()
"""


