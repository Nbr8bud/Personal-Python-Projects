#Paint App!

import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('PAINTO!')


def draw_menu():
    pygame.draw.rect(screen, 'gray', [0,0,WIDTH,70])

run=True
while run:
    timer.tick(fps)
    screen.fill('white')

    draw_menu()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.flip()
pygame.quit()


