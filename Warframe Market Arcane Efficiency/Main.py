import json

class arcane:
    def __init__(self , name , location , dissolution):
        self.name = name
        self.location = location
        self.dissolution = dissolution


with open("item.json" , "r") as data:
    payload = json.load(data)
with open("wiki.json" , "r") as data:
    wiki = json.load(data)

#print(wiki["data"]["Arcanes"]["Eternal Eradicate"])

# {'UpgradeTypes': ['WEAPON_DAMAGE_AMOUNT'], 
# 'MaxRank': 5, 
# 'InternalName': '/Lotus/Upgrades/CosmeticEnhancers/Zariman/OperatorOnOperatorAbilityIncreaseDamage', 
# 'IsRefreshable': True, 
# 'Name': 'Eternal Eradicate', 
# 'CodexSecret': False, 'Type': 'Amp', 
# 'Link': 'Eternal Eradicate', 
# 'Rarity': 'Rare', 
# 'IncompatibilityTags': ['OPERATOR_SUIT'], 
# 'Description': '+60% Damage to Amps for 8s', 
# 'Introduced': '31.5', 
# 'Dissolution': 22, 
# 'Image': 'EternalEradicate.png', 
# 'Icon': 'EternalEradicate64x.png', 
# 'Criteria': 'On Operator Ability'}


arcanes = [i for i in wiki["data"]["Arcanes"].values() if "InternalName" in i]
zariman = [i["Name"] for i in arcanes if "Zariman" in i["InternalName"].split("/")]
fake = ["Arcane Steadfast" , "Arcane Tanker" , "Arcane Double Back"]
eidolon = [i["Name"] for i in arcanes if "Arcane" in i["Name"].split() and i["Name"] not in fake]
cavia = [i["Name"] for i in arcanes if "Melee" in i["Name"].split()]
print(cavia)

#print(zariman)

