# импортируем модули random, time и pygame
import pygame
import random
import time

pygame.init() # инициализирует все модули pygame

# такие постоянные, как размер экрана (длина и ширина), несколько цветов
size = width, height = (800, 800)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
font = pygame.font.SysFont("Verdana", 20) # шрифт - Verdana, размер - 20
font1 = pygame.font.SysFont("Verdana", 70) # шрифт - Verdana, размер - 120
font2 = pygame.font.SysFont("Verdana", 30) # шрифт - Verdana, размер - 30
level_text = font.render("LEVEL:", True, BLACK) # Создаем текст черного цвета - "LEVEL"
score_text = font.render("SCORE:", True, BLACK) # Создаем текст черного цвета - "SCORE"
game_over_text = font1.render("GAME OVER", True, BLACK) # Создаем текст для окончания игры

screen = pygame.display.set_mode(size) # создаем экран вышеупомянутыми размерами
screen.fill(WHITE) # экран заполняем белым
pygame.display.set_caption('Snake') # добавляем название игры в верхней части экрана заголовка
FPS = 30 # 30 кадров в секунду
clock = pygame.time.Clock() # для отслеживания времени

class Food: # создаем класс Food
    def __init__(self): # функция для инициализации
        self.x = random.randint(21, 771) # центр выбирается рандомно
        self.y = random.randint(86, 776)
        self.width = random.randint(10, 12) # ширина генерируется рандомно
    
    def gen(self): # функция, которая генерирует новую еду (рандомно выбирая координату по Ох и Оу и ширину)
        self.x = random.randint(21, 771)
        self.y = random.randint(86, 776)
        self.width = random.randint(10, 12)

    def draw(self): # функция, которая отрисовывает еду (прямоугольник на экране, зеленого цвета, координаты цента инициализированы выше, а длина = 15, а ширина инициализирована выше)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 15, self.width))

F1 = Food() # вызываем класс Food

class Snake: # создаем класс Snake
    def __init__(self, x, y): # функция для инициализации
        self.elements = [[x, y]] # координаты центров окружностей
        self.size = 1 # размер змейки (количество окружностей)
        self.radius = 10 # радиус окружности
        self.dx = 5 # перемещение по Ох
        self.dy = 0 # перемещение по Оу
        self.speed = 10 # скорость змейки
        self.is_add = False # переменная по добавлению новых элементов (окружностей)
        self.direction = 'RIGHT' # направление движения змейки
        self.change_direction = self.direction # направление движения становится равным изменению направления 
        self.level = 1 # уровень
        self.score = 0 # счетчик съеденной еды

    def draw(self): # функция, которая отрисовывает элементы (окружности на экране желтого цвета, центр и радиус инициализированы выше)
        for element in self.elements:
            pygame.draw.circle(screen, YELLOW, element, self.radius)

    def add_to_snake(self): # функция, которая добавляет (увеличивает размер, счетчик еды, добавляет элементы (центры новых окружностей))
        self.size += 1
        self.elements.append([0, 0])
        self.ball = F1.width - 9 # переменная, которая показывает балл в зависимости от ширины еды
        self.score += self.ball
        self.is_add = False # переменная по добавлению новых элементов (окружностей) принимает значение False
        if self.score % 4 == 0 and self.score > 0: # если размер змейки кратен 4, то уровень повышается, а скорость увеличивается на 10
            self.level += 1
            self.speed += 10
        if self.ball == 2:
            if self.score % 4 != 0:
                if (self.score - 1) % 4 == 0:
                    self.level += 1
                    self.speed += 10
        if self.ball == 3:
            if self.score % 4 != 0:
                if (self.score - 1) % 4 == 0 or (self.score - 2) % 4 == 0:
                    self.level += 1
                    self.speed += 10

    def check_direction(self): # функция, которая меняет направление: если, например, направление - "вправо", а изменение направление - любое, но не "влево", тогда направление движения становится равным изменению движения
        if (self.direction == 'RIGHT' and self.change_direction != 'LEFT') or (self.direction == 'LEFT' and self.change_direction != 'RIGHT') or (self.direction == 'UP' and self.change_direction != 'DOWN') or (self.direction == 'DOWN' and self.change_direction != 'UP'):
            self.direction = self.change_direction

    def game_over(self): # функция для окончания игры: экран заполняется красным, и выходят тексты о том, что игра закончена и о конечных баллах и уровнях. а также, игра закрывается спустя 6 секунд
        screen.fill(RED)
        screen.blit(game_over_text, (180, 300))
        screen.blit(level_text, (250, 400))
        screen.blit(score_text, (450, 400))
        t1 = font2.render(str(self.score), True, BLACK)
        screen.blit(t1, (470, 430))
        t2 = font2.render(str(self.level), True, BLACK)
        screen.blit(t2, (280, 430))
        pygame.display.flip()
        time.sleep(6)
        pygame.quit()

    def move(self): # функция по передвижению
        if self.is_add: # если переменная по добавлению новых элементов (окружностей) принимает значение True, то выполняется функция add_to_snake
            self.add_to_snake()
        for i in range(self.size - 1, 0, -1): # пробегаемся от последнего элемента змейки до первого, чтобы каждый предыдущий элемент (окружность) принимал место следующего за ним
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        if self.direction == 'RIGHT': # если направление - "вправо" и змейка не выходит за границы экрана, то она двигается вправо (координаты элементов по Ох увеличиваются на 5), а в противном случае возвращается влево, на начальную координату по Ох
            if self.elements[0][0] <= 763 and self.elements[0][0] >= 31:
                self.elements[0][0] += self.dx
            else:
                self.elements[0][0] = 31
        elif self.direction == 'LEFT': # если направление - "влево" и змейка не выходит за границы экрана, то она двигается влево (координаты элементов по Ох уменьшаются на 5), а в противном случае возвращается вправо, на конечную координату по Ох
            if self.elements[0][0] <= 763 and self.elements[0][0] >= 35:
                self.elements[0][0] -= self.dx
            else:
                self.elements[0][0] = 763
        elif self.direction == 'UP': # если направление - "вверх" и змейка не выходит за границы экрана, то она двигается вниз (координаты элементов по Оу уменьшаются на 5), а в противном случае игра окончивается, вызываем вышеупомянутую функцию
            if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                self.elements[0][1] -= self.dy
            else:
                self.game_over()
                # self.elements[0][1] = 770
        elif self.direction == 'DOWN': # если направление - "вниз" и змейка не выходит за границы экрана, то она двигается вниз (координаты элементов по Оу увеличиваются на 5), а в противном случае возвращается вверх, на начальную координату по Оу
            if self.elements[0][1] <= 770 and self.elements[0][1] >= 96:
                self.elements[0][1] += self.dy
            else:
                self.elements[0][1] = 96

    def eat(self, foodx, foody): # функция для подсчета съеденной еды, которой передаем 2 параметра, которые являются координатами центра еды (окружности)
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx - 2 <= x <= foodx + 15 and foody - 2 <= y <= foody + 15: # если центр элемента (окружности) лежит в данном интервале, то функция возвращает значение True
            return True
        return False

S1 = Snake(30, 96) # вызываем класс Snake
d = 5 # переменная для передвижения

time_delay = 15000
timer_event = pygame.USEREVENT + 1 # создаем новое событие timer_event, которое происходит каждые 15 секунд
pygame.time.set_timer(timer_event, time_delay)

# Игровой цикл, в котором программа продолжает цикл снова и снова, пока не произойдет событие типа QUIT
done = False
while not done:
    clock.tick(S1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == timer_event: # если происходит событие timer_event, то заново генерируем еду (вызываем функцию gen из класса Food)
            F1.gen()
        if event.type == pygame.KEYDOWN: # если нажали какую-то клавишу клавиатуры
            if event.key == pygame.K_ESCAPE: # если нажали ESC, то выходим из игры
                done = True
            if event.key == pygame.K_RIGHT and S1.dx != d: # если нажата кнопка "right" и перемещение направлено не влево, то направление = "right", а двигаться будет по Ох на 5 вправо
                S1.direction = 'RIGHT'
                S1.dx = d
                S1.dy = 0
            if event.key == pygame.K_LEFT and S1.dx != d: # если нажата кнопка "left" и перемещение направлено не вправо, то направление = "left", а двигаться будет по Ох на 5 влево
                S1.direction = 'LEFT'
                S1.dx = d
                S1.dy = 0
            if event.key == pygame.K_UP and S1.dy != d: # если нажата кнопка "up" и перемещение направлено не вниз, то направление = "up", а двигаться будет по Он на 5 вверх
                S1.direction = 'UP'
                S1.dx = 0
                S1.dy = d
            if event.key == pygame.K_DOWN and S1.dy != d: # если нажата кнопка "down" и перемещение направлено не вверх, то направление = "down", а двигаться будет по Оу на 5 вниз
                S1.direction = 'DOWN'
                S1.dx = 0
                S1.dy = d

    levels = font.render(str(S1.level), True, BLACK) # текст, содержащий номер уровня
    scores = font.render(str(S1.score), True, BLACK) # текст, содержащий количество съеденной еды
    if S1.eat(F1.x, F1.y): # если еда была съедена (функция eat из класса Snake вернула значение True), то переменная is_add из класса Snake возвращает значение True, и тогда вызывается функция gen из класса Food (генерируем новую еду)
        S1.is_add = True
        F1.gen()
    S1.move() # вызываем функцию move для передвижения из класса Snake
    screen.fill(WHITE) # заполняем экран белым цветом
    screen.blit(level_text, (710, 20)) # выводим текст "LEVEL" на указанную позицию
    screen.blit(levels, (735, 50)) # выводим значение level на указанную позицию
    screen.blit(score_text, (20, 20)) #  выводим текст "SCORE" на указанную позицию
    screen.blit(scores, (45, 50)) # выводим значение score на указанную позицию
    pygame.draw.line(screen, BLACK, (20, 10), (780, 10), 1) # линия для отделения верхней части экрана от текста (толщина = 1)
    pygame.draw.line(screen, BLACK, (20, 85), (780, 85), 2) # линия для отделения верхней части экрана от текста (толщина = 2)
    pygame.draw.rect(screen, BLACK, (20, 85, 760, 700), 1) # прямоугольник для выделения игрового поля
    S1.draw() # вызываем функцию draw для отрисовки змейки
    F1.draw() # вызываем функцию draw для отрисовки еды

    pygame.display.flip() # обновляем содержимое дисплея игры

pygame.quit() # отключает модуль pygame