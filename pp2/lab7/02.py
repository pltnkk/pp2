import pygame
import pygame.freetype
import time

pygame.init()

x,y = 350, 600

songs = ['Erikpe.mp3', 'Sheker.mp3', 'Sapar.mp3', 'Uide.mp3']

music = 0


screen = pygame.display.set_mode((x,y))

pygame.display.set_caption("My Playlist")

photo = pygame.image.load("/Users/kpiltann/Desktop/pp2/lab7/djuzz.jpg")
show = pygame.transform.scale(photo, (250,250))

stop_button = pygame.image.load("stop.png")
stop = pygame.transform.scale(stop_button, (75,75))

next_button = pygame.image.load("next.png")
next  = pygame.transform.scale(next_button, (60,60))

previous_button = pygame.image.load("previous.png")
previous  = pygame.transform.scale(previous_button, (60,60))


font = pygame.font.Font(None, 36)

pygame.mixer.music.load("Erikpe.mp3")
pygame.mixer.music.play(-1)

start_time = time.time()


run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                run = not run
                if run : pygame.mixer.music.pause()
                else : pygame.mixer.music.unpause()    
                
            elif event.key == pygame.K_DOWN:         
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                if music == len(songs)-1:
                    music = 0
                    pygame.mixer.music.load(songs[music])
                    pygame.mixer.music.play(-1)
                else:
                    music +=1
                    pygame.mixer.music.load(songs[music])
                    pygame.mixer.music.play(-1)

            elif event.key == pygame.K_LEFT:
                if music == 0:
                    music = len(songs)
                    pygame.mixer.music.load(songs[music - 1])
                    pygame.mixer.music.play(-1)
                else:
                    music -= 1
                    pygame.mixer.music.load(songs[music])
                    pygame.mixer.music.play(-1)

    current_time = time.time() - start_time

    
    time_text = font.render('Time: {:.2f}'.format(current_time), True, "Black")
    screen.blit(time_text, (120, 360))

                
    screen.fill("White")                    
    screen.blit(show, (50,70))
    screen.blit(stop, (138,388) )
    screen.blit(next, (205,395))
    screen.blit(previous, (85, 395) )
    pygame.display.update()


    

    
