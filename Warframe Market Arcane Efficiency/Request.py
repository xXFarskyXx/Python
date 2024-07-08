import requests
import json

#WF.Market: "https://api.warframe.market/v1/items" / WF Wiki: http://wf.snekw.com
endpoint = "https://api.warframe.market/v1/items/arcane_energize/dropsources"
response = requests.get(endpoint)
print(response)
reponse = response.json()

path = "dropsources.json"

with open(path , "w") as file:
    json.dump(reponse , file)

