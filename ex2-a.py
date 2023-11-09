# EXERCICE 2 - a
# Créez une liste des dépenses marketing mensuelles et calculez les dépenses totales de l'année.

depenses_mensuelles = [300, 1100, 200, 1200, 300, 1200, 20, 1000, 980, 200, 1700, 1100]

depenses_annuelles = 0
for depense in depenses_mensuelles:
    depenses_annuelles += depense

print(f"Les dépenses marketing totales de l'entreprise sur l'année sont les suivantes: {depenses_annuelles}€.")