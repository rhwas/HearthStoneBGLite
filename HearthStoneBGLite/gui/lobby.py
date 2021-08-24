import pygame
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
from colors import GRAY, LIGHTGRAY, WHITE, BLACK
from gui.gui_element import GUI_Element

class Lobby(GUI_Element):
    def __init__(self, show=True, topLeft=(Renderer.getScreenResolution()[0] // 2, Renderer.getScreenResolution()[1] // 2)):
        super().__init__()
        self.width, self.height = 200, 400
        self.rect = pygame.Rect(topLeft[0] - self.width // 2,
                                topLeft[1] - self.height // 2,
                                self.width, self.height)
        self.clicked = False

        self.players = {}
        self.FONT = pygame.font.SysFont('calibri', 15)
        self.fontColor = WHITE

        if not show: self.kill()

    def draw(self, dt):
        pygame.draw.rect(Renderer.screen, GRAY, self.rect)
        Renderer.screen.blit(self.FONT.render("Lobby:", True, self.fontColor), 
                            (self.rect.x + self.rect.w // 2 - self.FONT.size("Lobby:")[0] // 2,
                            self.rect.y - self.FONT.size("Lobby:")[1] + 30))
        for i, player in enumerate(self.players):
            Renderer.screen.blit(self.FONT.render(self.players[player]['name'], True, self.fontColor),
                            (self.rect.x + 20,
                            self.rect.y + 60 + i*20))
    
    def isHovering(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
    
    def onMouseUp(self, event, dt):
        if self.isHovering():
            self.clicked = True
        else:
            self.clicked = False
    
    def onMouseDown(self, event, dt):
        pass

    def isClicked(self):
        if self.clicked:
            self.clicked = False
            return True
        return False
    
    def subscribe(self):
        eventManager.subscribe(EventEnums.mouseUp, self.onMouseUp)
        eventManager.subscribe(EventEnums.mouseDown, self.onMouseDown)
    
    def unsubscribe(self):
        eventManager.unsubscribe(EventEnums.mouseUp, self.onMouseUp)
        eventManager.unsubscribe(EventEnums.mouseDown, self.onMouseDown)