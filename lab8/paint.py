import pygame

pygame.init()
running = True

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1000, 600)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)

color = BLACK
shape = 'line'

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('uPaint')
screen.fill(WHITE)

width = 1

prev, cur = None, None

font = pygame.font.SysFont('Verdana', 15)

pygame.draw.line(screen, pygame.Color('purple'), (0, 31), (WINDOW_WIDTH, 31), 5)


while running:
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 30))
    screen.blit(font.render(f'Mode: {shape}', True, BLACK), (10, 10))
    screen.blit(font.render(f'Width: {width}', True, BLACK), (310, 10))
    screen.blit(font.render(f'Color: {color}', True, BLACK), (610, 10))
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if alt_pressed and pressed[pygame.K_b]:
                color = BLUE
            if alt_pressed and pressed[pygame.K_r]:
                color = RED
            if alt_pressed and pressed[pygame.K_g]:
                color = GREEN
            if alt_pressed and pressed[pygame.K_p]:
                color = pygame.Color('purple')
            if alt_pressed and pressed[pygame.K_o]:
                color = pygame.Color('orange')
            if alt_pressed and pressed[pygame.K_i]:
                color = pygame.Color('indigo')
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'

        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, WHITE, prev, cur, width)
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                cur = pygame.mouse.get_pos()
                if shape == 'circle':
                    x = (prev[0]+cur[0])/2
                    y = (prev[1]+cur[1])/2
                    rx = abs(prev[0]-cur[0])/2
                    ry = abs(prev[1]-cur[1])/2
                    r = (rx + ry)/2
                    pygame.draw.circle(screen, color, (x, y), r, width)
                if shape == 'rectangle':
                    x = min(prev[0], cur[0])
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])
                    ly = abs(prev[1]-cur[1])
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()