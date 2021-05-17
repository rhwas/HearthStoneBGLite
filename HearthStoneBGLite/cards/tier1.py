from cards.base import Card


class DragonspawnLieutenant(Card):
    def __init__(self):
        super().__init__("Dragonspawn Lieutenant", 1, 1, 10, taunt=True)

class AcolyteOfCThun(Card):
    def __init__(self):
        super().__init__("Acolyte Of C'Thun", 1, 2, 2, taunt=True, reborn=True)
    
    def on_death(self):
        pass

class RefreshingAnomoly(Card):
    def __init__(self):
        super().__init__("Refreshing Anomoly", 1, 1, 3)