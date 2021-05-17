import logging

from cards.tier1 import *
from game.warband import Warband
from game.simulator import Simulator
import os

os.remove("main.log")


playerWarband = Warband("Player", [DragonspawnLieutenant()])
computerWarband = Warband("Computer", [AcolyteOfCThun(), AcolyteOfCThun(), AcolyteOfCThun(), AcolyteOfCThun()])

nRounds = 1
if nRounds > 10:
    logging.basicConfig(filename='main.log', level=logging.WARNING)
else:
    logging.basicConfig(filename='main.log', level=logging.DEBUG)
playerWins = 0
computerWins = 0
ties = 0
for i in range(0, nRounds):
    simulator = Simulator(playerWarband.copy(), computerWarband.copy())
    simulator.simulate()
    if simulator.winner == playerWarband.name:
        playerWins += 1
    elif simulator.winner == computerWarband.name:
        computerWins += 1
    else:
        ties += 1

print(f'Player wins: {playerWins}, win%: {playerWins/nRounds}')
print(f'Computer wins: {computerWins}, win%: {computerWins/nRounds}')
print(f'Ties: {ties}')