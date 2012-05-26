import pygame
pygame.init()
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
import sys
import time
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
        self.background = load_image("background.png")
        self.menu_background = load_image("menu_background.png")
        self.menu_iniciar = load_image("menu_iniciar.png")
        self.menu_salir = load_image("menu_salir.png")
        
        self.gameover = load_image("gameover.png")
        self.cursor = load_image("cursor.png")
        self.arrow = load_image("arrow.png")
        self.player = Player()
        self.group = Group()
        self.protocolo = Protocolo()
        self.group.add(self.player)
        
        self.groupOyentes = Group()
        self.groupTakitos = Group()
        self.groupHUD = Group()
        self.state= GAME_INIT
        
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
        self.screen.blit(self.menu_background,(0,0))
        rect = self.screen.blit(self.menu_iniciar,(200,200))
        if rect.collidepoint(self.controller.mouse.position):    
            self.screen.blit(self.menu_iniciar,(200,200))
            if self.controller.mouse.click:
                self.state = GAME_LOOP
                self.oyentes=[
                              [0,0,0,0,0],
                              [0,0,0,0,0],
                              [0,0,0,0,0],
                              [0,0,0,0,0],
                              [0,0,0,0,0],
                             ]
                self.level=1
                self.initLevel();
                
        rect = self.screen.blit(self.menu_salir,(200,260))
        if rect.collidepoint(self.controller.mouse.position):    
            self.screen.blit(self.menu_salir,(200,260))
            if self.controller.mouse.click:
                sys.exit(0)
            
        
    
    def initLevel(self):
        count= (self.level - 1 )*2 + 4
        self.oyentes=[
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                     ]
        self.groupOyentes.empty()
        self.groupTakitos.empty()
        for i in range(count):            
            if self.hayPuesto():
                oyente=Oyente()
                self.groupOyentes.add(oyente)
                oyente.onScoreTick = self.comprobarScore
                while True:
                    i = randrange(5)
                    j = randrange(5)
                    if self.oyentes[i][j]== 0:
                        oyente.rect.x=160+(i*oyente.rect.w)
                        oyente.rect.y=j*oyente.rect.h
                        break
             
        self.time_next_level=time.time()+ 60
        self.puntos=0
    
    def comprobarScore(self, oyente):
        if oyente.state == OYENTE_DESPIERTO or \
           oyente.state == OYENTE_DISTRAIDO or \
           oyente.state == OYENTE_ABURRIDO:
            self.groupHUD.add(TextHUD(oyente.rect, "+1"))
        if oyente.state == OYENTE_DORMIDO:
            self.groupHUD.add(TextHUD(oyente.rect, "-1"))
        
    def loop(self):
        #input
        
        self.player.update(self)
        self.protocolo.update(self)
        
        for oyente in self.groupOyentes:
            oyente.update(self)
            
        for takito in self.groupTakitos:
            takito.update(self)
        
        self.groupHUD.update()
        
        #render
        self.screen.blit(self.background,(0,0))
        
        self.screen.blit(self.protocolo.image, self.protocolo.rect)
        self.groupOyentes.draw(self.screen)
        self.groupTakitos.draw(self.screen)
        self.group.draw(self.screen)
        self.groupHUD.draw(self.screen)
        
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
        	count= len(self.groupOyentes)
        	count_len=0
        	for sprite in self.groupOyentes:
        		if sprite.state <= OYENTE_NORMAL:
        			count_len+=1
        	if count_len >= count /2:
        		self.level+=1
        		self.initLevel()
        	else:
        		self.state= GAME_END
        		

    def end(self):
        self.screen.blit(self.gameover, (0,0))
    
    def update(self):
        self.controller.update()
        self.screen = pygame.display.get_surface()
        if self.state <= GAME_PAUSE:
            self.pause()   
        elif self.state <= GAME_INIT:
            self.init()
        elif self.state <= GAME_WAIT:
            self.wait()   
        elif self.state <= GAME_LOOP:
            self.loop()   
        elif self.state <= GAME_END:
            self.end()   
        if self.player.state != PLAYER_AIM:
        	self.screen.blit(self.cursor, self.controller.m.position)

    def go(self):
        while not self._quit:
            self.update()
            pygame.display.flip()
            self.clock.tick(TICKPERSEC)