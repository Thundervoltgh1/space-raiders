import pygame,sys
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("TEST GAME")
screen.fill("white")
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()