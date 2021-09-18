import logging
import copy
import json
import pickle
from sys import exit
from random import randint
from game.tier1 import AllCards
from game.warband import Warband
from game.simulator import Simulator
from utils.warbandlogic import remove_card, select_attacking_card, select_defending_card
from utils.cardlogic import inflict_damage_to_card

# player1Warband = Warband('Player', [Alleycat(), DragonspawnLieutenant(), AcolyteOfCThun(), Alleycat(), DragonspawnLieutenant()])
# player2Warband = Warband('Computer', [Alleycat(), AcolyteOfCThun(), Alleycat(), AcolyteOfCThun(), Alleycat(), AcolyteOfCThun()])
randomWarband1 = []
randomWarband2 = []
print(len(AllCards[5]))
for i in range(0, 4):
    randomWarband1.append(AllCards[randint(0, 5)][randint(0, 5)].copy())
    randomWarband2.append(AllCards[randint(0, 5)][randint(0, 5)].copy())

player1Warband = Warband('Player', randomWarband1)
player2Warband = Warband('Computer', randomWarband2)

pickle.dump( player1Warband, open('player1.pickle', 'wb') )
pickle.dump( player2Warband, open('player2.pickle', 'wb') )

nRounds = 1
if nRounds > 10:
    logging.basicConfig(filename='main.log', level=logging.WARNING)
else:
    logging.basicConfig(filename='main.log', level=logging.DEBUG)
player1Wins = 0
player2Wins = 0
ties = 0

for i in range(0, nRounds):
    simulator = Simulator(player1Warband.copy(), player2Warband.copy())
    simulator.simulate()
    if simulator.winner == player1Warband.name:
        player1Wins += 1
    elif simulator.winner == player2Warband.name:
        player2Wins += 1
    else:
        ties += 1

print(f'{player1Warband.name} wins: {player1Wins}, win%: {player1Wins/nRounds}')
print(f'{player2Warband.name} wins: {player2Wins}, win%: {player2Wins/nRounds}')
print(f'Ties: {ties}')