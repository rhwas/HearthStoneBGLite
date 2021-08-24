from typing import TypeVar, Generic, List, Type
import random as r

class Warband:
    def __init__(self, name:str, cards: List):
        """
        Base class for a player warband. A warband consists of a maximum of 7 cards.
        These cards are considered active and placed on the battlefield in front of the player.

        Arguments:
            arg {type} -- description

        Keyword Arguments:
            arg {type} -- description (default: {value})
        """
        self.positionID = [0, 1, 2, 3, 4, 5, 6]
        self.name = name
        self.cards = []
        for c in cards:
            c.positionID = self.positionID.pop(0)
            self.cards.append(c)
        self.attackingPosition = 0
        self.attackingCard = None
        self.defendingCard = None
    
    def getLength(self) -> int:
        return len(self.cards)
    
    def getTaunts(self) -> List:
        return [idx for idx, card in enumerate(self.cards) if card.taunt]

    def copy(self):
        """
        Copy current warband.

        Returns:
            Warband {Warband()} -- copy of current warband state
        """
        return Warband(name=self.name, cards=[card.copy() for card in self.cards])
