import pygame,sys

pygame.init()

class Temp(pygame.sprite.Sprite):
    def __init__(self,color,initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

screen = pygame.display.set_mode([900,600])
screen.fill([255,255,255])
b = Temp([255,0,0],[50,100])
screen.blit(b.image,b.rect)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()