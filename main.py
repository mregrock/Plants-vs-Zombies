import pygame
import time

def open_windows():
    global fl
    if fl == "start":
        first_window()
    if fl == "help":
        help_window()


def draw_cursor(coord, cursor):
    pygame.mouse.set_visible(False)
    screen.blit(cursor, coord)


def first_window():
    screen.blit(background, (0, 0))
    Bplay = pygame.image.load("button_play.png")
    Hplay = pygame.image.load("button_help.png")
    Eplay = pygame.image.load("button_exit.png")
    screen.blit(Bplay, (590, 320))
    screen.blit(Hplay, (550, 640))
    screen.blit(Eplay, (580, 770))


def help_window():
    screen.blit(help_background, (0, 0))
    H_back = pygame.image.load(("back_help.png"))
    screen.blit(H_back, (1100, 250))


def button_check_start(coord):
    global fl
    global running
    x, y = coord[0], coord[1]
    if 940 >= x >= 590 and 480 >= y >= 320:
        pass
        #переход к основной игре
    if 1000 >= x >= 550 and 720 >= y >= 640:
        fl = "help"
    if 950 >= x >= 580 and 850 >= y >= 770:
        running = False
    open_windows()
    cursor = pygame.image.load("cursor.png")
    screen.blit(cursor, coord)
    pygame.display.flip()


def button_check_help(coord):
    global fl
    x, y = coord[0], coord[1]
    if 1400 >= x >= 1100 and 700 >= y >= 250:
        fl = "start"
    open_windows()
    cursor = pygame.image.load("cursor.png")
    screen.blit(cursor, coord)
    pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Plants vs monsters")
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    cursor = pygame.image.load("cursor.png")
    background = pygame.image.load("background.png")
    help_background = pygame.image.load("help_background.png")
    fl = "start"
    pygame.mixer.music.load('music_start.mp3')
    pygame.mixer.music.play()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fl == "start":
                    button_check_start(pygame.mouse.get_pos())
                if fl == "help":
                    button_check_help(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEMOTION:
                open_windows()
                if pygame.mouse.get_focused():
                    draw_cursor(pygame.mouse.get_pos(), cursor)
                else:
                    pass
                pygame.display.flip()
    pygame.quit()
