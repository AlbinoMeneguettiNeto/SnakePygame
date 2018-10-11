import pygame
import Main
import random
import Functions
import Menu
import sys

lightgray = (211, 211, 211)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

points = 0
highscore = list()

fps = 5
pygame.init()
fpsClock = pygame.time.Clock()

SWidth, SHeight = 640, 480

GRIDSIZE = 10
GRID_WIDTH = SWidth / GRIDSIZE
GRID_HEIGHT = SHeight / GRIDSIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((SWidth, SHeight), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255, 255, 255))

clock = pygame.time.Clock()
pygame.key.set_repeat(1, 40)
screen.blit(surface, (0, 0))
