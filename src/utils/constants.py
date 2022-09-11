from pathlib import Path
import pygame
import os

pygame.init()

W, H = 800, 600
ROOT_PATH = str(Path(__file__).parents[2])
SRC_PATH = str(Path(__file__).parents[1])

# fonts

FONT_MAIN_SCREEN = pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'Cabin-Bold.ttf'), 72) 
FONT_CAPTION_TEXT =  pygame.font.Font(os.path.join(ROOT_PATH, 'assets', 'fonts', 'Cabin-Bold.ttf'), 48) 