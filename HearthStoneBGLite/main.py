import logging
import copy
from game.tier1 import *
from game.warband import Warband
from game.simulator import Simulator
from utils.warbandlogic import remove_card, select_attacking_card, select_defending_card
from utils.cardlogic import inflict_damage_to_card
import os

try:
    os.remove("main.log")
except:
    pass



import sys
from time import sleep
from colors import WOOD, BLACK, WHITE
import pygame
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
Renderer.initializeRenderer()
from gui.button import Button
from gui.playerwarband import PlayerWarband

VERSION = 'v0.0.1'

playerWarband = PlayerWarband(Warband('Player1',[DragonspawnLieutenant(), DragonspawnLieutenant(), AcolyteOfCThun()]), topLeft=[100, 100])
computerWarband = PlayerWarband(Warband('Player2',[Alleycat(), AcolyteOfCThun(), Alleycat(), AcolyteOfCThun()]), topLeft=[100, 600])

FONT = pygame.font.SysFont('calibri', 15)
fontColor = BLACK

def versionInfo(dt):
    Renderer.screen.blit(FONT.render(VERSION, True, fontColor), (3, Renderer.getScreenResolution()[1] - 15))

def background(dt):
    Renderer.screen.fill(WOOD)

def quitGame(event, dt):
    global running
    running = False

clock = pygame.time.Clock()
eventManager.subscribe(EventEnums.quitGame, quitGame)
def mainMenu():
    global running
    Renderer.addCallableToVersionLoop(versionInfo)
    running = True
    while True:
        dt = clock.tick(60)

        Renderer.processEventsAndCallables(dt)
        if not running: sys.exit()

running = True
# mainMenu()
while running:
    dt = clock.tick(60)

    Renderer.processEventsAndCallables(dt)

pygame.quit()
sys.exit()
# print(playerWarband.cards)
# remove_card(playerWarband, playerWarband.cards[0])
# print(playerWarband.cards)

# attackingCard = copy.deepcopy(select_attacking_card(playerWarband))
# attackingCard = select_attacking_card(playerWarband)

# print(playerWarband.cards[0].health)
# print(attackingCard.health)

# inflict_damage_to_card(attackingCard, 1)

# print(playerWarband.cards[0].health)
# print(attackingCard.health)

# print(playerWarband.cards[0])
# print(attackingCard)

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