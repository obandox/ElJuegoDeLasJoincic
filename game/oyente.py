import pygame
from pygame.locals import *
from random import randrange
from assets import load_image

from util import clamp


OYENTE_DESPIERTO=0
OYENTE_NORMAL=1000
OYENTE_ABURRRIDO=2000
OYENTE_DISTRAIDO=3000
OYENTE_DORMIDO=4000

ESTADOS_NOMBRE= {
          OYENTE_DESPIERTO : "despierto" ,  
          OYENTE_ABURRRIDO : "aburrido" ,      
          OYENTE_DISTRAIDO : "distraido" ,      
          OYENTE_DORMIDO : "dormido" ,      
}


MAX_TICK= 60 

class Oyente(pygame.sprite.Sprite):
    
    state = OYENTE_DESPIERTO
    last_state= -1    
    
    ticks = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect=Rect(0,0,80,96)
        self.original= load_image("oyente%d.png" % (1+randrange(5)) )
        self.image = self.original
        self.state= OYENTE_DESPIERTO
        self.renderState();
    
    def renderState(self):
        self.image = self.original.copy()
        if self.state != OYENTE_NORMAL:
            self.image.blit(load_image("state_%s.png" %  ESTADOS_NOMBRE[self.state]  ), (0,0))
        
    def update(self,game):
        self.ticks+=1
        if MAX_TICK <= self.ticks:
            self.ticks=0        
            if self.state != self.last_state:
                self.renderState()
                self.last_state=self.state
            if randrange(6) == 1 :
                self.state+=OYENTE_DESPIERTO
                self.state= clamp(self.state , OYENTE_DESPIERTO, OYENTE_DORMIDO  )

class  Coordinador(Oyente):
    pass
        
        