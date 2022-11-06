

import requests

headers = {'Ocp-Apim-Subscription-Key': 'bd9ed5d96b0b439489775cf52b7dce8a'}
resource_uri = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/arrivals?lang=nl&station=ut&maxJourneys=5"
response = requests.get(resource_uri, headers=headers)
response_data = response.json()

for items in response_data['payload']['arrivals']:
    print(str(items['origin']) + str(items['trainCategory']) + str(items['arrivalStatus']))