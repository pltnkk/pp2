import random
import time
import pygame

clock = pygame.time.Clock()
fps = 60  # frame per seconds

COINS_DICTIONARY = {'1': 'coin_1.png', '2': 'coin_2.png'}

RED = (255, 0, 0)  # colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPEED = 6  # speed of enemy car
SCORE = 0  # player's score

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 393, 600  # size of the window
pygame.init()  # initialization
screen = pygame.display.set_mode(WINDOW_SIZE)  # initializing main screen

font = pygame.font.SysFont('Verdana', 63)  # big font
font_small = pygame.font.SysFont('Verdana', 18)  # small font
game_over_text_label = font.render('Game over!', True, WHITE)  # game over label
background = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab9/racer/road.png')  # background image
pygame.mixer.init()  # initializing music component
pygame.mixer.music.set_volume(0.45)  # volume of music
pygame.mixer.music.load('/Users/kpiltann/Desktop/pp2/lab9/racer/background.wav')  # music that will be played while playing the game
pygame.mixer.music.play(loops=10 ** 9)  # approximately infinite music

pygame.display.set_caption('GAME')  # the title of window

game_over = False  # game not over condition


class Coin(pygame.sprite.Sprite):
    # coin is moving, so it should be extended from Sprite.
    # Also, I need to extend Coin from Sprite for increasing points if Player collided with Coin
    def __init__(self, _image_name: str, _points=1):
        # we have several coins with different masses,
        # so we pass the name of image and the weight of coin (points which player get for taking such coin)
        super().__init__()
        self.image = pygame.image.load(_image_name)  # image of coin
        self.rect = self.image.get_rect()  # rectangle of image
        self.radius = self.rect.width//2  # we need this for setting the limit of generating random coordinates of center of coin
        self.set_random_position()  # coin will appear at some position
        self.points = _points

    def move(self):
        self.rect.move_ip(0, 3)  # it is moving by y-axis with step 3
        if self.rect.top > WINDOW_HEIGHT:  # if coin reached the bottom, it will from the top
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying coin

    def set_random_position(self):
        self.rect.center = (random.randint(40+self.radius, WINDOW_WIDTH-40-self.radius), 0)
        # its coordinate by x-axis is limited by yellow line,
        # 40 - distance from edge to line
        self.rect.bottom = 0  # coin starts moving from the top


class Enemy(pygame.sprite.Sprite):
    # firstly, enemy car is moving.
    # Secondly, enemy car can collide with player.
    # These are reasons of extending enemy car from the sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab9/racer/eneemy.png')  # image of enemy car
        self.rect = self.image.get_rect()  # rectangle of image
        self.set_random_position()

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)  # car is moving by y-axis with some speed

        if self.rect.top > WINDOW_HEIGHT:  # if enemy car reached the bottom of window
            SCORE += 1  # player get point for not collision with enemy car
            self.set_random_position()

    def set_random_position(self):
        self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)
        # 40 distance between edge and yellow line, which should not be touched,
        # 24 is the distance to the center of car by x-axis.
        # 40+24=64
        self.rect.bottom = 0  # it starts motion from the top of window

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the enemy car


class Player(pygame.sprite.Sprite):  # Player is moving by x-axis. It can collide with coin or enemy car
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/kpiltann/Desktop/pp2/lab9/racer/car.png')  # image of player
        self.rect = self.image.get_rect()  # rectangle of image
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)  # initial coordinates of center

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # player moves by x-axis when some keys are pressed

        if self.rect.left > 43:  # possible coordinate by x-axis is limited by yellow line
            if pressed_keys[pygame.K_LEFT]:  # if left arrow touched, car will move to the left direction
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH - 43:
            if pressed_keys[pygame.K_RIGHT]:  # if right arrow touched, car will move to the right direction
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the player


player = Player()  # initializing the object of player class
enemy = Enemy()  # init the object of enemy class
coin_1 = Coin(COINS_DICTIONARY['1'])  # init the object of coin class
coin_2 = None

all_sprites = pygame.sprite.Group()
# creating array of objects
# we add all sprites to the one array for simplify and integrate their actions
# for example, all sprites move and should be drawn
# also, we need to stop game, if collision with enemy car occur
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin_1)

enemies = pygame.sprite.Group()  # pygame sprite collide method requires array of elements with which player can collide
enemies.add(enemy)

coins = pygame.sprite.Group()  # also, we need special array of coin sprites
coins.add(coin_1)

super_coin_group = pygame.sprite.Group()
# super_coins.add(coin_2)

simple_coins = 0  # variable which keeps number of touched coins
super_coins = 0
is_super_coin_generated = False
is_speed_increased = False


def generate_coin(type=1):
    global coin_1, coin_2
    if type == 1:
        coin_1 = Coin(COINS_DICTIONARY['1'])
        coins.add(coin_1)
        all_sprites.add(coin_1)
    else:
        coin_2 = Coin(COINS_DICTIONARY['2'])
        super_coin_group.add(coin_2)
        all_sprites.add(coin_2)


while not game_over:  # while game is playing
    for event in pygame.event.get():  # events
        if event.type == pygame.QUIT:  # quit
            game_over = True

    screen.blit(background, (0, 0))  # blitting background image to the window

    screen.blit(
        font_small.render(f'Score: {SCORE}', True, BLUE), (237, 9)
    )  # displaying total score

    screen.blit(
        font_small.render(f'Simple coins: {simple_coins}', True, BLUE), (237, 30)
    )  # displaying number of touched coins

    screen.blit(
        font_small.render(f'Super coins: {super_coins}', True, BLUE), (237, 51)
    )  # displaying number of touched coins

    for sprite in all_sprites:
        sprite.move()  # moving and displaying all sprites
        sprite.draw(screen)

    if SCORE % 12 == 0 and SCORE != 0:
        if not is_super_coin_generated:
            is_super_coin_generated = True
            generate_coin(type=2)
    elif SCORE % 12 == 1:
        is_super_coin_generated = False

    total_coins = simple_coins + super_coins

    if total_coins % 7 == 0 and total_coins != 0:
        if not is_speed_increased:
            is_speed_increased = True
            SPEED += 2
    elif total_coins % 7 == 1:
        is_speed_increased = False

    if coin_2:
        if pygame.sprite.spritecollideany(player, super_coin_group):
            coin_2.kill()
            super_coins += 1
            SCORE += 2

    if pygame.sprite.spritecollideany(player, coins):
        coin_1.kill()  # simple coin disappear
        SCORE += 1  # for touching a simple coin player get one points
        simple_coins += 1  # variable of number of touched simple coins
        generate_coin()  #new simple coin will appear

    if pygame.sprite.spritecollideany(player, enemies):  # collision with enemy car
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()  # crash music appears
        time.sleep(1)  # wait of 1 second

        screen.fill((69, 172, 116))  # unique green color on a backgroung
        screen.blit(game_over_text_label, (12, 190))  # displaying message that game over
        screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))  # display score
        screen.blit(font_small.render(f'Simple coins: {simple_coins}', True, WHITE),
                    (15, 290))  # display number of touched coins
        screen.blit(font_small.render(f'Super coins: {super_coins}', True, WHITE),
                    (15, 311))  # display number of touched coins

        pygame.display.update()  # updating the screen for showing game over page

        for sprite in all_sprites:
            sprite.kill()  # stopping the game

        time.sleep(7)  # wait for 7 seconds

        game_over = True  # condition of game

    pygame.display.update()  # changing the position of objects
    clock.tick(fps)  # speed of changing the screen

pygame.quit()