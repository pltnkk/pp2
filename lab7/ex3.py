import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Figure")

sq = pygame.Surface((50,170))

sq.fill("Red")

run = True
while run:

    screen.blit((sq, (100,100)))
    pygame.draw.circle(screen, "Yellow", (200,150)) 


    pygame.display.update()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
            pygame.quit() 


