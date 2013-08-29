#Imports
import pygame
import re #Fixes stupid cx_Freeze bug.
from pygame.locals import *
import sys, os, traceback, random

######### Used to detect screen resolution. Requires different methods on other Platforms #########

import ctypes
user32 = ctypes.windll.user32
screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

###################################################################################################


pygame.display.init()
pygame.font.init()
#screen_size = [1280, 800] #Test resolution.

surface = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)

pygame.display.set_caption("Game Base")

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)

def drawText(string, posx, posy, size, aa, shadow = None, font = None):

    if shadow is None:
        shadow = 0
        
    if font is None:
        font = "Arial"
        
    try:
        font = pygame.font.Font(font,size)
    except IOError:
        try:
            font = pygame.font.SysFont(font, size)
        except IOError:
            font = pygame.font.Font(None, size)
            aa = 1
    if shadow == 1:
        surface.blit(font.render(string, aa,(100,100,100)), (posx + size *0.1 ,posy + size * 0.1))
        
    surface.blit(font.render(string, aa,(255,255,255)), (posx,posy))

def framecounter(): #Display FPS.

    drawText("FPS: " + str(round(float(clock.get_fps()) ) ), 0, 0, 22, 0, 1, "Silkscreen")

def get_input():
    
    for event in pygame.event.get():
        if event.type == QUIT: return False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: return False
    return True

def overlay():

    drawText("Game Base", 0, 22, 22, 0, 1, "Silkscreen")

def draw():

    surface.fill((50,0,0))
    
    

def main():
    global clock
    clock = pygame.time.Clock()
    random.seed()
    while True:
        if not get_input(): break
        draw()
        framecounter()
        overlay()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

        
if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
