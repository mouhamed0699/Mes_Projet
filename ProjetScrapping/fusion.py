import json

# Ouvrir les deux fichiers JSON
with open('data.json', 'r') as file1:
    data1 = json.load(file1)

with open('flight_info.json', 'r') as file2:
    data2 = json.load(file2)

# Fusionner les données des deux fichiers
data_fusion = data1 + data2  # Utilisation de l'opérateur ** pour fusionner les dictionnaires

# Enregistrer les données fusionnées dans un nouveau fichier JSON
with open('fichier_vol.json', 'w') as outfile:
    json.dump(data_fusion, outfile)
