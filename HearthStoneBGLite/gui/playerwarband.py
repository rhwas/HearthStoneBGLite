import pygame
from typing import Type
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
from colors import BLACK, GRAY, WHITE
from gui.gui_element import GUI_Element
from game.warband import Warband
from game.Card import Card

class PlayerWarband(GUI_Element):
    def __init__(self, warband: Type[Warband], topLeft=(0, 0)):
        super().__init__()
        self.width, self.height = 100, 50
        self.rect = pygame.Rect(topLeft[0] - self.width // 2,
                                topLeft[1] - self.height // 2,
                                self.width, self.height)
        self.clicked = False
        self.subscribed = False
        self.warband = warband

        self.FONT = pygame.font.SysFont('calibri', 15)
        self.fontColor = WHITE

    def set_warband(self, warband: Type[Warband]):
        self.warband = warband

    def draw(self, dt):
        card: Type[Card]
        for i, card in enumerate(self.warband.cards):
            rect = pygame.Rect(self.rect.x + i*200, self.rect.y, 150, 70)
            pygame.draw.rect(Renderer.screen, GRAY, rect)
            Renderer.screen.blit(self.FONT.render(card.name, True, self.fontColor), (rect.x + 2, rect.y + 2))

    def isHovering(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
    
    def onMouseUp(self, event, dt):
        if self.isHovering():
            self.clicked = True
            self.active = True
        else:
            self.clicked = False
            self.active = False
    
    def onMouseDown(self, event, dt):
        pass

    def onKeyPress(self, event, dt):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                pass

    def isClicked(self):
        if self.clicked:
            self.clicked = False
            return True
        return False
    
    def subscribe(self):
        eventManager.subscribe(EventEnums.mouseUp, self.onMouseUp)
        eventManager.subscribe(EventEnums.mouseDown, self.onMouseDown)
        eventManager.subscribe(EventEnums.keyDown, self.onKeyPress)
    
    def unsubscribe(self):
        eventManager.unsubscribe(EventEnums.mouseUp, self.onMouseUp)
        eventManager.unsubscribe(EventEnums.mouseDown, self.onMouseDown)
        eventManager.unsubscribe(EventEnums.keyDown, self.onKeyPress)
    
    
