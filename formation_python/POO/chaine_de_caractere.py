# coding: utf-8

"""
une methode de chaine travaille sur une copie pas sur la chaine elle-même
class str : string(chaine de caractère)
            str.upper(), str.lower(), str.capitalize(), str.title(),
            str.center(<largeur>, <caractere-renmplissage>)
            str.find(<chaine>, <debut>, <fin>)
            str.index(<chaine>, <debut>, <fin>)
            str.strip() pour enlver les espace avant et après le string
            str.replace(<encienne>, <nouvelle>, <occurence>)
            str.split() pour mettre une chaine de caractère en liste
            str.isalpha()
            str.isdigit()
            str.isdecimal()
            str.isnumeric()
            str.isalphanum()
            str.islower()
            str.isupper()
            str.isidentifer()
            str.iskeyword()
"""

maChaine = "bonjour tous le monde !"

maChaine = maChaine.upper()
print(maChaine)

maChaine = maChaine.lower()
print(maChaine)

maChaine = maChaine.capitalize()
print(maChaine)

maChaine = maChaine.title()
print(maChaine)

maChaine1 = "MonSuperProgramme"
maChaine1 = maChaine1.center(50, "-")
print(maChaine1)
maChaine2 = "MonSuperProgramme"
print(maChaine2.find("Super"))
print(maChaine2.index("Super"))
try:
    print(maChaine2.index("super"))
except ValueError:
    print("je n'est pas trouvé dans la chaine de caractère !")
maChainn3 = "    MonSurperProgramme"
print(maChainn3.strip())

maChainn4 = "Mon-Super-Programme"
print(maChainn4.replace("-", " "))

maChaine5 = "Magicien|10|50"
print(maChaine5.split("|"))

maChainn6 = "bonjour"
if maChainn6.islower():
    print("la chaine en minuscule")
else:
    print("il contien un majuscule")

maChaine7 = "class"
if maChaine7.isidentifier():
    print("reserver")
else: 
    print("libre")