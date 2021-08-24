from typing import Type

class Card:
    def __init__(self,
                name: str,
                tier: int,
                base_attack: int,
                base_health: int,
                positionID: int = None,
                attack: int = None,
                health: int = None,
                taunt: bool = False,
                reborn: bool = False,
                battlecry: bool = False):
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
        self.taunt = taunt
        self.reborn = reborn
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
                    positionID = self.positionID,
                    attack = self.attack,
                    health = self.health,
                    taunt = self.taunt,
                    reborn = self.reborn)
