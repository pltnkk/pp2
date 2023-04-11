import math

import pygame

pygame.init() #init
running = True

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1000, 600) #window size
RED = (255, 0, 0) #colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)   #window

color = BLACK   # default color of shapes
shape = 'line'  # mode, which shae to draw

clock = pygame.time.Clock()
fps = 60

pygame.display.set_caption('uPaint')  # name of window
screen.fill(WHITE)

prev, cur = None, None  # current and previous points
width = 1


font = pygame.font.SysFont('Verdana', 15)  # font

pygame.draw.line(screen, pygame.Color('purple'), (0, 31), (WINDOW_WIDTH, 31), 5)   # splitting line

while running:
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 30))  # updating status
    screen.blit(font.render(f'Mode: {shape}', True, BLACK), (10, 10))  # current shape
    screen.blit(font.render(f'Width: {width}', True, BLACK), (310, 10))  # current width
    screen.blit(font.render(f'Color: {color}', True, BLACK), (610, 10))  # current color
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]  # press ctrl
        alt_pressed = pressed[pygame.K_RALT] or pressed[pygame.K_LALT]  # press alt

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:  # change width
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if alt_pressed and pressed[pygame.K_b]:  # change color
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
            if ctrl_pressed and pressed[pygame.K_c]:  # change shape
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_s]:
                shape = 'square'
            if ctrl_pressed and pressed[pygame.K_t]:
                shape = 'equilateral_triangle'
            if ctrl_pressed and pressed[pygame.K_m]:
                shape = 'right_triangle'
            if ctrl_pressed and pressed[pygame.K_h]:
                shape = 'rhombus'
        if shape == 'line' or shape == 'eraser':  # line and erasor have approximate same algorithm
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                cur = pygame.mouse.get_pos()
                if prev:
                    if shape == 'line':
                        pygame.draw.line(screen, color, prev, cur, width)
                    if shape == 'eraser':
                        pygame.draw.line(screen, WHITE, prev, cur, width)  # key word is white
                    prev = cur
            if event.type == pygame.MOUSEBUTTONUP:
                prev = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev = pygame.mouse.get_pos()  # if I press button I get previous point
            if event.type == pygame.MOUSEBUTTONUP:
                cur = pygame.mouse.get_pos()   # if I stop pressing the button I get current point
                if shape == 'circle':
                    x = (prev[0]+cur[0])/2  # coordinates of center
                    y = (prev[1]+cur[1])/2
                    rx = abs(prev[0]-cur[0])/2  # radius by Ox and Oy
                    ry = abs(prev[1]-cur[1])/2
                    r = (rx + ry)/2  # radius
                    pygame.draw.circle(screen, color, (x, y), r, width)
                elif shape == 'rectangle' or shape == 'square':
                    x = min(prev[0], cur[0])  #minimal coordinate
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  # length
                    ly = abs(prev[1]-cur[1])
                    if shape == 'square':
                        lx = (lx+ly)/2  # length and width are same for square
                        ly = lx
                    pygame.draw.rect(screen, color, (x, y, lx, ly), width)
                elif shape == 'right_triangle' or shape == 'equilateral_triangle':
                    x = min(prev[0], cur[0])  #minimal coordinate
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  # length of pseudo rectangle
                    ly = abs(prev[1]-cur[1])
                    if shape == 'right_triangle':
                        ly = math.sqrt(lx**2 - (lx/2)**2)  # all sides are equal
                    points = (x, y+ly), (x+lx/2, y), (x+lx, y+ly)  # draw by three points
                    pygame.draw.polygon(screen, color, points, width)
                elif shape == 'rhombus':
                    x = min(prev[0], cur[0])  # minimal coordinates
                    y = min(prev[1], cur[1])
                    lx = abs(prev[0]-cur[0])  #sizes
                    ly = abs(prev[1]-cur[1])
                    points = (x+lx/2, y), (x+lx, y+ly/2), (x+lx/2, y+ly), (x, y+ly/2)
                    pygame.draw.polygon(screen, color, points, width)  # draw by points
    pygame.display.flip()  #updating te screen
    clock.tick(fps)

pygame.quit()