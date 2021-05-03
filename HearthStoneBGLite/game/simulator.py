import logging
import random as r

class Simulator:
    def __init__(self, warband1, warband2):
        self.attackingWarband = warband1
        self.defendingWarband = warband2
        self.winner = None
    
    def simulate(self):
        """
        Simulation of round
        """
        logging.info("[SIMULATOR] Round begins")
        turnCounter = 0
        while self.attackingWarband.length > 0 and self.defendingWarband.length > 0:
            logging.info("[SIMULATOR] Turn %i", turnCounter)
            attackingCard = self.attackingWarband.select_attacking_card()
            defendingCard = self.defendingWarband.select_defending_card()
            logging.debug("[%s] Attacking Card: %s A: %i, H: %i", self.attackingWarband.name, attackingCard.name, attackingCard.attack, attackingCard.health)
            logging.debug("[%s] Defending Card: %s A: %i, H: %i", self.defendingWarband.name, defendingCard.name, defendingCard.attack, defendingCard.health)
            
            attackingCard.receive_damage(defendingCard.attack)
            defendingCard.receive_damage(attackingCard.attack)
            logging.debug("[%s] Attacking Card: %s A: %i, H: %i -- Inflicts %i damage", self.attackingWarband.name, attackingCard.name, attackingCard.attack, attackingCard.health, attackingCard.attack)
            logging.debug("[%s] Defending Card: %s A: %i, H: %i -- Inflicts %i damage", self.defendingWarband.name, defendingCard.name, defendingCard.attack, defendingCard.health, defendingCard.attack)

            if attackingCard.isDead():
                self.attackingWarband.remove_card(attackingCard)
            if defendingCard.isDead():
                self.defendingWarband.remove_card(defendingCard)
            
            # logging.debug("[%s] Warband: %s", self.attackingWarband.cards)
            # logging.debug("[%s] Warband: %s", self.defendingWarband.cards)

            if self.attackingWarband.length > 0 and self.defendingWarband.length > 0:
                temp = self.attackingWarband
                self.attackingWarband = self.defendingWarband
                self.defendingWarband = temp
            
            turnCounter += 1
        
        if self.attackingWarband.length == 0 and self.defendingWarband.length == 0:
            self.winner = 0
        elif self.defendingWarband.length == 0:
            self.winner = self.attackingWarband.name
        elif self.attackingWarband.length == 0:
            self.winner = self.defendingWarband.name

        if self.winner == 0:
            logging.info("Non one wins, its a tie")
        else:
            logging.info("Winner: %s", self.winner)