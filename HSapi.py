import requests
import json
from blizzardapi import BlizzardApi

f = open('utils/APIClient.json',)
data = json.load(f)

api_client = BlizzardApi(data['client_id'], data['client_secret'])


for i in range(0,6):

    data = api_client.hearthstone.game_data.search_cards("eu","en_US", game_mode="battlegrounds", tier=i+1, page=1)

    with open(f'game/cards/tier{i+1}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

