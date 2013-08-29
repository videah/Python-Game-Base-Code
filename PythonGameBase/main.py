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

devmode = True

pygame.display.init()
pygame.font.init()
#screen_size = [1280, 800] #Test resolution.

surface = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)

pygame.display.set_caption("Game Base")

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)

font = pygame.font.SysFont('Arial',22)

cache={}
def get_cache(msg, aa): #Font cache. Work in Progress.
    
    if not msg in cache:
        
      cache[msg] = font.render(msg, aa , (255,255,255))

      if devmode is True:
          print("Added string " + msg + " to the cache.")
      
    return cache[msg]

def drawText(string, posx, posy, aa = None):

    if aa is None:
        aa = False

    msg = string

    textobj=get_cache(msg, aa)
    
    surface.blit(textobj, (posx,posy))

def framecounter(): #Display FPS.

    drawText("FPS: " + str(round(float(clock.get_fps()) ) ), 0, 0)

def get_input():
    
    for event in pygame.event.get():
        if event.type == QUIT: return False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: return False
    return True

def overlay():

    if devmode is True:
        drawText("Game Base", 0, 22, False)

def draw():

    surface.fill((50,0,0))
    
    

def main():
    global clock
    clock = pygame.time.Clock()
    random.seed()
    while True:
        if not get_input(): break
        draw()
        
        if devmode is True:
            framecounter()
        
        overlay()
        
        pygame.display.flip()
        clock.tick(60)
    if devmode is True:
        print('Cache cleared.')
    pygame.quit()

        
if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
