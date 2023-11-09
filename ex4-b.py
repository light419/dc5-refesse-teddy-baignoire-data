# EXERCICE 4
# Étape 1 : Définir la fonction qui calcule le factoriel
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

# Étape 2 : Appeler la fonction
nombre = 7
resultat = factoriel(nombre)

# Étape 3 : Afficher le résultat
print(f"Le factoriel du {nombre} est le suivant : {resultat}")