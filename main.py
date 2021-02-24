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
        pygame.mixer.music.load('1.mp3')
        pygame.mixer.music.play()
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
    global reload_nut, reload_double_pee, reload_pee, reload_sunflower, reload_tomato, reload_cherry, reload_thorns
    global last_reload_sunflower, last_reload_tomato, last_reload_pee, last_reload_double_pee \
        , last_reload_nut, last_reload_thorns, last_reload_cherry
    now_time = time.time()
    x, y = coord[0], coord[1]
    if y > 155:
        for i in range(5):
            for j in range(9):
                if square_centres[i][j][0] + 50 >= x >= square_centres[i][j][0] \
                        and square_centres[i][j][1] + 50 >= y >= square_centres[i][j][1] and flag_sunflowers[i][j] == 1:
                    flag_sunflowers[i][j] = 0
                    score += 50

    elif 155 >= y >= 0:
        if 155 >= x >= 1 and check_score(50) and int(reload_tomato + 0.999) == 0:
            cursor = tomato
        elif 256 >= x >= 156 and check_score(50) and int(reload_sunflower + 0.999) == 0:
            cursor = sunflower
        elif 406 >= x >= 306 and check_score(100) and int(reload_pee + 0.999) == 0:
            cursor = pee
        elif 556 >= x >= 456 and check_score(50) and int(reload_nut + 0.999) == 0:
            cursor = nut
        elif 706 >= x >= 606 and check_score(200) and int(reload_double_pee + 0.999) == 0:
            cursor = double_pee
        elif 856 >= x >= 756 and check_score(150) and int(reload_cherry + 0.999) == 0:
            cursor = cherry
        elif 1006 >= x >= 906 and check_score(125) and int(reload_thorns + 0.999) == 0:
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
        time_now = time.time()
        if 930 >= y >= 155 and 1550 >= x >= 1:
            x = x // 155
            y = (y - 155) // 155
            if mas_flowers[x][y] == nots and cursor != shovel:
                score -= cost[cursor]
                mas_flowers[x][y] = cursor
                hp_flowers[x][y] = 50
                if cursor == double_pee:
                    dpee_fl.append(time_now)
                    dpee_x.append(x)
                    dpee_y.append(y)
                    dpee_coult.append(time.time())
                    last_dpee_coult.append(time.time())
                    reload_double_pee = 10
                    last_reload_double_pee = time.time()
                if cursor == tomato:
                    tomato_fl.append(time.time())
                    tomato_x.append(x)
                    tomato_y.append(y)
                    reload_tomato = 40
                    last_reload_tomato = time.time()
                if cursor == thorns:
                    thorns_fl.append(time_now)
                    thorns_x.append(x)
                    thorns_y.append(y)
                    reload_thorns = 20
                    last_reload_thorns =  now_time
                if cursor == pee:
                    pee_fl.append(time_now)
                    pee_x.append(x)
                    pee_y.append(y)
                    pee_coult.append( now_time)
                    last_pee_coult.append( now_time)
                    reload_pee = 7
                    last_reload_pee =  now_time
                if cursor == nut:
                    hp_flowers[x][y] = 500
                    reload_nut = 30
                    last_reload_nut =  now_time
                if cursor == sunflower:
                    sunflower_times[x][y] = time_now
                    sunfl_fl.append(time_now)
                    sunfl_x.append(x)
                    sunfl_y.append(y)
                    reload_sunflower = 5
                    last_reload_sunflower =  now_time
                if cursor == cherry:
                    cherry_bomb_fl = time_now
                    cherry_x = x * 150
                    cherry_y = y * 150
                    hp_flowers[x][y] = 1000
                    reload_cherry = 60
                    last_reload_cherry =  now_time
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
                            del last_pee_coult[i]
                if mas_flowers[x][y] in dpee_anim:
                    for i in range(len(dpee_x)):
                        if i >= len(dpee_x):
                            break
                        if dpee_x[i] == x and dpee_y[i] == y:
                            del dpee_x[i]
                            del dpee_y[i]
                            del dpee_fl[i]
                            del dpee_coult[i]
                            del last_dpee_coult[i]
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
    time_now = time.time()
    for k in range(len(thorns_fl)):
        if time_now - thorns_fl[k] > 0.2 and mas_flowers[thorns_x[k]][thorns_y[k]] in thorns_anim:
            thorns_fl[k] = time_now
            mas_flowers[thorns_x[k]][thorns_y[k]] = thorns_anim[
                1 - thorns_anim.index(mas_flowers[thorns_x[k]][thorns_y[k]])]
    for k in range(len(tomato_fl)):
        if time_now - tomato_fl[k] > 0.2 and mas_flowers[tomato_x[k]][tomato_y[k]] in tomato_anim:
            tomato_fl[k] = time_now
            mas_flowers[tomato_x[k]][tomato_y[k]] = tomato_anim[
                1 - tomato_anim.index(mas_flowers[tomato_x[k]][tomato_y[k]])]
    for k in range(len(sunfl_fl)):
        if time_now - sunfl_fl[k] > 0.2 and mas_flowers[sunfl_x[k]][sunfl_y[k]] in sunfl_anim:
            sunfl_fl[k] = time_now
            mas_flowers[sunfl_x[k]][sunfl_y[k]] = sunfl_anim[
                1 - sunfl_anim.index(mas_flowers[sunfl_x[k]][sunfl_y[k]])]
    for k in range(len(pee_fl)):
        if time_now - pee_fl[k] > 0.2 and mas_flowers[pee_x[k]][pee_y[k]] in pee_anim:
            pee_fl[k] = time_now
            mas_flowers[pee_x[k]][pee_y[k]] = pee_anim[
                1 - pee_anim.index(mas_flowers[pee_x[k]][pee_y[k]])]
    for k in range(len(dpee_fl)):
        if time_now - dpee_fl[k] > 0.2 and mas_flowers[dpee_x[k]][dpee_y[k]] in dpee_anim:
            dpee_fl[k] = time_now
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
                if time.time() - sunflower_times[x][y] > 13:
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


def draw_price():
    if fl == "play":
        screen.blit(font.render("50", True, black), [105, 100])
        screen.blit(font.render("50", True, black), [255, 100])
        screen.blit(font.render("100", True, black), [385, 100])
        screen.blit(font.render("50", True, black), [560, 100])
        screen.blit(font.render("200", True, black), [690, 100])
        screen.blit(font.render("150", True, black), [845, 100])
        screen.blit(font.render("125", True, black), [995, 100])


def toFixed(numObj, digits=0):
    return abs(float(f"{numObj:.{digits}f}"))


def draw_reload():
    if fl == "play":
        screen.blit(font.render(str(toFixed(float(reload_tomato), 1)), True, black), [10, 100])
        screen.blit(font.render(str(toFixed(float(reload_sunflower), 1)), True, black), [160, 100])
        screen.blit(font.render(str(toFixed(float(reload_pee), 1)), True, black), [310, 100])
        screen.blit(font.render(str(toFixed(float(reload_nut), 1)), True, black), [460, 100])
        screen.blit(font.render(str(toFixed(float(reload_double_pee), 1)), True, black), [615, 100])
        screen.blit(font.render(str(int(reload_cherry)), True, black), [765, 100])
        screen.blit(font.render(str(toFixed(float(reload_thorns), 1)), True, black), [920, 100])


def draw_sort_zombies(i):
    global zombie_anim_fl, zombies_anim, zombies_x, zombies_y, zombie_eat_fl
    global mas_flowers, zombie_hp
    global pee_coult, pee_y, pee_x, pee_anim, last_pee_coult
    global dpee_coult, dpee_y, dpee_x, dpee_anim, last_dpee_coult
    global pee_shot_coult, pee_shot_y, pee_shot_x, pee_shot_anim
    global kolvo_zombie, zombie_waves, zombie_wave_fl
    if i >= len(zombie_hp):
        return 0
    if zombie_hp[i] <= 0:
        del zombies_x[i]
        del zombie_eat_fl[i]
        del zombies_y[i]
        del zombie_anim_fl[i]
        del zombie_hp[i]
        del zombies_anim[i]
    if i >= len(zombie_eat_fl):
        return 0
    if zombie_eat_fl[i] == 0:
        zombies_x[i] -= 1.4
        screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))
        x1 = zombies_x[i] // 150
        y1 = (zombies_y[i]) // 150
        for y in range(5):
            for x in range(9):
                if mas_flowers[x][y] != nots:
                    if x1 == x and y1 == y:
                        zombie_eat_fl[i] = 1
                if mas_flowers[x][y] in thorns_anim:
                    if x1 == x and y1 == y:
                        zombie_eat_fl[i] = 0
                        zombie_hp[i] -= 0.15
                if mas_flowers[x][y] in tomato_anim:
                    if x1 == x and y1 == y:
                        zombie_hp[i] -= 1000
                        for i in range(len(tomato_x)):
                            if tomato_x[i] == x and tomato_y[i] == y:
                                mas_flowers[x][y] = POW
        if len(zombie_anim_fl) <= i:
            return 0
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
                        if x + 1 < 10:
                            if mas_flowers[x + 1][y] in thorns_anim:
                                zombie_hp[i] -= 3
                        hp_flowers[x][y] -= 10
                        if hp_flowers[x][y] == 300:
                            mas_flowers[x][y] = nut_1
                        if hp_flowers[x][y] == 100:
                            mas_flowers[x][y] = nut_2
                        if hp_flowers[x][y] == 0:
                            mas_flowers[x][y] = nots
                            zombie_eat_fl[i] = 0
                            for j1 in range(len(pee_x)):
                                if j1 >= len(pee_x):
                                    break
                                if pee_x[j1] == x and pee_y[j1] == y:
                                    del pee_x[j1]
                                    del pee_y[j1]
                                    del pee_fl[j1]
                                    del pee_coult[j1]
                                    del last_pee_coult[j1]
                            for j2 in range(len(dpee_x)):
                                if j2 >= len(dpee_x):
                                    break
                                if dpee_x[j2] == x and dpee_y[j2] == y:
                                    del dpee_x[j2]
                                    del dpee_y[j2]
                                    del dpee_fl[j2]
                                    del dpee_coult[j2]
                                    del last_dpee_coult[j2]
        screen.blit(anim_number[zombies_anim[i]], (zombies_x[i], zombies_y[i]))


def draw_zombies():
    global zombie_anim_fl, zombies_anim, zombies_x, zombies_y, zombie_eat_fl
    global mas_flowers, zombie_hp
    global pee_coult, pee_y, pee_x, pee_anim, last_pee_coult
    global dpee_coult, dpee_y, dpee_x, dpee_anim, last_dpee_coult
    global pee_shot_coult, pee_shot_y, pee_shot_x, pee_shot_anim
    global kolvo_zombie, zombie_waves, zombie_wave_fl
    if zombie_waves[kolvo_zombie] == 10 or zombie_waves[kolvo_zombie] == 20 or zombie_waves[kolvo_zombie] == 30:
        zombie_wave_fl += 750
    kolvo_zombie = zombie_wave_fl // 750 + 1
    print(zombie_waves[kolvo_zombie])
    zombie_wave_fl += 1
    if fl == "play":
        while len(zombies_x) < zombie_waves[kolvo_zombie]:
            zombies_x.append(1700)
            zombies_y.append(zombies_y_const[random.randrange(5)])
            zombie_eat_fl.append(0)
            zombie_anim_fl.append(0)
            zombies_anim.append(0)
            zombie_hp.append(40)
        for i in range(len(zombies_x)):
            if len(zombies_y) > i and (zombies_y[i] - 100) // 150 == 0:
                draw_sort_zombies(i)
        for i in range(len(zombies_x)):
            if len(zombies_y) > i and (zombies_y[i] - 100) // 150 == 1:
                draw_sort_zombies(i)
        for i in range(len(zombies_x)):
            if len(zombies_y) > i and (zombies_y[i] - 100) // 150 == 2:
                draw_sort_zombies(i)
        for i in range(len(zombies_x)):
            if len(zombies_y) > i and (zombies_y[i] - 100) // 150 == 3:
                draw_sort_zombies(i)
        for i in range(len(zombies_x)):
            if len(zombies_y) > i and (zombies_y[i] - 100) // 150 == 4:
                draw_sort_zombies(i)


def draw_sun():
    global prev_time
    global flag_sun_1
    global flag_sun_2
    global flag_sun_3
    if fl == "play" and time.time() - prev_time > 14:
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
    global pee_coult, pee_shot_y, pee_shot_x, last_pee_coult
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
                del pee_shot_x[i]
                del pee_shot_y[i]
        if len(pee_shot_x) <= i:
            break
        if pee_shot_x[i] > 1500:
            if i > len(pee_shot_x):
                break
            del pee_shot_x[i]
            del pee_shot_y[i]


def new_pee_shots():
    global pee_coult, pee_shot_y, pee_shot_x, last_pee_coult
    now_time = time.time()
    for i in range(len(pee_x)):
        for j in range(len(zombies_x)):
            pee_coult[i] = now_time
            if pee_coult[i] - last_pee_coult[i] >= 2 and zombies_y[j] // 150 == pee_y[i] \
                    and pee_x[i] <= zombies_x[j] // 155 and zombies_x[j] <= 1500:
                pee_shot_x.append((pee_x[i] + 1) * 150 - 40)
                pee_shot_y.append((pee_y[i] + 1) * 150 + 42)
                last_pee_coult[i] = pee_coult[i]
                pee_coult[i] = now_time
            pee_coult[i] = now_time


def new_double_pee_shots():
    global dee_coult, dpee_shot_y, dpee_shot_x, last_dpee_coult, dpee_pps_fl
    now_time = time.time()
    for i in range(len(dpee_x)):
        for j in range(len(zombies_x)):
            dpee_coult[i] = time.time()
            if dpee_coult[i] - last_dpee_coult[i] >= dpee_pps[dpee_pps_fl] and zombies_y[j] // 150 == dpee_y[i] \
                    and dpee_x[i] <= zombies_x[j] // 155 and zombies_x[j] <= 1500:
                pee_shot_x.append((dpee_x[i] + 1) * 150 - 40)
                pee_shot_y.append((dpee_y[i] + 1) * 150 + 42)
                last_dpee_coult[i] = dpee_coult[i]
                dpee_pps_fl = 1 - dpee_pps_fl
            dpee_coult[i] = now_time


def cherry_bomb():
    global cherry_bomb_fl, cherry_x, cherry_y, Pow_cherry_fl
    time_now = time.time()
    if time_now - cherry_bomb_fl >= 2:
        Pow_cherry_fl = time_now
        cherry_x = -1000
        cherry_y = -1000
        for x in range(9):
            for y in range(5):
                if mas_flowers[x][y] == cherry:
                    mas_flowers[x][y] = Pow_cherry
                    for k in range(len(zombies_x)):
                        if abs(int(zombies_x[k] // 155 - x)) <= 1 and abs(int(zombies_y[k] // 155 - y)) <= 1:
                            zombie_hp[k] = 0
                        if zombie_eat_fl[k] == 1 and zombies_x[k] // 155 == x - 2 \
                                and abs(int(zombies_y[k] // 155 - y)) <= 1:
                            zombie_hp[k] = 0
                    break
                if mas_flowers[x][y] == Pow_cherry:
                    mas_flowers[x][y] = nots


def reload():
    global reload_nut, reload_double_pee, reload_pee, reload_cherry, reload_tomato, reload_sunflower, reload_thorns
    global last_reload_nut, last_reload_double_pee, last_reload_pee, last_reload_cherry, \
        last_reload_tomato, last_reload_sunflower, last_reload_thorns
    i = 0.1
    if reload_nut > 0 and now - last_reload_nut >= 1000:
        last_reload_nut = now
        reload_nut -= i
    if reload_sunflower > 0 and now - last_reload_sunflower >= 50:
        last_reload_sunflower = now
        reload_sunflower -= i
    if reload_thorns > 0 and now - last_reload_thorns >= 1000:
        last_reload_thorns = now
        reload_thorns -= i
    if reload_pee > 0 and now - last_reload_pee >= 1000:
        last_reload_pee = now
        reload_pee -= i
    if reload_double_pee > 0 and now - last_reload_double_pee >= 1000:
        last_reload_double_pee = now
        reload_double_pee -= i
    if reload_cherry > 0 and now - last_reload_cherry >= 1000:
        last_reload_cherry = now
        reload_cherry -= i
    if reload_tomato > 0 and now - last_reload_tomato >= 1000:
        last_reload_tomato = now
        reload_tomato -= i


def win_text():
    screen.blit(font.render("win", True, black), [750, 500])


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
    win_fl = 0
    mas_flowers = [[nots] * 10 for i in range(10)]
    hp_flowers = [[0] * 10 for i in range(10)]
    for i in range(9):
        for j in range(5):
            mas_flowers[i][j] = nots
            hp_flowers[i][j] = 0
    black = pygame.Color("black")
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
    zombie_waves = [0, 1, 2, 4, 10, 5, 4, 7, 20, 11, 9, 13, 30, 0]
    zombie_wave_fl = -400
    kolvo_zombie = 0
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
    last_pee_coult = []
    dpee_pps = [2, 0.3]
    dpee_pps_fl = 0
    double_pee = dpee_1 = pygame.image.load("double_pee_skin_1.png")
    dpee_2 = pygame.image.load("double_pee_skin_2.png")
    dpee_anim = [dpee_1, dpee_2]
    dpee_fl = []
    dpee_x = []
    dpee_y = []
    dpee_coult = []
    last_dpee_coult = []
    pee_shot = pygame.image.load("pee_shot.png")
    pee_shot_x = []
    pee_shot_y = []
    cherry = pygame.image.load("cherry.png")
    cherry_bomb_fl = time.time()
    Pow_cherry_fl = 100000000
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
    score = 5000.
    reload_sunflower = reload_tomato = reload_pee = reload_double_pee = reload_nut = reload_thorns = reload_cherry = 0
    last_reload_sunflower = last_reload_tomato = last_reload_pee = last_reload_double_pee \
        = last_reload_nut = last_reload_thorns = last_reload_cherry = 0
    pygame.mixer.music.load('music_start.mp3')
    pygame.mixer.music.play()
    running = True
    open_windows()
    clock_time.tick(60)
    pygame.display.flip()
    time_fl = 0
    cost = {pee: 100, nut: 50, cherry: 150, tomato: 50, thorns: 50, double_pee: 200, sunflower: 50}
    sunflower_times = [[100000000000 for _ in range(5)] for _ in range(9)]
    flag_sunflowers = [[0 for _ in range(5)] for _ in range(9)]
    square_centres = [[(y * 155, x * 155 + 155) for x in range(9)] for y in range(5)]
    pygame.mixer.music.set_volume(0.5)
    volume = pygame.mixer.music.get_volume()
    prev_time = 0
    flag_sun_1 = 0
    flag_sun_2 = 0
    flag_sun_3 = 0
    mouse_x = -100
    mouse_y = -100
    # ---------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                cursor = cursor_const
                fl_cursor = "const"
            mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            pygame.display.flip()
            clock.tick(60)
            pygame.display.set_caption("fps: " + str(clock.get_fps()))
        pygame.time.Clock().tick()
        now = pygame.time.get_ticks()
        open_windows()
        if win_fl == 0:
            draw_plants()
            new_pee_shots()
            new_double_pee_shots()
            draw_pee_shots()
            draw_price()
            draw_reload()
            draw_zombies()
            cherry_bomb()
            draw_sun()
            reload()
        else:
            win_text()
            cursor = cursor_const
        draw_cursor((mouse_x, mouse_y))
        pygame.display.flip()
pygame.quit()
