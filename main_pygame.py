import os, sys, json, glob, logging, copy, pygame, pickle
from time import sleep
from colors import WOOD, BLACK, WHITE
from renderer.Renderer import eventManager
from renderer import Renderer
from events import EventEnums
Renderer.initializeRenderer()
from gui.button import Button
from game.tier1 import *
from game.warband import Warband
from game.simulator import Simulator
from gui.playerwarband import PlayerWarband
from utils.cardlogic import inflict_damage_to_card
from utils.warbandlogic import remove_card, select_attacking_card, select_defending_card
from utils.stageenums import Stage

try:
    os.remove("main.log")
except:
    pass

FONT = pygame.font.SysFont('calibri', 15)
fontColor = BLACK

# Initialize GUI elements
nextStep = Button(text='Next', topLeft=(850, 800))
reset = Button(text='Reset', topLeft=(1100, 800))
previousStep = Button(text='Previous', topLeft=(700, 800))

# Load replays
replays = glob.glob('replays/*')
f = open(replays[0])
replay = json.load(f)

# Initialize warband classes & load them
player1Warband = PlayerWarband(topLeft=(200, 100))
player2Warband = PlayerWarband(topLeft=(200, 500))
playerWarbands = [player1Warband, player2Warband]
for i, w in enumerate(replay['turn']['1']['warbands']):
    playerWarbands[i].ID = w
    playerWarbands[i].update_warband(replay['turn']['1'])

global turn, stage
stage = Stage.Idle
turn = '1'


def background(dt):
    Renderer.screen.fill(WOOD)


def game(dt):

    global turn, stage

    if reset.isClicked():
        turn = '1'
        stage = Stage.Idle
        for i, w in enumerate(replay['turn'][turn]['warbands']):
            playerWarbands[i].update_warband(replay['turn'][turn])
            playerWarbands[i].stage = stage
    
    if nextStep.isClicked():
        if stage == Stage.Idle:
            stage = Stage.OnDeath
        # elif stage == Stage.onAtt:
        #     stage = Stage.Att
        # elif stage == Stage.Att:
        #     stage = Stage.OnDmg
        # elif stage == Stage.OnDmg:
        #     stage = Stage.OnDeath
        elif stage == Stage.OnDeath:
            stage = Stage.Idle
            turn = str(int(turn) + 1)
            try:
                for i, w in enumerate(replay['turn'][turn]['warbands']):
                    playerWarbands[i].update_warband(replay['turn'][turn])
            except:
                pass
        try:
            for i, w in enumerate(replay['turn'][turn]['warbands']):
                playerWarbands[i].stage = stage
        except:
            pass
    
    if previousStep.isClicked():
        stage = Stage.Idle
        turn = str(int(turn) - 1)
        if turn == '0': turn = '1'
        try:
            for i, w in enumerate(replay['turn'][turn]['warbands']):
                playerWarbands[i].update_warband(replay['turn'][turn])
                playerWarbands[i].stage = stage
        except:
            pass


def quitGame(event, dt):

    global running

    running = False


clock = pygame.time.Clock()
eventManager.subscribe(EventEnums.quitGame, quitGame)

Renderer.addCallableToBackgroundLoop(background)
Renderer.addCallableToLoop(game)


running = True
while running:

    dt = clock.tick(60)
    
    Renderer.processEventsAndCallables(dt)

pygame.quit()
sys.exit()