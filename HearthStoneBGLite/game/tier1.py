from game.Card import Card

# name, tier, att, health

class DragonspawnLieutenant(Card):
    def __init__(self):
        super().__init__("Dragonspawn Lieutenant", 1, 2, 3, taunt=True)

class AcolyteOfCThun(Card):
    def __init__(self):
        super().__init__("Acolyte Of C'Thun", 1, 2, 2, taunt=True, reborn=True)
    
    def on_death(self):
        pass

class RefreshingAnomoly(Card):
    def __init__(self):
        super().__init__("Refreshing Anomoly", 1, 1, 3)

class Alleycat(Card):
    def __init__(self):
        super().__init__("Alleycat", 1, 1, 1)
        self.summonCard = 'CAT01'