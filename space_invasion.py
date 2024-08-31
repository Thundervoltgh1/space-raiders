import pygame,sys
pygame.init()
WIDTH,HEIGHT=900,500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
image=pygame.image.load("ship1.png")
sw,sh=55,40
imag=pygame.image.load("ship2.png")
image1=pygame.transform.scale(image,(sw,sh))
images=pygame.transform.scale(imag,(sw,sh))
one=pygame.transform.rotate(image1,90)
two=pygame.transform.rotate(images,270)
pygame.display.set_caption("SPACE RAIDERS")
screen.fill("white")
health=pygame.font.SysFont("Comicsans",20)
pygame.display.update()
spaceimg=pygame.image.load("bg.png")
space=pygame.transform.scale(spaceimg,(WIDTH,HEIGHT))
border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
#two types of functions are predefined and userdefined
def draw(red,yellow):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"white",border)
    screen.blit(two,(red.x,red.y))
    screen.blit(one,(yellow.x,yellow.y))
    pygame.display.update()
def main():
    red= pygame.Rect(700,250,sw,sh)
    yellow= pygame.Rect(150,250,sw,sh)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        draw(red,yellow)
if __name__=="__main__":
    main()
