import pygame



pygame.init()

width = 650
heigh = 500

sizeball = 50
radius = sizeball // 2

move = 20

xball = width // 2
yball = heigh // 2

screen = pygame.display.set_mode((width, heigh))
clock = pygame.time.Clock()

while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:

            pygame.quit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                yball -= move
            elif i.key == pygame.K_DOWN:
                yball += move
            elif i.key == pygame.K_LEFT:
                xball -= move
            elif i.key == pygame.K_RIGHT:
                xball += move 

    if xball < radius:
        xball = radius
    elif xball > width - radius:
        xball = width - radius
    elif yball < radius:
        yball = radius
    elif yball > heigh - radius:
        yball = heigh - radius

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (xball,yball), radius)

    pygame.display.update()
    clock.tick(60)
    

    