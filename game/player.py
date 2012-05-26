import pygame
from pygame.locals import *
from pygame import Rect
from assets import load_image
from util import *
from takito import *
import math

RECT_ESTRADO=Rect(20,20,100,420)
MAX_TICKS=30
SPEED=(0,5)
ANGLE_SPEED=5

PLAYER_TALK=1000
PLAYER_AIM=2000
PLAYER_SHOOT=3000

MAX_DISTAN_FORCE=500
MAX_ANGLE=90
MIN_ANGLE=-90


class Player(pygame.sprite.Sprite):
    
    state=PLAYER_TALK
    
    move=list(SPEED)
    angle_move=ANGLE_SPEED
    tick=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= load_image("player.png")
        self.rect=Rect(RECT_ESTRADO.w/2,RECT_ESTRADO.h-self.image.get_width(),self.image.get_width(),self.image.get_height())
        self.arrow_angle=0
        self.force=0
    
    def update(self,game):
        if self.state == PLAYER_TALK:
            
            if RECT_ESTRADO.collidepoint(game.controller.mouse.position) and game.controller.mouse.click:
                self.state=PLAYER_AIM
            
            if self.rect.y >= RECT_ESTRADO.h or self.rect.y <= RECT_ESTRADO.y:
                self.move[1]*=-1
                self.rect.y+=self.move[1]
                
            self.rect.y+=self.move[1]
            
            
            self.rect.x=clamp(self.rect.x,RECT_ESTRADO.x,RECT_ESTRADO.w)
            self.rect.y=clamp(self.rect.y,RECT_ESTRADO.y,RECT_ESTRADO.h)
            
        elif  self.state == PLAYER_AIM:         
               
            force=( (self.rect.centerx - game.controller.mouse.position[0])**2 + (self.rect.centery - game.controller.mouse.position[1])**2 ) ** .5
            force = clamp(force,0,MAX_DISTAN_FORCE)
            self.force=  float(force)/MAX_DISTAN_FORCE

            if self.arrow_angle >= MAX_ANGLE or self.arrow_angle<= MIN_ANGLE:
                self.angle_move*=-1
                self.arrow_angle+=self.angle_move
                
            self.arrow_angle+=self.angle_move
            self.arrow_angle=clamp(self.arrow_angle,MIN_ANGLE, MAX_ANGLE)
            
            if game.controller.mouse.click:
                self.tick=0
                tak=Takito(self.rect.centerx,self.rect.centery,self.force,  self.arrow_angle)                
                game.groupTakitos.add(tak)
                self.state=PLAYER_SHOOT
                
        elif self.state == PLAYER_SHOOT:
            self.tick+=1
            if MAX_TICKS <= self.tick:
                self.state=PLAYER_TALK
                
            