import pygame
from typing import Type
from renderer import Renderer
from renderer.Renderer import eventManager
from events import EventEnums
from colors import BLACK, GRAY, WHITE, BLUE, RED, GREEN
from gui.gui_element import GUI_Element
from game.warband import Warband
from game.Card import Card
from utils.stageenums import Stage

class PlayerWarband(GUI_Element):
    def __init__(self, topLeft=(0, 0)):
        super().__init__()
        self.width, self.height = 100, 50
        self.rect = pygame.Rect(topLeft[0] - self.width // 2,
                                topLeft[1] - self.height // 2,
                                self.width, self.height)
        self.clicked = False
        self.subscribed = False
        self.warband = None
        self.ID = None
        self.attackingCard = None
        self.defendingCard = None
        self.stage = Stage.Idle

        self.FONT = pygame.font.SysFont('calibri', 15)
        self.FONTSTATS = pygame.font.SysFont('calibri', 50)
        self.FONTDMG = pygame.font.SysFont('calibri', 90)
        self.fontColor = WHITE

    def update_warband(self, turn: dict):
        self.warband = turn['warbands'][self.ID]
        try:
            self.attackingCard = turn['attackingCard']
            self.defendingCard = turn['defendingCard']
        except:
            pass

    def draw(self, dt):
        card: Type[Card]
        for i, card in enumerate(self.warband['cards']):
            rect = pygame.Rect(self.rect.x + i*250, self.rect.y, 210, 250)
            if self.attackingCard['ID'] == card:
                pygame.draw.ellipse(Renderer.screen, WHITE, (rect.x - 8, rect.y - 8, rect.w + 16, rect.h + 16))
                pygame.draw.ellipse(Renderer.screen, RED, (rect.x - 6, rect.y - 6, rect.w + 12, rect.h + 12))
            if self.defendingCard['ID'] == card:
                pygame.draw.ellipse(Renderer.screen, WHITE, (rect.x - 8, rect.y - 8, rect.w + 16, rect.h + 16))
                pygame.draw.ellipse(Renderer.screen, BLUE, (rect.x - 6, rect.y - 6, rect.w + 12, rect.h + 12))
            pygame.draw.ellipse(Renderer.screen, GRAY, rect)
            Renderer.screen.blit(self.FONT.render(self.warband['cards'][card]['name'], True, self.fontColor), (rect.x + rect.w//2 - self.FONT.size(self.warband['cards'][card]['name'])[0]//2, rect.y + rect.h//2))

            # Draw stats
            attRect = pygame.Rect(rect.x, rect.y + rect.h//2 + 60, 60, 60)
            hpRect = pygame.Rect(rect.x + rect.w - 60, rect.y + rect.h//2 + 60, 60, 60)
            pygame.draw.ellipse(Renderer.screen, GREEN, attRect)
            pygame.draw.ellipse(Renderer.screen, RED, hpRect)

            if self.stage == Stage.OnDmg or self.stage == Stage.OnDeath:
                if self.attackingCard['ID'] == card:
                    Renderer.screen.blit(self.FONTSTATS.render(str(self.warband['cards'][card]['health'] - self.attackingCard['dmgRecv']), True, self.fontColor),
                                        (hpRect.x + hpRect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                        hpRect.y + hpRect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
                    Renderer.screen.blit(self.FONTDMG.render('-' + str(self.attackingCard['dmgRecv']), True, self.fontColor),
                                        (rect.x + rect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                        rect.y + rect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
                elif self.defendingCard['ID'] == card:
                    Renderer.screen.blit(self.FONTSTATS.render(str(self.warband['cards'][card]['health'] - self.defendingCard['dmgRecv']), True, self.fontColor),
                                        (hpRect.x + hpRect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                        hpRect.y + hpRect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
                    Renderer.screen.blit(self.FONTDMG.render('-' + str(self.defendingCard['dmgRecv']), True, self.fontColor),
                                        (rect.x + rect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                        rect.y + rect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
                else:
                    Renderer.screen.blit(self.FONTSTATS.render(str(self.warband['cards'][card]['health']), True, self.fontColor),
                                        (hpRect.x + hpRect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                        hpRect.y + hpRect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
            else:
                Renderer.screen.blit(self.FONTSTATS.render(str(self.warband['cards'][card]['health']), True, self.fontColor),
                                    (hpRect.x + hpRect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[0]//2,
                                    hpRect.y + hpRect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['health']))[1]//2))
            
            Renderer.screen.blit(self.FONTSTATS.render(str(self.warband['cards'][card]['attack']), True, self.fontColor),
                                    (attRect.x + attRect.w//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['attack']))[0]//2,
                                    attRect.y + attRect.h//2 - self.FONTSTATS.size(str(self.warband['cards'][card]['attack']))[1]//2))
            
            


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
    
    
