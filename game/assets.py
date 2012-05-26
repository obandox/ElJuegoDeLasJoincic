
import os
import pygame

FOLDER = "assets"

_CACHE = {}


def load_image(name, colorkey=None):
    fullname = os.path.join(os.getcwd(), FOLDER , name)
    if(fullname in _CACHE): return _CACHE[fullname]
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    _CACHE[fullname]=image
    return image