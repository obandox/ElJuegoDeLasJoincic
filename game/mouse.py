from pygame.locals import *
import sys

#maneja el raton con un pekenho hash de los botones y la posicion del cursor
class Mouse:
    def __init__(self):
        self.is_button_up=False
        self.is_button_down=False
        self.is_motion=False
        self.button_map={

         "CLICK":1,

         "RIGHT_CLICK":3,
         "LEFT_CLICK":1,

         "RIGHT":3,
         "LEFT":1,

         "MB1":1,
         "MB2":2,
         "MB3":3,
         "MB4":4,
         "MB5":5,
         "MB6":6,
         "MB7":7,
         "MB8":8,
         "MB9":9,
         "MB10":10,
        }
        self.position=(1,1)

    def update(self,event):
        if self.is_button_down :
           self.is_button_down=False
        if self.is_button_up:
           self.is_button_up=False
        if self.is_motion:
           self.is_motion=False
        if event.type == QUIT or  (event.type == KEYDOWN and event.key==K_ESCAPE)  :
                 sys.exit(0)
        elif event.type == MOUSEBUTTONDOWN:
                self.is_button_down = True
                self.button_map[event.button]=1
                self.position=event.pos
        elif event.type == MOUSEBUTTONUP:
                self.is_button_up = True
                self.button_map[event.button]=0
                self.position=event.pos
        elif event.type == MOUSEMOTION:
                self.is_motion = True
                self.position=event.pos

                         

    def is_pressed(self,button):
        try:
         return self.button_map[button]
        except KeyError:
         return 0


    def __getattr__(self, key):
       try:
           return object.__getattr__(self, key)
       except AttributeError:
           return self.dispatch(key)

    def dispatch(self, button):
          button=button.upper()
          t= self.is_pressed(self.button_map[button])
          if "CLICK" in button: self.button_map[self.button_map[button]]=0
          return t


