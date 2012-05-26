import pygame
from pygame.locals import *
from random import randrange
from assets import load_image

from util import clamp

COLOR_TEXTO = (255, 255, 255)

OYENTE_DESPIERTO=0
OYENTE_NORMAL=1000
OYENTE_ABURRIDO=2000
OYENTE_DISTRAIDO=3000
OYENTE_DORMIDO=4000

ESTADOS_NOMBRE= {
          OYENTE_DESPIERTO : "despierto" ,  
          OYENTE_ABURRIDO : "aburrido" ,      
          OYENTE_DISTRAIDO : "distraido" ,      
          OYENTE_DORMIDO : "dormido" ,      
}


MAX_TICK= 60
TIMER_COMPROBACION = 60*3

PENALIZACION= 4

class Oyente(pygame.sprite.Sprite):
    
    state = OYENTE_DESPIERTO
    last_state= -1    
    
    ticks = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect=Rect(0,0,96,96)
        self.original= load_image("oyente%d.png" % (1+randrange(5)) )
        self.image = self.original
        self.state= OYENTE_DESPIERTO
        self.renderState()
        self.onScoreTick = None
    
    def renderState(self):
        self.image = self.original.copy()
        if self.state != OYENTE_NORMAL:
            self.image.blit(load_image("state_%s.png" %  ESTADOS_NOMBRE[self.state]  ), (0,0))
        
    def takazo(self,game):
        if self.state <= OYENTE_NORMAL:
            game.puntos-=PENALIZACION
        else:
            self.state-= OYENTE_NORMAL
        
    def update(self,game):
        self.ticks+=1
        if self.ticks % MAX_TICK == 0 and self.ticks != 0:
            if self.state != self.last_state:
                self.renderState()
                self.last_state=self.state
            if randrange(6) == 1:
                self.state+=OYENTE_NORMAL
                self.state= clamp(self.state , OYENTE_DESPIERTO, OYENTE_DORMIDO  )
        if self.ticks % TIMER_COMPROBACION == 0 and self.ticks != 0:
            if self.onScoreTick is not None:
                self.onScoreTick(self)

class TextHUD(pygame.sprite.Sprite):
    font = pygame.font.Font(None, 36)
    def __init__(self, pos, text, speed=-1):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.font.render(text, 0, COLOR_TEXTO)
        self.rect = self.image.get_rect()
        self.rect.centerx = pos.centerx
        self.rect.centery = pos.y
        self.speed = speed
        self.distance = 0
    
    def update(self):
        self.image.set_alpha(255-255*(self.distance/20.0))
        self.rect.y += self.speed
        self.distance += 1
        if self.distance >= 20:
            self.kill()
        
class  Coordinador(Oyente):
    pass
        
        