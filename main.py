# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pygame.locals import *
import pygame
import math as m

GREEN = (100,250,100)
BLUE = (180,180,250)
BLACK = (0,0,0)
WHITE = (240,240,240)

class GameState:
    def do(self,key):
        return


class Title(GameState):
    def __init__(self):
        font = pygame.font.Font('freesansbold.ttf', 100)
        self.textSurfaceObj = font.render("Train Door",True,GREEN,BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (300, 170)

        font = pygame.font.Font('freesansbold.ttf', 60)
        self.messageSurfaceObj = font.render("HIT SPACE KEY",True,BLACK)
        self.messageRectObj = self.messageSurfaceObj.get_rect()
        self.messageRectObj.center = (300, 280)

    def do(self,key):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.textSurfaceObj, self.textRectObj)
        DISPLAYSURF.blit(self.messageSurfaceObj, self.messageRectObj)

        if key == pygame.K_SPACE:
            print("start")
            return True
        return False


class GameLoop(GameState):
    def __init__(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.textSurfaceObj = font.render("o:open, c:close",True,GREEN,BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (300,430)

        self.count = 0
        self.posx = 0

    def door(self,key):
        WIDTH = 140
        HEIGHT = 240
        DOORSIZE = (WIDTH,HEIGHT)
        WINDOWSIZE = (WIDTH*0.43,HEIGHT*0.43)
        YPOS = 80

        if key == pygame.K_o:
            print("open")
            self.posx = WIDTH
        elif key == pygame.K_c:
            print("close")
            self.posx = 0

        pygame.draw.rect(DISPLAYSURF,GREEN,pygame.Rect((640//2-WIDTH - self.posx,YPOS),DOORSIZE))
        pygame.draw.rect(DISPLAYSURF,BLUE,pygame.Rect((640//2-WIDTH - self.posx,YPOS),WINDOWSIZE))
        pygame.draw.rect(DISPLAYSURF,GREEN,pygame.Rect((640//2 + self.posx,YPOS),DOORSIZE))
        pygame.draw.rect(DISPLAYSURF,BLUE,pygame.Rect((640//2 + self.posx,YPOS),WINDOWSIZE))

        self.count += 1


    def do(self,key):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.textSurfaceObj,self.textRectObj)
        self.door(key)

        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    flags = pygame.FULLSCREEN
    #DISPLAYSURF = pygame.display.set_mode(size=(640,480), display=0, depth=32, flags=pygame.FULLSCREEN)
    DISPLAYSURF = pygame.display.set_mode(size=(640,480), display=0, depth=32)

    pygame.display.set_caption('Train Door simulator')

    running = True
    #g = Title()
    g = GameLoop()

    while running:
        key = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("quit")
                    running = False
                else:
                    key = event.key

        g.do(key)
#        if g.do(key):
#            g = GameLoop()
        pygame.display.update()
        clock.tick(30)

pygame.quit()
