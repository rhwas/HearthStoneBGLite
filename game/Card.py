from typing import Type, List, Dict
import shortuuid
import re
import copy

class Card:
    def __init__(self,
                name: str,
                tier: int,
                base_attack: int,
                base_health: int,
                image: str = '',
                keywords: List = [],
                text: str = "",
                ID: str = shortuuid.ShortUUID().random(length=5),
                positionID: int = None,
                attack: int = None,
                health: int = None,
                attributes: Dict = None):
        """
        Base minion class of which all normal minions and tokens should inherit from, and they can override certain triggers to implement custom behaviour.
        Important to note is that all the "base_*" arguments should be used in implementing the normal minions and that the non-base versions should be used
        for specific instances of the normal minions, so for the simulations itself in which case they can be different than their base type.

        Arguments:
            name {str} -- Name of the card
            rank {int} -- Rank of the card
            base_attack {int} -- Base attack of the non-golden version
            base_defense {int} -- Base defense of the non-golden version

        Keyword Arguments:
            taunt {bool} -- Standard Taunt (default: {False})
            reborn {bool} -- Standard Reborn (default: {False})
        """
        self.attributeIDs = {3: "divineshield", 1: "taunt", 4: "charge", 8: "battlecry", 10: "freeze", 11: "windfury", 12: "deathrattle", 17: "immune", 21: "discover", 32: "poisonous", 34: "adapt", 66: "magnetic", 78: "reborn", 92: "atstartofcombat", 99: "frenzy", 109: "bloodgem", 196: "refresh", 197: "refresh", 198: "avenge"}
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = {"divineshield": False, "taunt": False, "charge": False, "battlecry": False, "freeze": False, "windfury": False, "deathrattle": False, "immune": False, "discover": False, "poisonous": False, "adapt": False, "magnetic": False, "reborn": False, "atstartofcombat": False, "frenzy": False, "bloodgem": False, "refresh": False, "avenge": False}
            self.keywords = keywords
            for keyword in self.keywords:
                self.attributes[self.attributeIDs[keyword]] = True
        
        self.text = text

        self.ID = ID
        self.name = name
        self.tier = tier
        self.base_attack = base_attack
        self.base_health = base_health
        self.positionID = positionID
        if attack == None:
            self.attack = self.base_attack
        else: self.attack = attack
        if health == None:
            self.health = self.base_health
        else: self.health = health
    
        self.isDead = False
    
    def copy(self):
        """
        Create a copy of the current state of the card.
        
        Returns:
            Card -- copy of the card
        """
        return Card(name = self.name,
                    tier = self.tier,
                    base_attack = self.base_attack,
                    base_health = self.base_health,
                    ID = shortuuid.ShortUUID().random(length=5),
                    positionID = self.positionID,
                    attack = self.attack,
                    health = self.health,
                    attributes=copy.deepcopy(self.attributes))
