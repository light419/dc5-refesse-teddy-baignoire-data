# EXERCICE 4
# Définissez une fonction pour convertir le CTR (Click-Through Rate) en pourcentage. Testez la fonction avec plusieurs entrées.


def convertir_ctr_en_pourcentage(ctr):
    pourcentage = ctr * 100
    return pourcentage

ctr_test_1 = 0.02
resultat_test_1 = convertir_ctr_en_pourcentage(ctr_test_1)
print(f"Le CTR {ctr_test_1} en pourcentage est : {resultat_test_1}%")

ctr_test_2 = 0.17
resultat_test_2 = convertir_ctr_en_pourcentage(ctr_test_2)
print(f"Le CTR {ctr_test_2} en pourcentage est : {resultat_test_2}%")

ctr_test_3 = 0.07
resultat_test_3 = convertir_ctr_en_pourcentage(ctr_test_3)
print(f"Le CTR {ctr_test_3} en pourcentage est : {resultat_test_3}%")