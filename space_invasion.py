import pygame,sys
pygame.init()
WIDTH,HEIGHT=900,500
screen= pygame.display.set_mode((WIDTH,HEIGHT))
image=pygame.image.load("ship1.png")
vel=5
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
def draw(red,yellow,redhealth,yellowhealth):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"white",border)
    redtxt=health.render("Health:"+str(redhealth),1,"yellow")
    yellowtxt=health.render("Health:"+str(yellowhealth),1,"yellow")
    screen.blit(redtxt,(WIDTH-redtxt.get_width()-10,10))
    screen.blit(yellowtxt,(10,10))
    screen.blit(two,(red.x,red.y))
    screen.blit(one,(yellow.x,yellow.y))
    pygame.display.update()
def main():
    red= pygame.Rect(700,250,sw,sh)
    yellow= pygame.Rect(150,250,sw,sh)
    redhealth=10
    yellowhealth=10
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        keys_pressed=pygame.key.get_pressed()
        ylwmove(keys_pressed,yellow)
        draw(red,yellow,redhealth,yellowhealth)

def ylwmove(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-vel>0: 
        yellow.x-=vel 
    if keys_pressed[pygame.K_d] and yellow.x+sw<border.x:
        yellow.x+=vel
    if keys_pressed[pygame.K_w]:
        yellow.y-=vel 
    if keys_pressed[pygame.K_s]:
        yellow.y+=vel


if __name__=="__main__":
    main()
