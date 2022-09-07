import os
import pygame
from .exceptions import LoadException
from .constants import ROOT_PATH

def load_sound(name):
    """ Load sound and return sound object"""
    
    fullname = os.path.join(ROOT_PATH, 'assets', 'audio', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        raise LoadException("Cannot load sound " + fullname)

    return sound

def load_png(name):
    """ Load image and return image object"""

    fullname = os.path.join(ROOT_PATH,'assets','images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()

    except pygame.error:
        raise LoadException("Cannot load image " + fullname)

    return image, image.get_rect()