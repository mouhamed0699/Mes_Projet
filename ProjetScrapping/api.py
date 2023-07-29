# # import requests

# # params = {
# #   'access_key': 'cf37308cc908e3ed5a088eb8f160417d'
# # }

# # api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

# # api_response = api_result.json()

# # for flight in api_response['results']:
# #     if (flight['live']['is_ground'] is False):
# #         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
# #             flight['airline']['name'],
# #             flight['flight']['iata'],
# #             flight['departure']['airport'],
# #             flight['departure']['iata'],
# #             flight['arrival']['airport'],
# #             flight['arrival']['iata']))

# from amadeus import Client, ResponseError
# import json

# amadeus = Client(
#     client_id='aiUt5FXs9uKtwLkEv4t39SpzyAyxSysG',
#     client_secret='vFlL4DccHqQgqKaU'
# )

# try:
#     '''
#     Find the cheapest flights from SYD to BKK
#     '''
#     response = amadeus.shopping.flight_offers_search.get(
#         originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2023-07-10', adults=1)
    
#     # Convertir les données de réponse en format JSON
#     json_data = json.dumps(response.data)

#     # Enregistrer les données JSON dans un fichier
#     with open('flight_offers.json', 'w') as json_file:
#         json_file.write(json_data)
#         print("Les données ont été enregistrées dans flight_offers.json.")
# except ResponseError as error:
#     raise error

# import json

# # Charger les données depuis le fichier JSON
# with open('flight_offers.json', 'r') as json_file:
#     json_data = json.load(json_file)

# # Charger les correspondances aéroport depuis un fichier CSV (exemple)
# airport_data = {}
# with open('airport_codes.csv', 'r') as csv_file:
#     # Code pour lire le fichier CSV et stocker les correspondances dans airport_data

# # Charger les correspondances compagnie depuis un fichier CSV (exemple)
# airline_data = {}
# with open('airline_codes.csv', 'r') as csv_file:
#     # Code pour lire le fichier CSV et stocker les correspondances dans airline_data

# # Créer une liste pour stocker les informations des vols
# flight_info_list = []

# # Extraire les informations des segments
# for offer in json_data:
#     itineraries = offer['itineraries']
#     for itinerary in itineraries:
#         segments = itinerary['segments']
#         for segment in segments:
#             departure = segment['departure']
#             arrival = segment['arrival']
#             carrier_code = segment['carrierCode']
#             departure_time = departure['at'].split('T')[1]
#             arrival_time = arrival['at'].split('T')[1]

#             # Remplacer les codes des aéroports par les noms correspondants
#             departure_airport_code = departure['iataCode']
#             departure_airport_name = airport_data.get(departure_airport_code, '')
#             arrival_airport_code = arrival['iataCode']
#             arrival_airport_name = airport_data.get(arrival_airport_code, '')

#             # Remplacer le code de la compagnie par le nom correspondant
#             carrier_name = airline_data.get(carrier_code, '')

#             # Créer un dictionnaire avec les informations du vol
#             flight_info = {
#                 'compagnie': carrier_name,
#                 'heuredep': departure_time,
#                 'aeroportdepart': departure_airport_name,
#                 'heurearrivee': arrival_time,
#                 'aeroportarrivee': arrival_airport_name,
#                 'prixdevise': offer['price']['total'] + ' ' + offer['price']['currency']
#             }

#             # Ajouter le dictionnaire à la liste
#             flight_info_list.append(flight_info)

# # Enregistrer les informations des vols dans un fichier JSON
# with open('flight_info.json', 'w') as json_file:
#     json.dump(flight_info_list, json_file)

# print("Les informations des vols ont été enregistrées dans flight_info.json.")


from amadeus import Client, ResponseError

amadeus = Client(
    client_id='aiUt5FXs9uKtwLkEv4t39SpzyAyxSysG',
    client_secret='vFlL4DccHqQgqKaU'
)

try:
    '''
    What's the airline name for the IATA code BA?
    '''
    response = amadeus.reference_data.airlines.get()
    print(response.data)
except ResponseError as error:
    raise error