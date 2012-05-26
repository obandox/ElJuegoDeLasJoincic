import pygame
from pygame.locals import *
from random import randrange
from assets import load_image

from util import clamp


import math

MAX_SPEED=20

class Takito(pygame.sprite.Sprite):
    def __init__(self,x,y,force,angle):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed= MAX_SPEED  * (1+force)
        self.velocity=(self.speed* math.cos(float(angle)/180*math.pi) ,
                       -self.speed* math.sin(float(angle)/180*math.pi) )  
        
        self.image= load_image("takito.png"  )
        
        self.rect=Rect(x,y,self.image.get_width(),self.image.get_height())
        
    def update(self,game):        
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]
        
        sprite = pygame.sprite.spritecollideany (self, game.groupOyentes )
        if sprite is not None :
            try:
                sprite.takazo(game)
                self.kill()
            except:
                pass
            
            