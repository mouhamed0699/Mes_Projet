import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    database="cmd_services",
    user="djilybaxdad",
    password="0504"

    #     user: 'djilybaxdad',
    # host: 'localhost',
    # database: 'cmd_services',
    # password: '0504',

)




# CREATE TABLE voiture (vin SERIAL PRIMARY KEY, 
#  modele VARCHAR(500) NOT NULL, 
#  prix VARCHAR(50) NOT NULL, 
#  image VARCHAR(500) NOT NULL);

# with open('djily.json', 'r') as file:
#     data = json.load(file)



# cursor = conn.cursor()

# for item in data:
#     modele = item['modele']
#     prix= item['prix']
#     image = item['image']

#     # Exécuter la requête SQL d'insertion
#     cursor = conn.cursor()
#     query = "INSERT INTO voiture (modele, prix, image) VALUES (%s, %s, %s)"
#     values = (modele, prix, image)
#     cursor.execute(query, values)
#     conn.commit()

# # Fermer la connexion à la base de données
# conn.close()






#  CREATE TABLE vols (                     
#     id SERIAL PRIMARY KEY,
#     compagnie VARCHAR(100) NOT NULL,
#     heuredep VARCHAR(20) NOT NULL,
#     aeroportdep VARCHAR(20) NOT NULL,
#     heurearr VARCHAR(20) NOT NULL,
#     aeroportarr VARCHAR(20) NOT NULL,
#     prix VARCHAR(20) NOT NULL
# );

with open('fichier_vol.json', 'r') as file:
    data = json.load(file)


cursor = conn.cursor()


for item in data:
    compagnie = item['compagnie']
    heuredep = item['heuredep']
    aeroportdep = item['aeroportdep']
    heurearr = item['heurearr']
    aeroportarr = item['aeroportarr']
    prix = item['prix']

#     # Exécuter la requête SQL d'insertion
    cursor = conn.cursor()
    query = "INSERT INTO vols (compagnie, heuredep, aeroportdep, heurearr, aeroportarr,prix) VALUES (%s, %s, %s, %s, %s,%s)"
    values = (compagnie, heuredep, aeroportdep, heurearr, aeroportarr,prix)
    cursor.execute(query, values)
    conn.commit()

# # Fermer la connexion à la base de données
conn.close()








#  CREATE TABLE chambre (
#     id SERIAL PRIMARY KEY,
#     ville VARCHAR(100) NOT NULL,
#     nom_hotel VARCHAR(100) NOT NULL,
#     prix VARCHAR(20) NOT NULL,
#     note VARCHAR(20),
#     localisation VARCHAR(100)
# );


# with open('data.json', 'r') as file:
#     data = json.load(file)

# cursor = conn.cursor()

# for item in data:
#     ville = item['Ville']
#     nom_hotel = item['NomHotel']
#     prix = item['Prix']
#     note = item['Note']
#     localisation = item['localisa']

#     # Exécuter la requête SQL d'insertion
#     cursor = conn.cursor()
#     query = "INSERT INTO chambre (ville, nom_hotel, prix, note, localisation) VALUES (%s, %s, %s, %s, %s)"
#     values = (ville, nom_hotel, prix, note, localisation)
#     cursor.execute(query, values)
#     conn.commit()

# # Fermer la connexion à la base de données
# conn.close()
