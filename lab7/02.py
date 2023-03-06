import pygame

pygame.init()

playlist = ['song1.mp3', 'song2.mp3', 'song3.mp3'] # define your playlist here
current_song = 0 # index of currently playing song

pygame.mixer.music.load(playlist[current_song])

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

# assign keyboard shortcuts to functions
pygame.key.set_repeat(250, 50)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_song()
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                prev_song()
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit()