from pygame.locals import *
from controller import *
from assets import *
from pygame import Rect
import os
import pickle
import threading  
from random import randrange
import time


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


def clamp(value,vmin,vmax):
    return max(vmin,min(vmax,value))

class Game():
        
    def __init__(self):
        #setup
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None,24)
        pygame.mixer.init()
        pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('#ElJuegoDeLasJoincic')
        self.screen = pygame.display.get_surface()
        
        self._quit=False
        self.clock = pygame.time.Clock()
        self.controller= Controller()
        self.state = GAME_LOOP

        
    def pause(self):
        pass
    def wait(self):
        pass
    def init(self):
        pass
    
    
    def loop(self):
        pass
            
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

    def go(self):
        while not self._quit:   
            self.update()        
            pygame.display.flip()
            self.clock.tick(TICKPERSEC)