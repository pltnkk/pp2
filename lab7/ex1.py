import pygame


pygame.init()
screen = pygame.display.set_mode((700,400))#, flags = pygame.NOFRAME)
pygame.display.set_caption("My first Game")

square = pygame.Surface((50,100))
square.fill("Red")

fo = pygame.font.Font()
run = True
while run:
    pygame.draw.circle(square, "blue", (250,150), (40))
    screen.blit(square, (25,50))
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit() 
    
