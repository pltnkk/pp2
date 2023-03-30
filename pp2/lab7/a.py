import pygame

import datetime

pygame.init()

w,h = (820,830)

time = datetime.datetime.now()

angles = -(int(time.strftime("%S"))) * 6 -6
anglem = -(int(time.strftime("%M"))) * 6 + (int(time.strftime("%S")) * 6 / 60) - 54

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center = rect.center )
    return new_image, rect

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Mickey Clock')

mickey = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab7/body.jpeg')
seconds = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab7/left.png')
minutes = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab7/right.png')

imagem = pygame.Surface((w,h), pygame.SRCALPHA)
imagem.blit(minutes, (0, 0))
newm = imagem
rectm = imagem.get_rect(center = (w//2, h//2))

images = pygame.Surface((w,h), pygame.SRCALPHA)
images.blit(seconds, (0, 0))
news = images
rects = images.get_rect(center = (w//2, h//2))

clock = pygame.time.Clock()

run = True

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.blit(mickey, (0, 0))
    screen.blit(imagem, rectm)
    screen.blit(images, rects)

    images, rects = rotate(seconds, rects, angles)
    imagem, rectm = rotate(minutes, rectm, anglem)

    angles -= 0.099
    anglem -= 0.099/60
    pygame.display.update()
    clock.tick(60)
   
