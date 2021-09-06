import pygame
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
from colors import GRAY, LIGHTGRAY, WHITE, BLACK
from gui.gui_element import GUI_Element

class InputBox(GUI_Element):
    def __init__(self, text='', show=True, topLeft=(Renderer.getScreenResolution()[0] // 2, Renderer.getScreenResolution()[1] // 2)):
        super().__init__()
        self.width, self.height = 140, 20
        self.rect = pygame.Rect(topLeft[0] - self.width // 2,
                                topLeft[1] - self.height // 2,
                                self.width, self.height)
        self.clicked = False
        self.active = False

        self.FONT = pygame.font.SysFont('calibri', 15)
        self.fontColor = WHITE
        self.text = text

        if not show:
            self.text = ''
            self.kill()

    def draw(self, dt):
        self.color = LIGHTGRAY if self.active else GRAY
        pygame.draw.rect(Renderer.screen, BLACK, pygame.Rect(self.rect.x - 5,
                                self.rect.y - 5,
                                self.width + 10, self.height + 10))
        pygame.draw.rect(Renderer.screen, GRAY, pygame.Rect(self.rect.x - 2,
                                self.rect.y - 2,
                                self.width + 4, self.height + 4))
        pygame.draw.rect(Renderer.screen, self.color, self.rect)
        Renderer.screen.blit(self.FONT.render(self.text, True, self.fontColor), (self.rect.x + 2, self.rect.y + 2))

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
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

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