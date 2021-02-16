import pygame
import datetime
import random


def open_windows():
    global fl
    if fl == "start":
        first_window()
    if fl == "help":
        help_window()
    if fl == "play":
        play_window()


def draw_cursor(coord):
    screen.blit(cursor, coord)


def first_window():
    screen.blit(background, (0, 0))
    screen.blit(Bplay, (590, 320))
    screen.blit(Hplay, (550, 640))
    screen.blit(Eplay, (580, 770))


def help_window():
    screen.blit(help_background, (0, 0))
    screen.blit(H_back, (1100, 250))


def play_window():
    screen.blit(play_background, (0, 0))
    for i in range(8):
        screen.blit(page, (i * 152, 0))
    screen.blit(tomato, (20, 20))
    screen.blit(sunflower, (175, 20))
    screen.blit(pee, (335, 20))
    screen.blit(nut, (485, 20))
    screen.blit(double_pee, (625, 20))
    screen.blit(cherry, (780, 20))
    screen.blit(thorns, (930, 20))
    screen.blit(shovel, (1080, 20))


def button_check_start(coord):
    global fl
    global running
    x, y = coord[0], coord[1]
    if 940 >= x >= 590 and 480 >= y >= 320:
        fl = "play"
        open_windows()
        screen.blit(cursor, coord)
        pygame.display.flip()
        # pygame.mixer.music.load('play_music.mp3')
        # pygame.mixer.music.play()
    if 1000 >= x >= 550 and 720 >= y >= 640:
        fl = "help"
        open_windows()
        screen.blit(cursor, coord)
        pygame.display.flip()
    if 950 >= x >= 580 and 850 >= y >= 770:
        running = False


def button_check_help(coord):
    global fl
    x, y = coord[0], coord[1]
    if 1400 >= x >= 1100 and 700 >= y >= 250:
        fl = "start"
        open_windows()

        screen.blit(cursor, coord)
        pygame.display.flip()


def button_check_play(coord):
    global fl_cursor
    global cursor
    global mas_flowers
    x, y = coord[0], coord[1]
    if 155 >= y >= 0:
        if 155 >= x >= 1:
            cursor = tomato
        elif 256 >= x >= 156:
            cursor = sunflower
        elif 406 >= x >= 306:
            cursor = pee
        elif 556 >= x >= 456:
            cursor = nut
        elif 706 >= x >= 606:
            cursor = double_pee
        elif 856 >= x >= 756:
            cursor = cherry
        elif 1006 >= x >= 906:
            cursor = thorns
        elif 1156 >= x >= 1056:
            cursor = shovel
        if 1156 >= x >= 1:
            fl_cursor = "not const"
    if fl_cursor == "not const" and cursor_const != cursor:
        if 930 >= y >= 155 and 1550 >= x >= 1:
            x = x // 155
            y = (y - 155) // 155
            if mas_flowers[x][y] == nots and cursor != shovel:
                mas_flowers[x][y] = cursor
            elif cursor == shovel:
                mas_flowers[x][y] = nots
            cursor = cursor_const
            fl_cursor = "const"


def draw_plants():
    for i in range(9):
        for j in range(5):
            screen.blit(mas_flowers[i][j], (i * 155 + 20, j * 155 + 175))


def sun_down():
    screen.blit(sun, (1400, 50))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Plants vs zombos")
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    cursor_const = cursor = pygame.image.load("cursor.png")
    fl_cursor = "const"
    nots = pygame.image.load("not.png")
    mas_flowers = [[nots] * 10 for i in range(10)]
    for i in range(9):
        for j in range(5):
            mas_flowers[i][j] = nots
    print(mas_flowers)
    background = pygame.image.load("background.png").convert()
    help_background = pygame.image.load("help_background.png").convert()
    play_background = pygame.image.load("game_background.png").convert()
    Bplay = pygame.image.load("button_play.png").convert()
    Hplay = pygame.image.load("button_help.png").convert()
    Eplay = pygame.image.load("button_exit.png").convert()
    H_back = pygame.image.load("back_help.png").convert()
    page = pygame.image.load("page.png").convert()
    tomato = pygame.image.load("tomato.png")
    sunflower = pygame.image.load("sunflower.png")
    nut = pygame.image.load("nut.png")
    pee = pygame.image.load("pee.png")
    double_pee = pygame.image.load("double_pee.png")
    cherry = pygame.image.load("cherry.png")
    thorns = pygame.image.load("thorns.png")
    shovel = pygame.image.load("shovel.png")
    sun = pygame.image.load("sun.png")
    fl = "start"
    pygame.mixer.music.load('music_start.mp3')
    pygame.mixer.music.play()
    running = True
    open_windows()
    pygame.display.flip()
    time_fl = 0
    now = datetime.datetime.now()
    then = datetime.datetime.now()
    volume = pygame.mixer.music.get_volume()
    while running:
        for event in pygame.event.get():
            open_windows()
            draw_plants()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fl == "start":
                    button_check_start(pygame.mouse.get_pos())
                if fl == "help":
                    button_check_help(pygame.mouse.get_pos())
                if fl == "play":
                    button_check_play(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEMOTION:
                draw_cursor(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if volume > 0:
                        volume -= 0.1
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_RIGHT:
                    if volume < 1:
                        volume += 0.1
                    pygame.mixer.music.set_volume(volume)
            draw_cursor(pygame.mouse.get_pos())
            pygame.display.flip()
            clock.tick(60)
            pygame.display.set_caption("fps: " + str(clock.get_fps()))
            pygame.display.update()
pygame.quit()
