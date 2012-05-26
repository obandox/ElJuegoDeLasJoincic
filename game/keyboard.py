import pygame
from pygame.locals import *
import sys

#maneja el teclado para ello usa un hashmap con todas las teclas de este
class Keyboard:
    
    def __init__(self):
        self.is_key_up=False
        self.is_key_down=False
        self.lag=-1
        self.last_key=None
        self.key_map={}
        self.key_map["K_UNKNOWN"]=K_UNKNOWN
        self.key_map["K_FIRST"]=K_FIRST
        self.key_map["K_BACKSPACE"]=K_BACKSPACE
        self.key_map["K_TAB"]=K_TAB
        self.key_map["K_CLEAR"]=K_CLEAR
        self.key_map["K_RETURN"]=K_RETURN
        self.key_map["K_PAUSE"]=K_PAUSE
        self.key_map["K_ESCAPE"]=K_ESCAPE
        self.key_map["K_SPACE"]=K_SPACE
        self.key_map["K_EXCLAIM"]=K_EXCLAIM
        self.key_map["K_QUOTEDBL"]=K_QUOTEDBL
        self.key_map["K_HASH"]=K_HASH
        self.key_map["K_DOLLAR"]=K_DOLLAR
        self.key_map["K_AMPERSAND"]=K_AMPERSAND
        self.key_map["K_QUOTE"]=K_QUOTE
        self.key_map["K_LEFTPAREN"]=K_LEFTPAREN
        self.key_map["K_RIGHTPAREN"]=K_RIGHTPAREN
        self.key_map["K_ASTERISK"]=K_ASTERISK
        self.key_map["K_PLUS"]=K_PLUS
        self.key_map["K_COMMA"]=K_COMMA
        self.key_map["K_MINUS"]=K_MINUS
        self.key_map["K_PERIOD"]=K_PERIOD
        self.key_map["K_SLASH"]=K_SLASH
        self.key_map["K_0"]=K_0
        self.key_map["K_1"]=K_1
        self.key_map["K_2"]=K_2
        self.key_map["K_3"]=K_3
        self.key_map["K_4"]=K_4
        self.key_map["K_5"]=K_5
        self.key_map["K_6"]=K_6
        self.key_map["K_7"]=K_7
        self.key_map["K_8"]=K_8
        self.key_map["K_9"]=K_9
        self.key_map["K_COLON"]=K_COLON
        self.key_map["K_SEMICOLON"]=K_SEMICOLON
        self.key_map["K_LESS"]=K_LESS
        self.key_map["K_EQUALS"]=K_EQUALS
        self.key_map["K_GREATER"]=K_GREATER
        self.key_map["K_QUESTION"]=K_QUESTION
        self.key_map["K_AT"]=K_AT
        self.key_map["K_LEFTBRACKET"]=K_LEFTBRACKET
        self.key_map["K_BACKSLASH"]=K_BACKSLASH
        self.key_map["K_RIGHTBRACKET"]=K_RIGHTBRACKET
        self.key_map["K_CARET"]=K_CARET
        self.key_map["K_UNDERSCORE"]=K_UNDERSCORE
        self.key_map["K_BACKQUOTE"]=K_BACKQUOTE
        self.key_map["K_A"]=K_a
        self.key_map["K_B"]=K_b
        self.key_map["K_C"]=K_c
        self.key_map["K_D"]=K_d
        self.key_map["K_E"]=K_e
        self.key_map["K_F"]=K_f
        self.key_map["K_G"]=K_g
        self.key_map["K_H"]=K_h
        self.key_map["K_I"]=K_i
        self.key_map["K_J"]=K_j
        self.key_map["K_K"]=K_k
        self.key_map["K_L"]=K_l
        self.key_map["K_M"]=K_m
        self.key_map["K_N"]=K_n
        self.key_map["K_O"]=K_o
        self.key_map["K_P"]=K_p
        self.key_map["K_Q"]=K_q
        self.key_map["K_R"]=K_r
        self.key_map["K_S"]=K_s
        self.key_map["K_T"]=K_t
        self.key_map["K_U"]=K_u
        self.key_map["K_V"]=K_v
        self.key_map["K_W"]=K_w
        self.key_map["K_X"]=K_x
        self.key_map["K_Y"]=K_y
        self.key_map["K_Z"]=K_z
        self.key_map["K_DELETE"]=K_DELETE

        self.key_map["K_KP0"]=K_KP0
        self.key_map["K_KP1"]=K_KP1
        self.key_map["K_KP2"]=K_KP2
        self.key_map["K_KP3"]=K_KP3
        self.key_map["K_KP4"]=K_KP4
        self.key_map["K_KP5"]=K_KP5
        self.key_map["K_KP6"]=K_KP6
        self.key_map["K_KP7"]=K_KP7
        self.key_map["K_KP8"]=K_KP8
        self.key_map["K_KP9"]=K_KP9
        self.key_map["K_KP_PERIOD"]=K_KP_PERIOD
        self.key_map["K_KP_DIVIDE"]=K_KP_DIVIDE
        self.key_map["K_KP_MULTIPLY"]=K_KP_MULTIPLY
        self.key_map["K_KP_MINUS"]=K_KP_MINUS
        self.key_map["K_KP_PLUS"]=K_KP_PLUS
        self.key_map["K_KP_ENTER"]=K_KP_ENTER
        self.key_map["K_KP_EQUALS"]=K_KP_EQUALS
        self.key_map["K_UP"]=K_UP
        self.key_map["K_DOWN"]=K_DOWN
        self.key_map["K_RIGHT"]=K_RIGHT
        self.key_map["K_LEFT"]=K_LEFT
        self.key_map["K_INSERT"]=K_INSERT
        self.key_map["K_HOME"]=K_HOME
        self.key_map["K_END"]=K_END
        self.key_map["K_PAGEUP"]=K_PAGEUP
        self.key_map["K_PAGEDOWN"]=K_PAGEDOWN
        self.key_map["K_F1"]=K_F1
        self.key_map["K_F2"]=K_F2
        self.key_map["K_F3"]=K_F3
        self.key_map["K_F4"]=K_F4
        self.key_map["K_F5"]=K_F5
        self.key_map["K_F6"]=K_F6
        self.key_map["K_F7"]=K_F7
        self.key_map["K_F8"]=K_F8
        self.key_map["K_F9"]=K_F9
        self.key_map["K_F10"]=K_F10
        self.key_map["K_F11"]=K_F11
        self.key_map["K_F12"]=K_F12
        self.key_map["K_F13"]=K_F13
        self.key_map["K_F14"]=K_F14
        self.key_map["K_F15"]=K_F15

        self.key_map["K_NUMLOCK"]=K_NUMLOCK
        self.key_map["K_CAPSLOCK"]=K_CAPSLOCK
        self.key_map["K_SCROLLOCK"]=K_SCROLLOCK
        self.key_map["K_RSHIFT"]=K_RSHIFT
        self.key_map["K_LSHIFT"]=K_LSHIFT
        self.key_map["K_RCTRL"]=K_RCTRL
        self.key_map["K_LCTRL"]=K_LCTRL
        self.key_map["K_RALT"]=K_RALT
        self.key_map["K_LALT"]=K_LALT
        self.key_map["K_RMETA"]=K_RMETA
        self.key_map["K_LMETA"]=K_LMETA
        self.key_map["K_LSUPER"]=K_LSUPER
        self.key_map["K_RSUPER"]=K_RSUPER
        self.key_map["K_MODE"]=K_MODE

        self.key_map["K_HELP"]=K_HELP
        self.key_map["K_PRINT"]=K_PRINT
        self.key_map["K_SYSREQ"]=K_SYSREQ
        self.key_map["K_BREAK"]=K_BREAK
        self.key_map["K_MENU"]=K_MENU
        self.key_map["K_POWER"]=K_POWER
        self.key_map["K_EURO"]=K_EURO
        self.key_map["K_LAST"]=K_LAST


    def update(self,event):
        self.is_key_down=False
        self.is_key_up=False
        self.last_key = 0

        if event.type == QUIT or  (event.type == KEYDOWN and event.key==K_ESCAPE)  :
             sys.exit(0)
        elif event.type == KEYDOWN:
          self.is_key_down=True
          self.key_map[event.key]=1
        elif event.type == KEYUP:
          self.is_key_up=True
          self.key_map[event.key]=0
          self.last_key = event.key
          self.lag=-1
                         

    def is_pressed(self,key):
        if self.lag > 0:
            if self.lag > 0:
                self.lag-=1
            return False
        try:
         if self.key_map[key]==1 and self.lag == -1:
            self.lag=25
         return self.key_map[key]
        except KeyError:
         return 0


    def __getattr__(self, key):
       try:
           return object.__getattr__(self, key)
       except AttributeError:
           return self.dispatch(key)

    def dispatch(self, key):
        key=key.upper();
        if key == "ENTER" :
          return self.is_pressed(K_RETURN)
        elif "LAST_" in key:
          return self.last(key.replace("LAST_",""))          

        if('K_' in key ):
          return self.is_pressed(self.key_map[key])
        else:
          return self.is_pressed(self.key_map['K_'+key])
    def get_abc(self,str):
        if self.last_key== 0: return str
        last=self.last_key
        self.last_key = 0
        if last==K_a: return  str+"a"
        elif last==K_b: return str+"b"
        elif last==K_c: return str+"c"
        elif last==K_d: return str+"d"
        elif last==K_e: return str+"e"
        elif last==K_f: return str+"f"
        elif last==K_g: return str+"g"
        elif last==K_h: return str+"h"
        elif last==K_i: return str+"i"
        elif last==K_j: return str+"j"
        elif last==K_k: return str+"k"
        elif last==K_l: return str+"l"
        elif last==K_n: return str+"n"
        elif last==K_m: return str+"m"
        elif last==K_o: return str+"o"
        elif last==K_p: return str+"p"
        elif last==K_q: return str+"q"
        elif last==K_r: return str+"r"
        elif last==K_s: return str+"s"
        elif last==K_t: return str+"t"
        elif last==K_u: return str+"u"
        elif last==K_v: return str+"v"
        elif last==K_w: return str+"w"
        elif last==K_x: return str+"x"
        elif last==K_y: return str+"y"
        elif last==K_z: return str+"z"
        elif last==K_BACKSPACE: return str[0:-1]
        else: return str+" "
        
    
    def last(self, key):
        key=key.upper();
        if key == "ENTER" :
          if self.last_key==(K_RETURN):
            self.last_key = 0
            return 1

        if('K_' in key ):
          if self.last_key==(self.key_map[key]):
            self.last_key = 0
            return 1
        else:
          if self.last_key==(self.key_map['K_'+key]):
            self.last_key = 0
            return 1
        
