from enum import Enum
import pygame

class EventEnums(Enum):
    user_event = pygame.USEREVENT
    keyDown = pygame.KEYDOWN
    keyUp = pygame.KEYUP
    mouseDown = pygame.MOUSEBUTTONDOWN
    mouseUp = pygame.MOUSEBUTTONUP
    mouseMotion = pygame.MOUSEMOTION
    quitGame = pygame.QUIT