import pygame
import random
import math

pygame.init()

#CONSTANTS

FPS = 60
IDTH, HEIGHT = 600, 600
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT//ROWS
RECT_WIDTH = WIDTH//COLS

OUTLINE_COLOR = (187, 173, 160) #RGB
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (110, 119, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")
