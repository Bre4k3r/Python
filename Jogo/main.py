import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1280, 640))
running = True
clock = pygame.time.Clock()
black = (0,0,0)

timer = 0

b1 = pygame.image.load('capybara.jpg').convert_alpha()
b2 = pygame.image.load('capybara.jpg').convert_alpha()


class Button():
    def __init__(self,x,y,image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                time.sleep(0.1)
                print('Clicked')
        screen.blit(self.image, (self.rect.x, self.rect.y))

botao1 = Button(100,200,b1,0.8)
botao2 = Button(450,200,b2,0.8)

while running:

    screen.fill("white")
    botao1.draw()
    botao2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()