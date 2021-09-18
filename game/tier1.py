from game.Card import Card
import shortuuid
import json
# name, tier, att, health

t1Cards = []
t2Cards = []
t3Cards = []
t4Cards = []
t5Cards = []
t6Cards = []
AllCards = []

for i in range(0,6):
    cards = []
    with open(f'game/cards/tier{i+1}.json') as infile:
        data = json.load(infile)
        infile.close()

    for card in data["cards"]:
        if "keywordIds" in card.keys():
            keywords = card["keywordIds"]
        else:
            keywords = []


        cards.append(Card(card["name"], card["battlegrounds"]["tier"], card["attack"], card["health"], image=card["image"], keywords=keywords, text=card["text"], ID=shortuuid.ShortUUID().random(length=5)))

    AllCards.append(cards)



# class DragonspawnLieutenant(Card):
#     def __init__(self):
#         super().__init__("Dragonspawn Lieutenant", 1, 2, 3, taunt=True, ID=shortuuid.ShortUUID().random(length=5))

# class AcolyteOfCThun(Card):
#     def __init__(self):
#         super().__init__("Acolyte Of C'Thun", 1, 2, 2, taunt=True, reborn=True, ID=shortuuid.ShortUUID().random(length=5))
    
#     def on_death(self):
#         pass

# class RefreshingAnomoly(Card):
#     def __init__(self, ID=shortuuid.ShortUUID().random(length=5)):
#         super().__init__("Refreshing Anomoly", 1, 1, 3, ID=shortuuid.ShortUUID().random(length=5))

# class Alleycat(Card):
#     def __init__(self, ID=shortuuid.ShortUUID().random(length=5)):
#         super().__init__("Alleycat", 1, 1, 1, ID=shortuuid.ShortUUID().random(length=5))
#         self.summonCard = 'CAT01'

# card = DragonspawnLieutenant()

