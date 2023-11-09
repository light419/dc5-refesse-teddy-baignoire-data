# EXERCICE 2 - b
# Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.

liste_de_nombres = [7, 32, 14, 60, 42, 68, 40, 65, 53, 87]


maximum = liste_de_nombres[0]  
for nombre in liste_de_nombres:
    if nombre > maximum:
        maximum = nombre

minimum = liste_de_nombres[0] 
for nombre in liste_de_nombres:
    if nombre < minimum:
        minimum = nombre

somme = 0
for nombre in liste_de_nombres:
    somme += nombre
moyenne = somme / len(liste_de_nombres)


print(f"Le maximum est : {maximum}")
print(f"Le minimum est : {minimum}")
print(f"La moyenne est : {moyenne}")