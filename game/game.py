from pygame.locals import *
from controller import Controller
from assets import load_image

from pygame import Rect
import os
import pickle
import threading  
from random import randrange
from player import *
from oyente import *
from util import *
import time
import pygame
from pygame.sprite import Group


os.environ['SDL_VIDEO_CENTERED'] = '1'


SCREEN= 640, 480
SCREEN_RECT=Rect(0,0,SCREEN[0],SCREEN[1])

#STATES
GAME_PAUSE=0
GAME_INIT=1000
GAME_WAIT=2000
GAME_LOOP=3000
GAME_END=4000






TICKPERSEC=30



class Game():
        
    def __init__(self):
        #setup
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None,24)
        self.fontColor = (0,0,0)
        pygame.mixer.init()
        pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('#ElJuegoDeLasJoincic')
        self.screen = pygame.display.get_surface()
        
        self._quit=False
        self.clock = pygame.time.Clock()
        self.controller= Controller()
        self.state = GAME_LOOP
        self.background = load_image("background.png")
        self.cursor = load_image("cursor.png")
        self.arrow = load_image("arrow.png")
        self.player = Player()
        self.group = Group()
        self.group.add(self.player)
        self.groupOyentes = Group()
        self.groupTakitos = Group()
        
        self.oyentes=[
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                     ]
        self.level=1
        self.initLevel();
        
    def pause(self):
        pass
    def wait(self):
        pass
    
    def hayPuesto(self):
        for row in self.oyentes:
            for val in row:
                if val == 0:
                    return True
        return False
    def init(self):
        pass
    
    def initLevel(self):
        count= (self.level - 1 )*2 + 4
        self.groupOyentes.empty()
        self.groupTakitos.empty()
        for i in range(count):            
            if self.hayPuesto():
                oyente=Oyente()
                self.groupOyentes.add(oyente)
                while True:
                    i = randrange(5)
                    j = randrange(5)
                    if self.oyentes[i][j]== 0:
                        oyente.rect.x=240+(i*oyente.rect.w)
                        oyente.rect.y=10+j*oyente.rect.h
                        break
             
        self.time_next_level=time.time()+ 60
        self.puntos=0
        
    def loop(self):
        #input
        
        self.player.update(self)
        
        for oyente in self.groupOyentes:
            oyente.update(self)
            
        for takito in self.groupTakitos:
            takito.update(self)
        
        #render
        self.screen.blit(self.background,(0,0))
        
        self.groupOyentes.draw(self.screen)
        self.groupTakitos.draw(self.screen)
        self.group.draw(self.screen)
        
        if self.player.state == PLAYER_AIM:
            image= pygame.transform.scale(self.arrow, ( self.arrow.get_width()+ int( MAX_DISTAN_FORCE*self.player.force) ,self.arrow.get_height() ))
            image= pygame.transform.rotate(image, self.player.arrow_angle)
            rect=image.get_rect()
            rect.centerx=self.player.rect.centerx
            rect.centery=self.player.rect.centery
            self.screen.blit(image, rect)
        
        delta_time=self.time_next_level - time.time()
        self.screen.blit( self.font.render("Faltan: %d : %d " % ( (delta_time/60) , delta_time % 60),True, self.fontColor ) , (15,15) )    
        self.screen.blit( self.font.render(" Nivel: %d  " % self.level ,True, self.fontColor ) , (565,15) )      
        self.screen.blit( self.font.render(" Puntos: %d  " % self.puntos ,True, self.fontColor ) , (365,15) )    
       
        if delta_time <= 0:
            print "game over"
        
    def end(self):
        pass
    
    def update(self):
        self.controller.update()
        if self.state <= GAME_PAUSE:
            self.pause()   
        elif self.state <= GAME_INIT:
            self.init()()   
        elif self.state <= GAME_WAIT:
            self.wait()   
        elif self.state <= GAME_LOOP:
            self.loop()   
        elif self.state <= GAME_END:
            self.end()   
        self.screen.blit(self.cursor, self.controller.m.position)

    def go(self):
        while not self._quit:   
            self.update()        
            pygame.display.flip()
            self.clock.tick(TICKPERSEC)