import os
import sys
import pygame
from typing import Callable, List, Tuple
from events import EventManager
from colors import BLACK, WOOD
# public variables
screen = None
eventManager = EventManager()

# private variables
__clock = pygame.time.Clock()
__running = True
__loopCallables: List[Callable[[float], None]] = []
__loopBackgroundCallables: List[Callable[[float], None]] = []
__loopVersionCallables: List[Callable[[float], None]] = []
__loopForegroundCallables: List[Callable[[float], None]] = []
__loopMapCallables: List[Callable[[float], None]] = []
# __initializer = PackageInitializer('Renderer')

def getScreenResolution() -> Tuple[float, float]:
    info = pygame.display.Info()
    return (info.current_w, info.current_h)

# returns how many miliseconds has passed since the last tick
def getTimeDelta() -> float:
    global __clock
    # 60 fps
    return __clock.tick(60)

# returns how many seconds has passed since the last tick
def getTimeDeltaInSeconds() -> float:
    return getTimeDelta() / 1000

def addCallableToLoop(callable: Callable[[float], None]):
    global __loopCallables
    __loopCallables.append(callable)
    # print(__loopCallables)

def addCallableToBackgroundLoop(callable: Callable[[float], None]):
    global __loopBackgroundCallables
    __loopBackgroundCallables.append(callable)

def addCallableToVersionLoop(callable: Callable[[float], None]):
    global __loopVersionCallables
    __loopVersionCallables.append(callable)

def addCallableToForegroundLoop(callable: Callable[[float], None]):
    global __loopForegroundCallables
    __loopForegroundCallables.append(callable)

def addCallableToMapLoop(callable: Callable[[float], None]):
    global __loopMapCallables
    __loopMapCallables.append(callable)

def addCallablesToLoop(callables: List[Callable[[float], None]]):
    global __loopCallables
    __loopCallables.extend(callables)

def removeCallableFromLoop(callable: Callable[[float], None]):
    global __loopCallables
    __loopCallables.remove(callable)
    # print(__loopCallables)

def removeCallableFromMapLoop(callable: Callable[[float], None]):
    global __loopMapCallables
    __loopMapCallables.remove(callable)

def removeCallableFromBackgroundLoop(callable: Callable[[float], None]):
    global __loopBackgroundCallables
    __loopBackgroundCallables.remove(callable)

def removeCallableFromForegroundLoop(callable: Callable[[float], None]):
    global __loopForegroundCallables
    __loopForegroundCallables.remove(callable)

# function that is called to quit the game
def quitGame() -> None:
    global __running
    __running = False   

def processEventsAndCallables(dt):
    eventManager.processEvents(pygame.event.get(), dt)
    for callable in __loopMapCallables: callable(dt)
    for callable in __loopBackgroundCallables: callable(dt)
    for callable in __loopForegroundCallables: callable(dt)
    for callable in __loopCallables: callable(dt)
    for callable in __loopVersionCallables: callable(dt)
    # print(__loopBackgroundCallables, __loopCallables)
    pygame.display.update()

# the main loop that runs all the games functionality every tick
def loop() -> None:
    global __running, screen
    while __running:
        dt = getTimeDelta()
        eventManager.processEvents(pygame.event.get(), dt)
        for callable in __loopMapCallables: callable(dt)
        for callable in __loopBackgroundCallables: callable(dt)
        for callable in __loopForegroundCallables: callable(dt)
        for callable in __loopCallables: callable(dt)
        pygame.display.flip()
    
    # Done! Time to quit.
    pygame.quit()
    sys.exit()

# initializes pygame and the app screen
def initializeRenderer() -> None:
    global screen, __initializer
    
    # This shouldn't have error handling. It should end program execution
    # if the error is called because it should only ever be called once at the beginning
    # of the program
    # __initializer.checkInitializtion()

    # Initialize pygame
    pygame.init()

    # Set up the drawing window
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    displayInfo = pygame.display.Info()
    # windowDimension = (displayInfo.current_w, displayInfo.current_h)
    windowDimension = (1600, 900)
    # screen = pygame.display.set_mode(windowDimension, pygame.NOFRAME)
    screen = pygame.display.set_mode(windowDimension)
    pygame.display.set_caption('Skyjo Multiplayer')
    screen.fill(WOOD)
    # Initialize gui framework
    # GuiManager.initializeGUIManager()

    # __initializer.initialized()