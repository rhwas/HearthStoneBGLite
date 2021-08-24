import logging
import random as r
from typing import Type
from game.warband import Warband
from utils.warbandlogic import select_attacking_card, select_defending_card, remove_card
from utils.cardlogic import inflict_damage_to_card, isCardDead

class Simulator:
    def __init__(self, warband1: Type[Warband], warband2: Type[Warband]):
        self.warband1 = warband1
        self.warband2 = warband2
        self.attackingWarband = warband1
        self.defendingWarband = warband2
        self.winner = None

    def turn(self):
        # Attack phase

        attackingCard = select_attacking_card(self.attackingWarband)
        defendingCard = select_defending_card(self.defendingWarband)

        logging.debug("[%s] Current attacking position: %i", self.attackingWarband.name, self.attackingWarband.attackingPosition)

        inflict_damage_to_card(attackingCard, defendingCard.attack)
        inflict_damage_to_card(defendingCard, attackingCard.attack)

        logging.debug("[%s] Attacking Card: %s (ID: %i) A: %i, H: %i -- Inflicts %i damage", self.attackingWarband.name, attackingCard.name, self.attackingWarband.cards.index(attackingCard), attackingCard.attack, attackingCard.health, attackingCard.attack)
        logging.debug("[%s] Defending Card: %s (ID: %i) A: %i, H: %i -- Inflicts %i damage", self.defendingWarband.name, defendingCard.name, self.defendingWarband.cards.index(defendingCard), defendingCard.attack, defendingCard.health, defendingCard.attack)

        if isCardDead(attackingCard):
            remove_card(self.attackingWarband, attackingCard)
        else:
            if self.attackingWarband.attackingPosition == self.attackingWarband.getLength():
                self.attackingWarband.attackingPosition = 0
            else:
                self.attackingWarband.attackingPosition += 1
        if isCardDead(defendingCard) and self.defendingWarband.attackingPosition > self.defendingWarband.cards.index(defendingCard):
            remove_card(self.defendingWarband, defendingCard)
            self.defendingWarband.attackingPosition -= 1
        elif isCardDead(defendingCard):
            remove_card(self.defendingWarband, defendingCard)


    def simulate(self):
        """
        Simulation of round
        """
        logging.info("[SIMULATOR] Round begins")
        turnCounter = 0

        while self.attackingWarband.getLength() > 0 and self.defendingWarband.getLength() > 0:

            logging.info("[SIMULATOR] Turn %i", turnCounter)

            logging.debug("[%s] Player1 Warband: %s", self.warband1.name, [card.name + f'({card.positionID})' + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband1.cards])
            logging.debug("[%s] Player2 Warband: %s", self.warband2.name, [card.name + f'({card.positionID})' + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband2.cards])

            self.turn()
            
            # Swap attacking warband with defending warband
            if self.attackingWarband.getLength() > 0 and self.defendingWarband.getLength() > 0:
                temp = self.attackingWarband
                self.attackingWarband = self.defendingWarband
                self.defendingWarband = temp
            
            turnCounter += 1
        
        if self.attackingWarband.getLength() == 0 and self.defendingWarband.getLength() == 0:
            self.winner = 0
        elif self.defendingWarband.getLength() == 0:
            self.winner = self.attackingWarband.name
        elif self.attackingWarband.getLength() == 0:
            self.winner = self.defendingWarband.name

        logging.debug("[%s] Attacking Warband: %s", self.attackingWarband.name, [card.name + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.attackingWarband.cards])
        logging.debug("[%s] Defending Warband: %s", self.defendingWarband.name, [card.name + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.defendingWarband.cards])

        if self.winner == 0:
            logging.info("Non one wins, its a tie")
        else:
            logging.info("Winner: %s", self.winner)