import os
import sys
from time import sleep
from colors import WOOD, BLACK, WHITE
import pygame
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
Renderer.initializeRenderer()
from gui.button import Button

VERSION = 'v0.0.1'

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
mainMenu()
while running:
    dt = clock.tick(60)

    Renderer.processEventsAndCallables(dt)

pygame.quit()
sys.exit()