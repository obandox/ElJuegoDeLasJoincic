from pygame.locals import *
from mouse import *
from keyboard import *
import sys

#se encarga de mantener actualizado las clases que controlan el raton y el teclado.. parte de contenerlas en si mismo
class Controller:
    def __init__(self):
        self.k= self.keyboard=Keyboard()
        self.m= self.mouse=Mouse()
        
    
    def update(self):      
        events=pygame.event.get()        
        for event in events:
            e=event
            if (e.type is KEYDOWN and e.key == K_RETURN
                    and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                self.toggle_fullscreen()
            self.keyboard.update(event)
            self.mouse.update(event)
            
            
    def toggle_fullscreen(self):
        screen = pygame.display.get_surface()
        tmp = screen.convert()
        caption = pygame.display.get_caption()
        cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007         
        w,h = screen.get_width(),screen.get_height()
        flags = screen.get_flags()
        bits = screen.get_bitsize()        
        pygame.display.quit()
        pygame.display.init()        
        screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
        screen.blit(tmp,(0,0))
        pygame.display.set_caption(*caption)     
        pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??     
        pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007        
        return screen
                         






   