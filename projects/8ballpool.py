import pygame
import sys
from math import *
import random

pygame.init()

screen_width = 1200
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pool")

#gameloop
run = True
while run:

    #event handler 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
