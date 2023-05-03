# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pygame.locals import *
import pygame
import math as m
import numpy as np
from enum import Enum

GREEN = (90,180,90)
MOSGREEN = (70,100,70)
BLUE = (180,180,250)
BLACK = (0,0,0)
WHITE = (240,240,240)


def mirror_x():
    return np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])


def tr(vec):
    x,y = vec[0],vec[1]
    return np.array([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1],
    ])


def rot(th):
    return np.array([
        [np.cos(th), -np.sin(th), 0],
        [np.sin(th),  np.cos(th), 0],
        [0, 0, 1],
    ])


def draw_center_rect(vec,size,color):
    pygame.draw.rect(DISPLAYSURF, color, pygame.Rect((vec[0]-size[0]/2.0,vec[1]-size[1]/2.0), size))


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


class DoorState(Enum):
    OPEN = 1
    OPENNING = 2
    CLOSE = 3
    CLOSING = 4

class GameLoop(GameState):
    def __init__(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.textSurfaceObj = font.render("o:open, c:close",True,GREEN,BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (300,430)

        self.posx = 0
        self.DOORSIZE = (140,240)
        self.WINDOWSIZE = (self.DOORSIZE[0]*0.5,self.DOORSIZE[1]*0.43)
        self.YPOS = 200
        self.count = 0
        self.state = DoorState.CLOSE
        self.STEPMAX=50

    def door(self,key):
        if self.count > 0:
            self.count += 1
            if self.count > self.STEPMAX:
                self.count = self.STEPMAX
                print("full open")
        else:
            if key == pygame.K_o:
                print("open")
                self.count += 1
            elif key == pygame.K_c:
                print("close")
                if self.state == DoorState.CLOSE:
                    self.state = DoorState.CLOSE

        self.posx = self.count / self.STEPMAX * self.DOORSIZE[0]

        game_cord = np.array([640//2, self.YPOS, 1])
        door_r = tr(game_cord) @ tr(np.array([self.posx,0])) @ np.array([self.DOORSIZE[0]//2, 0,1])
        door_l = tr(game_cord) @ mirror_x() @ tr(np.array([self.posx,0])) @ np.array([self.DOORSIZE[0]//2, 0,1])

        window_align = np.array([0,-40,1])

        draw_center_rect(door_r,self.DOORSIZE,GREEN)
        draw_center_rect(tr(window_align) @ door_r, self.WINDOWSIZE, BLUE)

        draw_center_rect(door_l,self.DOORSIZE,GREEN)
        draw_center_rect(tr(window_align) @ door_l, self.WINDOWSIZE, BLUE)

        wall_r = tr(game_cord) @ np.array([230,0,1])
        draw_center_rect(wall_r,(180,self.DOORSIZE[1]),MOSGREEN)
        wall_l = tr(game_cord) @ mirror_x() @ np.array([230,0,1])
        draw_center_rect(wall_l,(180,self.DOORSIZE[1]),MOSGREEN)


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
