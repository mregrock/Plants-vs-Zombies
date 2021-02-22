import pygame
import datetime
import random
import time


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
    global prev_time
    screen.blit(play_background, (0, 0))
    draw_text()
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
    plants_action()


def button_check_start(coord):
    global fl, prev_time
    global running
    x, y = coord[0], coord[1]
    if 940 >= x >= 590 and 480 >= y >= 320:
        fl = "play"
        prev_time = time.time()
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


def check_score(price):
    global score
    if score >= price:
        return True
    return False


def button_check_play(coord):
    global fl_cursor, prev_time
    global score
    global cost
    global cursor
    global mas_flowers, pee_shoot_times, sunflower_times
    global flag_sun_1, flag_sun_2, flag_sun_3
    x, y = coord[0], coord[1]
    if y > 155:
        for i in range(5):
            for j in range(9):
                if square_centres[i][j][0] + 15 >= x >= square_centres[i][j][0] \
                        and square_centres[i][j][1] + 15 >= y >= square_centres[i][j][1] and flag_sunflowers[i][j] == 1:
                    flag_sunflowers[i][j] = 0
                    score += 50

    elif 155 >= y >= 0:
        if 155 >= x >= 1 and check_score(50):
            cursor = tomato
        elif 256 >= x >= 156 and check_score(50):
            cursor = sunflower
        elif 406 >= x >= 306 and check_score(100):
            cursor = pee
        elif 556 >= x >= 456 and check_score(50):
            cursor = nut
        elif 706 >= x >= 606 and check_score(200):
            cursor = double_pee
        elif 856 >= x >= 756 and check_score(150):
            cursor = cherry
        elif 1006 >= x >= 906 and check_score(50):
            cursor = thorns
        elif 1156 >= x >= 1056:
            cursor = shovel
        elif 1400 <= x <= 1415 and 50 <= y <= 65 and flag_sun_1:
            score += 100
            flag_sun_1 = 0
            prev_time = time.time()
        elif 1460 <= x <= 1475 and 80 <= y <= 95 and flag_sun_2:
            score += 100
            flag_sun_2 = 0
            prev_time = time.time()
        elif 1450 <= x <= 1465 and 30 <= y <= 45 and flag_sun_3:
            score += 100
            flag_sun_3 = 0
            prev_time = time.time()
        if 1156 >= x >= 1:
            fl_cursor = "not const"
    if fl_cursor == "not const" and cursor_const != cursor:
        if 930 >= y >= 155 and 1550 >= x >= 1:
            x = x // 155
            y = (y - 155) // 155
            if mas_flowers[x][y] == nots and cursor != shovel:
                score -= cost[cursor]
                mas_flowers[x][y] = cursor
                hp_flowers[x][y] = 50
                if cursor == nut:
                    hp_flowers[x][y] = 500
                if cursor == sunflower:
                    sunflower_times[x][y] = time.time()
                if cursor == pee:
                    pee_shoot_times[x][y] = time.time()
                    pee_shoot_flags[x][y] = 1
            elif cursor == shovel:
                mas_flowers[x][y] = nots
                hp_flowers[x][y] = 0
            cursor = cursor_const
            fl_cursor = "const"


def checks():
    for i in range(9):
        for j in range(5):
            if mas_flowers[i][j] == POW:
                mas_flowers[i][j] = nots


def draw_plants():
    global mas_flowers
    for i in range(9):
        for j in range(5):
            screen.blit(mas_flowers[i][j], (i * 155 + 10, j * 155 + 175))


def sun_down_1():
    screen.blit(sun, (1400, 50))


def sun_down_2():
    screen.blit(sun, (1460, 80))


def sun_down_3():
    screen.blit(sun, (1450, 30))


def plants_action():
    global sunflower_times
    global flag_sunflowers
    flag_sunflower = 0
    square_centre = (0, 0)
    for x in range(5):
        for y in range(9):
            if mas_flowers[x][y] == sunflower:
                if time.time() - sunflower_times[x][y] > 20:
                    sunflower_times[x][y] = time.time()
                    square_centre = (x * 155, y * 155 + 155)
                    flag_sunflowers[x][y] = 1
                    screen.blit(sun, square_centre)


def draw_text():
    global score
    text_surface = font.render(str(score), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (1300, 935)
    screen.blit(text_surface, text_rect)


def draw_zombies():
    global zombie_anim_fl
    global zombies_anim
    global zombies_x
    global zombies_y
    global zombie_eat_fl
    global mas_flowers
    global zombie_hp
    if fl == "play":
        if len(zombies_x) == 0:
            zombies_x.append(1500)
            zombies_y.append(zombies_y_const[random.randrange(5)])
            zombie_eat_fl.append(0)
            zombie_anim_fl.append(0)
            zombies_anim.append(0)
            zombie_hp.append(100)
        for i in range(len(zombies_x)):
            if zombie_hp[i] <= 0:
                del zombies_x[i]
                del zombie_eat_fl[i]
                del zombies_y[i]
                del zombie_anim_fl[i]
                del zombie_hp[i]
                del zombies_anim[i]
                break
            if zombie_eat_fl[i] == 0:
                zombies_x[i] -= 0.5
                screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))
                x1 = zombies_x[i] // 150
                y1 = (zombies_y[i]) // 150
                for y in range(5):
                    for x in range(9):
                        if mas_flowers[x][y] != nots and mas_flowers[x][y] != thorns:
                            if x1 == x and y1 == y:
                                zombie_eat_fl[i] = 1
                        if mas_flowers[x][y] == thorns:
                            if x1 == x and y1 == y:
                                zombie_hp[i] -= 0.13
                        if mas_flowers[x][y] == tomato:
                            if x1 == x and y1 == y:
                                zombie_hp[i] -= 1000
                                mas_flowers[x][y] = POW
                if zombie_anim_fl[i] < 9:
                    zombie_anim_fl[i] += 1
                elif zombie_anim_fl[i] == 9:
                    zombie_anim_fl[i] = 0
                    zombies_anim[i] += 1
                    zombies_anim[i] %= 3
            else:
                dop_trash = zombies_anim[i]
                if dop_trash == 1 or dop_trash == 2:
                    zombies_anim[i] = 0
                    zombie_anim_fl[i] = 0
                if zombie_anim_fl[i] < 20:
                    zombie_anim_fl[i] += 1
                elif zombie_anim_fl[i] == 20:
                    zombie_anim_fl[i] = 0
                    zombies_anim[i] = 3 - zombies_anim[i]
                    x1 = zombies_x[i] // 150
                    y1 = (zombies_y[i]) // 150
                    for y in range(5):
                        for x in range(9):
                            if x1 == x and y1 == y:
                                hp_flowers[x][y] -= 10
                                if hp_flowers[x][y] == 300:
                                    mas_flowers[x][y] = nut_1
                                if hp_flowers[x][y] == 100:
                                    mas_flowers[x][y] = nut_2
                                if hp_flowers[x][y] == 0:
                                    mas_flowers[x][y] = nots
                                    zombie_eat_fl[i] = 0
                screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))


def draw_sun():
    global prev_time
    global flag_sun_1
    global flag_sun_2
    global flag_sun_3
    if fl == "play" and time.time() - prev_time > 20:
        prev_time = time.time()
        if flag_sun_1 == 0:
            flag_sun_1 = 1
        elif flag_sun_2 == 0:
            flag_sun_2 = 1
        else:
            flag_sun_3 = 1
    if flag_sun_1:
        sun_down_1()
    if flag_sun_2:
        sun_down_2()
    if flag_sun_3:
        sun_down_3()
    for x in range(5):
        for y in range(9):
            if flag_sunflowers[x][y] == 1:
                screen.blit(sun, square_centres[x][y])
                sunflower_times[x][y] = time.time()


def draw_pee_shots():
    global pee_shot_coord, pee_shoot_flags, pee_shoot_times
    for x in range(5):
        for y in range(9):
            if pee_shot_coord[x][y][0] < 1500 and pee_shot_coord[x][y][1] < 1000:
                if mas_flowers[x][y] == pee and pee_shoot_flags[x][y] == 1:
                    screen.blit(pee_shot, (pee_shot_coord[x][y][0] + 15, pee_shot_coord[x][y][1]))
                    pee_shot_coord[x][y] = (pee_shot_coord[x][y][0] + 15, pee_shot_coord[x][y][1])
            else:
                pee_shot_coord[x][y] = (x * 155 + 15, y * 155 + 175)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Plants vs zombos")
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    clock_time = pygame.time.Clock()
    cursor_const = cursor = pygame.image.load("cursor.png")
    fl_cursor = "const"
    nots = pygame.image.load("not.png")
    mas_flowers = [[nots] * 10 for i in range(10)]
    hp_flowers = [[0] * 10 for i in range(10)]
    for i in range(9):
        for j in range(5):
            mas_flowers[i][j] = nots
            hp_flowers[i][j] = 0
    zombies_x = []
    zombies_y = []
    zombies_y_const = [100, 250, 400, 550, 700]
    zombies_anim = []
    zombie_anim_1 = pygame.image.load("zombie_const.png")
    zombie_anim_2 = pygame.image.load("zombie_rightleg.png")
    zombie_anim_3 = pygame.image.load("zombie_leftleg.png")
    zombie_anim_4 = pygame.image.load("zombie_eat.png")
    anim_number = [zombie_anim_1, zombie_anim_2, zombie_anim_3, zombie_anim_4]
    zombie_eat_fl = []
    zombie_anim_fl = []
    zombie_helmet = []
    zombie_hp = []
    score = 100
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 50)
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
    nut_1 = pygame.image.load("nut_2.png")
    nut_2 = pygame.image.load("nut_3.png")
    pee = pygame.image.load("pee.png")
    double_pee = pygame.image.load("double_pee.png")
    pee_shot = pygame.image.load("pee_shot.png")
    cherry = pygame.image.load("cherry.png")
    thorns = pygame.image.load("thorns.png")
    shovel = pygame.image.load("shovel.png")
    sun = pygame.image.load("sun.png")
    POW = pygame.image.load("POW.png")
    pos_mouse_x = -100
    pos_mouse_y = -100
    fl = "start"
    score = 1000
    # pygame.mixer.music.load('music_start.mp3')
    # pygame.mixer.music.play()
    running = True
    open_windows()
    clock_time.tick(60)
    pygame.display.flip()
    time_fl = 0
    cost = {pee: 100, nut: 50, cherry: 150, tomato: 50, thorns: 50, double_pee: 200, sunflower: 50}
    sunflower_times = [[100000000000 for _ in range(9)] for _ in range(5)]
    pee_shoot_times = [[100000000000 for _ in range(9)] for _ in range(5)]
    pee_shoot_flags = [[0 for _ in range(9)] for _ in range(5)]
    pee_shot_coord = [[(x * 155 + 15, y * 155 + 170) for y in range(9)] for x in range(5)]
    flag_sunflowers = [[0 for _ in range(9)] for _ in range(5)]
    square_centres = [[(x * 155, y * 155 + 155) for y in range(9)] for x in range(5)]
    now = datetime.datetime.now()
    then = datetime.datetime.now()
    pygame.mixer.music.set_volume(0.5)
    volume = pygame.mixer.music.get_volume()
    prev_time = 0
    flag_sun_1 = 0
    flag_sun_2 = 0
    flag_sun_3 = 0
    mouse_x = -100
    mouse_y = -100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fl == "start":
                    button_check_start(pygame.mouse.get_pos())
                if fl == "help":
                    button_check_help(pygame.mouse.get_pos())
                if fl == "play":
                    button_check_play(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if volume > 0:
                        volume -= 0.1
                    pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_RIGHT:
                    if volume < 1:
                        volume += 0.1
                    pygame.mixer.music.set_volume(volume)
            mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            pygame.display.flip()
            clock.tick(60)
            pygame.display.set_caption("fps: " + str(clock.get_fps()))
        open_windows()
        draw_plants()
        draw_zombies()
        draw_sun()
        draw_pee_shots()
        draw_cursor((mouse_x, mouse_y))
        pygame.display.flip()
pygame.quit()
