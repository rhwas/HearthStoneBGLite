import logging
import random as r
from typing import Type
import os
import glob
from game.warband import Warband
import shortuuid
import json
from utils.warbandlogic import select_attacking_card, select_defending_card, remove_card, kill_card
from utils.cardlogic import inflict_damage_to_card, isCardDead


class Simulator:
    def __init__(self, warband1: Type[Warband], warband2: Type[Warband]):
        self.warband1 = warband1
        self.warband2 = warband2
        # self.attackingWarband = warband1
        # self.defendingWarband = warband2
        self.winner = None
        self.turnCounter = 1

        self.data = {}
        self.data['turn'] = {}
        self.data['turn']['1'] = {'warbands': {self.warband1.ID: {'cards': {}}, 
                            self.warband2.ID: {'cards': {}}}}
        
        for w in [self.warband1, self.warband2]:
            for c in w.cards:
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID] = {'name': c.name}
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['tier'] = c.tier
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['base_attack'] = c.base_attack
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['base_health'] = c.base_health
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['positionID'] = c.positionID
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['attack'] = c.attack
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['health'] = c.health
                self.data['turn']['1']['warbands'][w.ID]['cards'][c.ID]['attributes'] = c.attributes
        

    def turn(self, warband1, warband2, attacker):
        # Attack phase
        
        if attacker == 0:
            attackingWarband = warband1
            defendingWarband = warband2
            
        else:
            attackingWarband = warband2
            defendingWarband = warband1
        
        attackingCard = select_attacking_card(attackingWarband)
        defendingCard = select_defending_card(defendingWarband)
        if self.turnCounter > 1:
            attackingWarband.attackingPosition += 1
            if attackingWarband.attackingPosition >= attackingWarband.getLength():
                attackingWarband.attackingPosition = 0

        logging.debug("[%s] Current attacking position: %i", attackingWarband.name, attackingWarband.attackingPosition)

        inflict_damage_to_card(attackingCard, defendingCard.attack)
        inflict_damage_to_card(defendingCard, attackingCard.attack)

        # Write Replay
        self.data['turn'][f'{self.turnCounter}']['attackingCard'] = {'ID': attackingCard.ID, 'dmgRecv': defendingCard.attack}
        self.data['turn'][f'{self.turnCounter}']['defendingCard'] = {'ID': defendingCard.ID, 'dmgRecv': attackingCard.attack}

        logging.debug("[%s] Attacking Card: %s (ID: %i) A: %i, H: %i -- Inflicts %i damage", attackingWarband.name, attackingCard.name, attackingWarband.cards.index(attackingCard), attackingCard.attack, attackingCard.health, attackingCard.attack)
        logging.debug("[%s] Defending Card: %s (ID: %i) A: %i, H: %i -- Inflicts %i damage", defendingWarband.name, defendingCard.name, defendingWarband.cards.index(defendingCard), defendingCard.attack, defendingCard.health, defendingCard.attack)

        if isCardDead(attackingCard):
            kill_card(attackingWarband, attackingCard)
            
        if isCardDead(defendingCard):
            kill_card(defendingWarband, defendingCard)
        
        print(f'attPos: {attackingWarband.attackingPosition}, defPos: {defendingWarband.attackingPosition}')
            


    def simulate(self):
        """
        Simulation of round
        """
        logging.info("[SIMULATOR] Round begins")
        attacker = 0
        while self.warband1.getLength() > 0 and self.warband2.getLength() > 0:

            logging.info("[SIMULATOR] Turn %i", self.turnCounter)
            
            logging.debug("[%s] Player1 Warband: %s", self.warband1.name, [card.name + f'({card.positionID})' + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband1.cards])
            logging.debug("[%s] Player2 Warband: %s", self.warband2.name, [card.name + f'({card.positionID})' + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband2.cards])

            self.turn(self.warband1, self.warband2, attacker)
            
            # # Swap attacking warband with defending warband
            # if self.attackingWarband.getLength() > 0 and self.defendingWarband.getLength() > 0:
            #     temp = self.attackingWarband
            #     self.attackingWarband = self.defendingWarband
            #     self.defendingWarband = temp
            
            self.turnCounter += 1
            self.data['turn'][f'{self.turnCounter}'] = {'warbands': {self.warband1.ID: {'cards': {}}, 
                            self.warband2.ID: {'cards': {}}}}
                        
            for w in [self.warband1, self.warband2]:
                for c in w.cards:
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID] = {'name': c.name}
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['tier'] = c.tier
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['base_attack'] = c.base_attack
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['base_health'] = c.base_health
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['positionID'] = c.positionID
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['attack'] = c.attack
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['health'] = c.health
                    self.data['turn'][f'{self.turnCounter}']['warbands'][w.ID]['cards'][c.ID]['attributes'] = c.attributes
            
            if attacker == 0:
                attacker = 1
            elif attacker == 1:
                attacker = 0
        
        if self.warband1.getLength() == 0 and self.warband2.getLength() == 0:
            self.winner = 0
        elif self.warband2.getLength() == 0:
            self.winner = self.warband1.name
        elif self.warband1.getLength() == 0:
            self.winner = self.warband2.name

        logging.debug("[%s] Attacking Warband: %s", self.warband1.name, [card.name + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband1.cards])
        logging.debug("[%s] Defending Warband: %s", self.warband2.name, [card.name + ': ' + str(card.attack) + ', ' + str(card.health) for card in self.warband2.cards])

        if self.winner == 0:
            logging.info("Non one wins, its a tie")
        else:
            logging.info("Winner: %s", self.winner)
        
        files = glob.glob('replays/*')
        for f in files:
            os.remove(f)
        
        with open('replays/' + shortuuid.ShortUUID().random(length=5) + '.json', 'w') as f:
            json.dump(self.data, f, indent=2)