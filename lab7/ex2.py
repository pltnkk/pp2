import pygame
import time
pygame.init()

mickey = pygame.image.load("/Users/kpiltann/Downloads/mickeyclock.jpeg")

minute = pygame.Surface((50,200))
second = pygame.Surface((25,100))

minute1 = 0
second1 = 0

screen = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("Mickey Mouse Clock")


while True:
    now = time.localtime()
    min = now.tm_min
    sec = now.tm_sec


    minute1 = (min/60) * 360
    second1 = (sec/60) * 360
    minuteee = pygame.transform.rotate(minute, min)
    seconddd = pygame.transform.rotate(second, sec)


    mickey.blit(minuteee, (275, 200))
    mickey.blit(seconddd, (300,150))
    screen.blit(mickey, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()