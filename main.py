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
    global cherry_bomb_fl, cherry_x, cherry_y
    global fl_cursor, prev_time
    global score
    global cost
    global cursor
    global mas_flowers, sunflower_times
    global flag_sun_1, flag_sun_2, flag_sun_3
    x, y = coord[0], coord[1]
    if y > 155:
        for i in range(5):
            for j in range(9):
                if square_centres[i][j][0] + 50 >= x >= square_centres[i][j][0] \
                        and square_centres[i][j][1] + 50 >= y >= square_centres[i][j][1] and flag_sunflowers[i][j] == 1:
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
        elif 1006 >= x >= 906 and check_score(125):
            cursor = thorns
        elif 1156 >= x >= 1056:
            cursor = shovel
        elif 1400 <= x <= 1450 and 50 <= y <= 100 and flag_sun_1:
            score += 25
            flag_sun_1 = 0
            prev_time = time.time()
        elif 1460 <= x <= 1510 and 80 <= y <= 130 and flag_sun_2:
            score += 25
            flag_sun_2 = 0
            prev_time = time.time()
        elif 1450 <= x <= 1500 and 30 <= y <= 80 and flag_sun_3:
            score += 25
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
                if cursor == double_pee:
                    dpee_fl.append(0)
                    dpee_x.append(x)
                    dpee_y.append(y)
                    dpee_coult.append(0)
                if cursor == tomato:
                    tomato_fl.append(0)
                    tomato_x.append(x)
                    tomato_y.append(y)
                if cursor == thorns:
                    thorns_fl.append(0)
                    thorns_x.append(x)
                    thorns_y.append(y)
                if cursor == pee:
                    pee_fl.append(0)
                    pee_x.append(x)
                    pee_y.append(y)
                    pee_coult.append(0)
                if cursor == nut:
                    hp_flowers[x][y] = 500
                if cursor == sunflower:
                    sunflower_times[x][y] = time.time()
                    sunfl_fl.append(0)
                    sunfl_x.append(x)
                    sunfl_y.append(y)
                if cursor == cherry:
                    cherry_bomb_fl = 1
                    cherry_x = x * 150
                    cherry_y = y * 150
            elif cursor == shovel:
                if mas_flowers[x][y] in thorns_anim:
                    for i in range(len(thorns_x)):
                        if thorns_x[i] == x and thorns_y[i] == y:
                            del thorns_x[i]
                            del thorns_y[i]
                            del thorns_fl[i]
                if mas_flowers[x][y] in sunfl_anim:
                    for i in range(len(sunfl_x)):
                        if sunfl_x[i] == x and sunfl_y[i] == y:
                            del sunfl_x[i]
                            del sunfl_y[i]
                            del sunfl_fl[i]
                if mas_flowers[x][y] in pee_anim:
                    for i in range(len(pee_x)):
                        if i >= len(pee_x):
                            break
                        if pee_x[i] == x and pee_y[i] == y:
                            del pee_x[i]
                            del pee_y[i]
                            del pee_fl[i]
                            del pee_coult[i]
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
    global thorns_fl
    global mas_flowers
    for k in range(len(thorns_fl)):
        if thorns_fl[k] < 5:
            thorns_fl[k] += 1
        elif thorns_fl[k] == 5:
            thorns_fl[k] = 0
            mas_flowers[thorns_x[k]][thorns_y[k]] = thorns_anim[
                1 - thorns_anim.index(mas_flowers[thorns_x[k]][thorns_y[k]])]
    for k in range(len(tomato_fl)):
        if tomato_fl[k] < 7:
            tomato_fl[k] += 1
        elif tomato_fl[k] == 7 and mas_flowers[tomato_x[k]][tomato_y[k]] in tomato_anim:
            tomato_fl[k] = 0
            mas_flowers[tomato_x[k]][tomato_y[k]] = tomato_anim[
                1 - tomato_anim.index(mas_flowers[tomato_x[k]][tomato_y[k]])]
    for k in range(len(sunfl_fl)):
        if sunfl_fl[k] < 15:
            sunfl_fl[k] += 1
        elif sunfl_fl[k] == 15 and mas_flowers[sunfl_x[k]][sunfl_y[k]] in sunfl_anim:
            sunfl_fl[k] = 0
            mas_flowers[sunfl_x[k]][sunfl_y[k]] = sunfl_anim[
                1 - sunfl_anim.index(mas_flowers[sunfl_x[k]][sunfl_y[k]])]
    for k in range(len(pee_fl)):
        if pee_fl[k] < 5:
            pee_fl[k] += 1
        elif pee_fl[k] == 5 and mas_flowers[pee_x[k]][pee_y[k]] in pee_anim:
            pee_fl[k] = 0
            mas_flowers[pee_x[k]][pee_y[k]] = pee_anim[
                1 - pee_anim.index(mas_flowers[pee_x[k]][pee_y[k]])]
    for k in range(len(dpee_fl)):
        if dpee_fl[k] < 9:
            dpee_fl[k] += 1
        elif dpee_fl[k] == 9 and mas_flowers[dpee_x[k]][dpee_y[k]] in dpee_anim:
            dpee_fl[k] = 0
            mas_flowers[dpee_x[k]][dpee_y[k]] = dpee_anim[
                1 - dpee_anim.index(mas_flowers[dpee_x[k]][dpee_y[k]])]
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
            if mas_flowers[x][y] in sunfl_anim:
                if time.time() - sunflower_times[x][y] > 7:
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
    global pee_coult, pee_y, pee_x, pee_anim
    global pee_shot_coult, pee_shot_y, pee_shot_x, pee_shot_anim
    if fl == "play":
        if len(zombies_x) < 6:
            zombies_x.append(1500)
            zombies_y.append(zombies_y_const[random.randrange(5)])
            zombie_eat_fl.append(0)
            zombie_anim_fl.append(0)
            zombies_anim.append(0)
            zombie_hp.append(40)
        for i in range(len(zombies_x)):
            if i >= len(zombie_hp):
                break
            if zombie_hp[i] <= 0:
                del zombies_x[i]
                del zombie_eat_fl[i]
                del zombies_y[i]
                del zombie_anim_fl[i]
                del zombie_hp[i]
                del zombies_anim[i]
            if i >= len(zombie_eat_fl):
                break
            if zombie_eat_fl[i] == 0:
                zombies_x[i] -= 1.4  # ---------------------------------------------------------------------------------
                screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))
                x1 = zombies_x[i] // 150
                y1 = (zombies_y[i]) // 150
                for y in range(5):
                    for x in range(9):
                        if mas_flowers[x][y] != nots:
                            if x1 == x and y1 == y:
                                zombie_eat_fl[i] = 1
                        if mas_flowers[x][y] in thorns_anim:
                            zombie_eat_fl[i] = 0
                            if x1 == x and y1 == y:
                                zombie_hp[i] -= 0.15
                        if mas_flowers[x][y] in tomato_anim:
                            if x1 == x and y1 == y:
                                zombie_hp[i] -= 1000
                                for i in range(len(tomato_x)):
                                    if tomato_x[i] == x and tomato_y[i] == y:
                                        mas_flowers[x][y] = POW
                if zombie_anim_fl[i] < 6:
                    zombie_anim_fl[i] += 1
                elif zombie_anim_fl[i] >= 6:
                    zombie_anim_fl[i] = 0
                    zombies_anim[i] += 1
                    zombies_anim[i] %= 3
            else:
                x1 = int(zombies_x[i] // 150)
                y1 = int(zombies_y[i] // 150)
                if mas_flowers[x1][y1] == nots:
                    zombie_eat_fl[i] = 0
                    zombies_anim[i] = 0
                dop_trash = zombies_anim[i]
                if dop_trash == 1 or dop_trash == 2:
                    zombies_anim[i] = 0
                    zombie_anim_fl[i] = 0
                if zombie_anim_fl[i] < 20:
                    zombie_anim_fl[i] += 1
                elif zombie_anim_fl[i] == 20:
                    zombie_anim_fl[i] = 0
                    zombies_anim[i] = 3 - zombies_anim[i]
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
                                    for j in range(len(pee_x)):
                                        if j >= len(pee_x):
                                            break
                                        if pee_x[j] == x and pee_y[j] == y:
                                            del pee_x[j]
                                            del pee_y[j]
                                            del pee_fl[j]
                                            del pee_coult[j]
                screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))


def draw_sun():
    global prev_time
    global flag_sun_1
    global flag_sun_2
    global flag_sun_3
    if fl == "play" and time.time() - prev_time > 10:
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
    for y in range(5):
        for x in range(9):
            if flag_sunflowers[x][y] == 1:
                screen.blit(sun, square_centres[x][y])
                sunflower_times[x][y] = time.time()


def draw_pee_shots():
    global pee_coult, pee_shot_y, pee_shot_x
    for i in range(len(pee_shot_x)):
        if len(pee_shot_x) <= i:
            i = 0
        screen.blit(pee_shot, (pee_shot_x[i], pee_shot_y[i]))
        pee_shot_x[i] += 13
        for j in range(len(zombies_x)):
            if j >= len(zombies_x) or i >= len(pee_shot_x):
                break
            if abs(zombies_x[j] - pee_shot_x[i]) <= 20 and zombies_y[j] // 150 + 1 == pee_shot_y[i] // 150:
                zombie_hp[j] -= 4
                # |++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                del pee_shot_x[i]
                del pee_shot_y[i]
        if len(pee_shot_x) <= i:
            break
        if pee_shot_x[i] > 1500:
            if i > len(pee_shot_x):
                break
            del pee_shot_x[i]
            del pee_shot_y[i]
    for i in range(len(pee_x)):
        for j in range(len(zombies_x)):
            if zombies_y[j] // 150 == pee_y[i] and pee_coult[i] == 0 and pee_x[i] <= zombies_x[j] // 155:
                pee_shot_x.append((pee_x[i] + 1) * 150 - 40)
                pee_shot_y.append((pee_y[i] + 1) * 150 + 42)
                pee_coult[i] = 300
            if pee_coult[i] > 0:
                pee_coult[i] -= 1


def cherry_bomb():
    global cherry_bomb_fl, cherry_x, cherry_y
    if cherry_bomb_fl == 49:
        for x in range(9):
            for y in range(5):
                if mas_flowers[x][y] == cherry:
                    mas_flowers[x][y] = nots
                    for k in range(len(zombies_x)):
                        if int(zombies_x[k] // 155 - x) <= 1 and int(zombies_y[k] // 155 - y) <= 1:
                            zombie_hp[k] = 0
                    break
    if 100 >= cherry_bomb_fl >= 50:
        screen.blit(Pow_cherry, (cherry_x + 50, cherry_y + 170))
    if cherry_bomb_fl < 101:
        cherry_bomb_fl += 2
    else:
        cherry_bomb_fl = 100
        cherry_x = -1000
        cherry_y = -1000


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
    tomato_1 = tomato = pygame.image.load("tomato_skin_1.png")
    tomato_2 = pygame.image.load("tomato_skin_2.png")
    tomato_x = []
    tomato_y = []
    tomato_fl = []
    tomato_anim = [tomato_1, tomato_2]
    sunfl_1 = sunflower = pygame.image.load("sunflower_skin_1.png")
    sunfl_2 = pygame.image.load("sunflower_skin_2.png")
    sunfl_x = []
    sunfl_y = []
    sunfl_fl = []
    sunfl_anim = [sunfl_1, sunfl_2]
    nut = pygame.image.load("nut.png")
    nut_1 = pygame.image.load("nut_2.png")
    nut_2 = pygame.image.load("nut_3.png")
    pee = pee_1 = pygame.image.load("pee_skin_1.png")
    pee_2 = pygame.image.load("pee_skin_2.png")
    pee_anim = [pee_1, pee_2]
    pee_fl = []
    pee_x = []
    pee_y = []
    pee_coult = []
    double_pee = dpee_1 = pygame.image.load("double_pee_skin_1.png")
    dpee_2 = pygame.image.load("double_pee_skin_2.png")
    dpee_anim = [dpee_1, dpee_2]
    dpee_fl = []
    dpee_x = []
    dpee_y = []
    dpee_coult = []
    pee_shot = pygame.image.load("pee_shot.png")
    pee_shot_x = []
    pee_shot_y = []
    cherry = pygame.image.load("cherry.png")
    cherry_bomb_fl = 100
    cherry_x = -1000
    cherry_y = -1000
    thorns = thorns_1 = pygame.image.load("thorns_skin_1.png")
    thorns_2 = pygame.image.load("thorns_skin_2.png")
    thorns_anim = [thorns_1, thorns_2]
    thorns_fl = []
    thorns_x = []
    thorns_y = []
    shovel = pygame.image.load("shovel.png")
    sun = pygame.image.load("sun.png")
    POW = pygame.image.load("POW.png")
    Pow_cherry = pygame.image.load("Pow_cherry.png")
    sun = pygame.transform.scale(sun, (50, 50))
    pos_mouse_x = -100
    pos_mouse_y = -100
    fl = "start"
    score = 5000
    # pygame.mixer.music.load('music_start.mp3')
    # pygame.mixer.music.play()
    running = True
    open_windows()
    clock_time.tick(60)
    pygame.display.flip()
    time_fl = 0
    cost = {pee: 100, nut: 50, cherry: 150, tomato: 50, thorns: 50, double_pee: 200, sunflower: 50}
    sunflower_times = [[100000000000 for _ in range(5)] for _ in range(9)]
    flag_sunflowers = [[0 for _ in range(5)] for _ in range(9)]
    square_centres = [[(y * 155, x * 155 + 155) for x in range(9)] for y in range(5)]
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
        draw_pee_shots()
        draw_zombies()
        cherry_bomb()
        draw_sun()
        draw_cursor((mouse_x, mouse_y))
        pygame.display.flip()
pygame.quit()
