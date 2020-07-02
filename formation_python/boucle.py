#coding : utf-8
"""
boucles     : while / for
mots clés   : break(casse la boucle) / continue(revient au début de la boucle)    
"""

compteur = 0
while compteur <= 5:
    print("je suis une phrase")
    compteur += 1
print("je suis sortie de la boucle")

# dans un jeu video
jeulance = True

while jeulance:
    # fais des instructions en rapport avec le jeu
    choixMenu = input(">")

    if choixMenu == "again":
        continue
    elif choixMenu == "quit":
        #break
        jeulance = False
    elif choixMenu == "hello":
        print("Bonjour !")
    else:
        print("Commande introuvable")
print("A bientot ...") 


# boucle for

phrase = "Bonjour tous le monde !"
for lettre in phrase :
    print(lettre)