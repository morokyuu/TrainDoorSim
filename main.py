# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pygame.locals import *
import pygame

GREEN = (100,250,100)
BLUE = (180,180,250)
BLACK = (0,0,0)
WHITE = (240,240,240)

class GameState:
    def do(self,key):
        return


class GameLoop(GameState):
    def __init__(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.textSurfaceObj = font.render("push o button",True,GREEN,BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()

    def do(self,key):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.textSurfaceObj,self.textRectObj)
        self.textRectObj.center = (300,300)

        if key == pygame.K_o:
            print("open")
        else:
            pass
        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    flags = pygame.FULLSCREEN
    #DISPLAYSURF = pygame.display.set_mode(size=(640,480), display=0, depth=32, flags=pygame.FULLSCREEN)
    DISPLAYSURF = pygame.display.set_mode(size=(640,480), display=0, depth=32)

    pygame.display.set_caption('Train Door simulator')

    running = True
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
        pygame.display.update()
        clock.tick(30)

pygame.quit()
