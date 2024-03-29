import pygame
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
    if fl == "pause":
        pause_window()


def draw_cursor(coord):
    screen.blit(cursor, coord)


def pause_window():
    screen.blit(pause_page, (0, 0))


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
        pygame.mixer.music.load('second_music.mp3')
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
    global cherry_bomb_fl, cherry_x, cherry_y, sun_take, planting_sound
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
                    sun_take.play()
                    score += 25

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
            sun_take.play()
            prev_time = time.time()
        elif 1460 <= x <= 1510 and 80 <= y <= 130 and flag_sun_2:
            score += 25
            flag_sun_2 = 0
            sun_take.play()
            prev_time = time.time()
        elif 1450 <= x <= 1500 and 30 <= y <= 80 and flag_sun_3:
            score += 25
            flag_sun_3 = 0
            sun_take.play()
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
                planting_sound.play()
                if cursor == double_pee:
                    dpee_fl.append(time_now)
                    dpee_x.append(x)
                    dpee_y.append(y)
                    dpee_coult.append(time.time())
                    last_dpee_coult.append(time.time())
                    reload_double_pee = 10
                    flag_reload[4] = False
                    flag_start_reload[4] = True
                    last_reload_double_pee = time.time()
                if cursor == tomato:
                    tomato_fl.append(time.time())
                    tomato_x.append(x)
                    tomato_y.append(y)
                    reload_tomato = 40
                    flag_reload[0] = False
                    flag_start_reload[0] = True
                    last_reload_tomato = time.time()
                if cursor == thorns:
                    thorns_fl.append(time_now)
                    thorns_x.append(x)
                    thorns_y.append(y)
                    reload_thorns = 20
                    flag_reload[6] = False
                    flag_start_reload[6] = True
                    last_reload_thorns = now_time
                if cursor == pee:
                    pee_fl.append(time_now)
                    pee_x.append(x)
                    pee_y.append(y)
                    pee_coult.append(now_time)
                    last_pee_coult.append(now_time)
                    reload_pee = 7
                    flag_reload[2] = False
                    flag_start_reload[2] = True
                    last_reload_pee = now_time
                if cursor == nut:
                    hp_flowers[x][y] = 1000
                    reload_nut = 30
                    flag_reload[3] = False
                    flag_start_reload[3] = True
                    last_reload_nut = now_time
                if cursor == sunflower:
                    sunflower_times[x][y] = time_now
                    sunfl_fl.append(time_now)
                    sunfl_x.append(x)
                    sunfl_y.append(y)
                    flag_reload[1] = False
                    flag_start_reload[1] = True
                    reload_sunflower = 5
                    last_reload_sunflower = now_time
                if cursor == cherry:
                    cherry_bomb_fl = time_now
                    cherry_x = x * 150
                    cherry_y = y * 150
                    hp_flowers[x][y] = 100000
                    reload_cherry = 60
                    flag_reload[5] = False
                    flag_start_reload[5] = True
                    last_reload_cherry = now_time
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
                undig_sound.play()
                mas_flowers[x][y] = nots
                hp_flowers[x][y] = 0
            cursor = cursor_const
            fl_cursor = "const"


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
        if time_now - sunfl_fl[k] > 0.4 and mas_flowers[sunfl_x[k]][sunfl_y[k]] in sunfl_anim:
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
    global zombie_anim_fl, zombies_anim, zombies_x, zombies_y, zombie_eat_fl, last_run, tomato_sound
    global mas_flowers, zombie_hp, eating_sound
    global pee_coult, pee_y, pee_x, pee_anim, last_pee_coult
    global dpee_coult, dpee_y, dpee_x, dpee_anim, last_dpee_coult
    global pee_shot_coult, pee_shot_y, pee_shot_x, pee_shot_anim, lose_fl
    global zombie_helmet
    now_time = time.time()
    if i >= len(zombie_hp):
        return 0
    if zombie_hp[i] <= 0:
        del zombies_x[i]
        del zombie_eat_fl[i]
        del zombies_y[i]
        del zombie_anim_fl[i]
        del zombie_hp[i]
        del zombies_anim[i]
        del last_run[i]
        del zombie_helmet[i]
        die_sound.play()
    if i >= len(zombie_eat_fl) or i >= len(last_run):
        return 0
    if zombie_hp[i] <= 40:
        zombie_helmet[i] = nots
    if zombie_eat_fl[i] == 0:
        if len(zombie_anim_fl) <= i:
            return 0
        elif now_time - zombie_anim_fl[i] > 0.3:
            zombie_anim_fl[i] = now_time
            zombies_anim[i] += 1
            zombies_anim[i] %= 3
            if zombies_anim[i] == 0:
                zombies_anim[i] += 1
    if zombie_eat_fl[i] == 0 and now_time - last_run[i] >= 0.1:
        zombies_x[i] -= 2
        if zombies_x[i] < -100:
            lose_fl = 1
            return 0
        last_run[i] = now_time
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
                        zombie_hp[i] -= 0.2
                if mas_flowers[x][y] in tomato_anim:
                    if x1 == x and y1 == y:
                        zombie_hp[i] -= 1000
                        for i in range(len(tomato_x)):
                            if tomato_x[i] == x and tomato_y[i] == y:
                                tomato_sound.play()
                                mas_flowers[x][y] = POW
    elif now_time - last_run[i] >= 0.1:
        x1 = int(zombies_x[i] // 150)
        y1 = int(zombies_y[i] // 150)
        if mas_flowers[x1][y1] == nots:
            zombie_eat_fl[i] = 0
            zombies_anim[i] = 0
        dop_trash = zombies_anim[i]
        if dop_trash == 1 or dop_trash == 2:
            zombies_anim[i] = 0
            zombie_anim_fl[i] = now_time
        elif now_time - zombie_anim_fl[i] > 0.3:
            zombie_anim_fl[i] = now_time
            zombies_anim[i] = 3 - zombies_anim[i]
            for y in range(5):
                for x in range(9):
                    if x1 == x and y1 == y:
                        if x + 1 < 10:
                            if mas_flowers[x + 1][y] in thorns_anim:
                                zombie_hp[i] -= 0.7
                        eating_sound.play()
                        hp_flowers[x][y] -= 5
                        if hp_flowers[x][y] == 600:
                            mas_flowers[x][y] = nut_1
                        if hp_flowers[x][y] == 200:
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
    global zombie_anim_fl, zombies_anim, zombies_x, zombies_y, zombie_eat_fl, last_run
    global mas_flowers, zombie_hp
    global pee_coult, pee_y, pee_x, pee_anim, last_pee_coult
    global dpee_coult, dpee_y, dpee_x, dpee_anim, last_dpee_coult
    global pee_shot_coult, pee_shot_y, pee_shot_x, pee_shot_anim, win_fl, zombie_helmet
    global last_wave, fl_wave, start_time
    if last_wave == 2:
        last_wave = now_time
        start_time = now_time
    if now_time - last_wave >= 35 and waves[fl_wave] != -1:
        last_wave = now_time
        fl_wave += 1
    if len(zombies_x) == 0 and waves[fl_wave] == -1:
        win_fl = 1
        return 0
    if fl == "play":
        while len(zombies_x) < waves[fl_wave]:
            zombies_x.append(random.randrange(1700, 1900))
            zombies_y.append(zombies_y_const[random.randrange(5)])
            zombie_eat_fl.append(0)
            zombie_anim_fl.append(now_time)
            zombies_anim.append(0)
            last_run.append(now_time)
            if now_time - start_time >= 300:
                k = random.randrange(4)
            elif now_time - start_time >= 200:
                k = random.randrange(3)
            elif now_time - start_time >= 100:
                k = random.randrange(2)
            else:
                k = 0
            zombie_helmet.append(helmets[k])
            zombie_hp.append(40 + helmets_hp[k])
        if waves[fl_wave] % 10 == 0:
            fl_wave += 1
            last_wave = now_time
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
    global pee_coult, pee_shot_y, pee_shot_x, last_pee_coult, pee_pop
    for i in range(len(pee_shot_x)):
        if len(pee_shot_x) <= i:
            i = 0
        screen.blit(pee_shot, (pee_shot_x[i], pee_shot_y[i]))
        pee_shot_x[i] += 10
        for j in range(len(zombies_x)):
            if j >= len(zombies_x) or i >= len(pee_shot_x):
                break
            if abs(zombies_x[j] - pee_shot_x[i]) <= 20 and zombies_y[j] // 150 + 1 == pee_shot_y[i] // 150:
                damage_sound.play()
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
            if pee_coult[i] - last_pee_coult[i] >= 3 and zombies_y[j] // 150 == pee_y[i] \
                    and pee_x[i] <= zombies_x[j] // 155 and zombies_x[j] <= 1500:
                pee_shot_x.append((pee_x[i] + 1) * 150 - 40)
                pee_shot_y.append((pee_y[i] + 1) * 150 + 42)
                last_pee_coult[i] = pee_coult[i]
                pee_coult[i] = now_time
                pee_pop.play()
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
                pee_pop.play()
            dpee_coult[i] = now_time


def cherry_bomb():
    global cherry_bomb_fl, cherry_x, cherry_y, Pow_cherry_fl, cherry_fl, cherry_pow_2
    time_now = now_time
    if time_now - cherry_bomb_fl >= 1:
        cherry_x = -1000
        cherry_y = -1000
        for x in range(9):
            for y in range(5):
                if mas_flowers[x][y] == cherry:
                    cherry_fl = 0
                    cherry_pow_2.play()
                    mas_flowers[x][y] = Pow_cherry
                    for k in range(len(zombies_x)):
                        if abs(int(zombies_x[k] // 155 - x)) <= 1 and abs(int(zombies_y[k] // 155 - y)) <= 1:
                            zombie_hp[k] = 0
                        if zombie_eat_fl[k] == 1 and zombies_x[k] // 155 == x - 2 \
                                and abs(int(zombies_y[k] // 155 - y)) <= 1:
                            zombie_hp[k] = 0
                    break
                if mas_flowers[x][y] == Pow_cherry and cherry_fl == 0:
                    cherry_bomb_fl = time_now
                    cherry_fl = 1
                elif mas_flowers[x][y] == Pow_cherry:
                    mas_flowers[x][y] = nots


def reload():
    global reload_nut, reload_double_pee, reload_pee, reload_cherry, reload_tomato, reload_sunflower, reload_thorns
    global last_reload_nut, last_reload_double_pee, last_reload_pee, last_reload_cherry, \
        last_reload_tomato, last_reload_sunflower, last_reload_thorns, reload_sound, flag_reload, flag_start_reload
    i = 0.037
    now = time.time()
    if reload_nut > 0 and now - last_reload_nut >= i:
        last_reload_nut -= i
        reload_nut -= i
    if reload_sunflower > 0 and now - last_reload_sunflower >= i:
        last_reload_sunflower -= i
        reload_sunflower -= i
    if reload_thorns > 0 and now - last_reload_thorns >= i:
        last_reload_thorns -= i
        reload_thorns -= i
    if reload_pee > 0 and now - last_reload_pee >= i:
        last_reload_pee -= i
        reload_pee -= i
    if reload_double_pee > 0 and now - last_reload_double_pee >= i:
        last_reload_double_pee = i
        reload_double_pee -= i
    if reload_cherry > 0 and now - last_reload_cherry >= i:
        last_reload_cherry -= i
        reload_cherry -= i
    if reload_tomato > 0 and now - last_reload_tomato >= i:
        last_reload_tomato -= i
        reload_tomato -= i
    if int(reload_tomato + 0.999) == 0 and not flag_reload[0]:
        if flag_start_reload[0]:
            flag_reload[0] = True
            reload_sound.play()
    if int(reload_sunflower + 0.999) == 0 and not flag_reload[1]:
        if flag_start_reload[1]:
            flag_reload[1] = True
            reload_sound.play()
    if int(reload_pee + 0.999) == 0 and not flag_reload[2]:
        if flag_start_reload[2]:
            flag_reload[2] = True
            reload_sound.play()
    if int(reload_nut + 0.999) == 0 and not flag_reload[3]:
        if flag_start_reload[3]:
            flag_reload[3] = True
            reload_sound.play()
    if int(reload_double_pee + 0.999) == 0 and not flag_reload[4]:
        if flag_start_reload[4]:
            flag_reload[4] = True
            reload_sound.play()
    if int(reload_cherry + 0.999) == 0 and not flag_reload[5]:
        if flag_start_reload[5]:
            flag_reload[5] = True
            reload_sound.play()
    if int(reload_thorns + 0.999) == 0 and not flag_reload[6]:
        if flag_start_reload[6]:
            flag_reload[6] = True
            reload_sound.play()


def win():
    screen.blit(win_page, (0, 0))


def lose():
    screen.blit(not_win_page, (0, 0))


def draw_helmets():
    global zombie_helmet
    for i in range(len(zombie_helmet)):
        if zombie_helmet[i] == helmet:
            screen.blit(zombie_helmet[i], (zombies_x[i] + 15, zombies_y[i] - 30))
        if zombie_helmet[i] == conus:
            screen.blit(zombie_helmet[i], (zombies_x[i] + 20, zombies_y[i] - 25))
        if zombie_helmet[i] == bucket:
            screen.blit(zombie_helmet[i], (zombies_x[i] + 25, zombies_y[i] - 15))


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
    conus = pygame.image.load("conus.png")
    bucket = pygame.image.load("bucket.png")
    helmet = pygame.image.load("helmet.png")
    anim_number = [zombie_anim_1, zombie_anim_2, zombie_anim_3, zombie_anim_4]
    zombie_eat_fl = []
    zombie_anim_fl = []
    zombie_helmet = []
    zombie_hp = []
    last_wave = 2
    waves = [1, 2, 4, 6, 10, 6, 7, 8, 20, 9, 13, 12, 30, -1]
    fl_wave = 0
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 50)
    background = pygame.image.load("background.png").convert()
    help_background = pygame.image.load("help_background.png").convert()
    play_background = pygame.image.load("game_background.png").convert()
    Bplay = pygame.image.load("button_play.png").convert()
    Hplay = pygame.image.load("button_help.png").convert()
    Eplay = pygame.image.load("button_exit.png").convert()
    H_back = pygame.image.load("back_help.png").convert()
    win_page = pygame.image.load("win_page.png").convert()
    pause_page = pygame.image.load("pause_page.png").convert()
    not_win_page = pygame.image.load("not_win_page.png").convert()
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
    dpee_pps = [3, 0.5]
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
    helmets = [nots, conus, bucket, helmet]
    helmets_hp = [0, 25, 40, 80]
    fl = "start"
    score = 50
    reload_sunflower = reload_tomato = reload_pee = reload_double_pee = reload_nut = reload_thorns = reload_cherry = 0
    last_reload_sunflower = last_reload_tomato = last_reload_pee = last_reload_double_pee \
        = last_reload_nut = last_reload_thorns = last_reload_cherry = 0
    pygame.mixer.music.load('music_start.mp3')
    pygame.mixer.music.play()
    running = True
    open_windows()
    clock_time.tick(60)
    pygame.display.flip()
    last_run = []
    time_fl = 0
    cost = {pee: 100, nut: 50, cherry: 150, tomato: 50, thorns: 50, double_pee: 200, sunflower: 50}
    sunflower_times = [[100000000000 for _ in range(5)] for _ in range(9)]
    flag_sunflowers = [[0 for _ in range(5)] for _ in range(9)]
    square_centres = [[(y * 155, x * 155 + 155) for x in range(9)] for y in range(5)]
    flag_reload = [False for i in range(7)]
    flag_start_reload = [False for i in range(7)]
    pygame.mixer.music.set_volume(0.5)
    volume = pygame.mixer.music.get_volume()
    cherry_pow_2 = pygame.mixer.Sound('cherry_pow_2.mp3')
    pee_pop = pygame.mixer.Sound('pee_pop.mp3')
    sun_take = pygame.mixer.Sound('sun_take.mp3')
    reload_sound = pygame.mixer.Sound('reload_sound.mp3')
    planting_sound = pygame.mixer.Sound('planting_sound.mp3')
    eating_sound = pygame.mixer.Sound('eating_sound.mp3')
    tomato_sound = pygame.mixer.Sound('tomato_sound.mp3')
    undig_sound = pygame.mixer.Sound('undig.mp3')
    damage_sound = pygame.mixer.Sound('damage.mp3')
    die_sound = pygame.mixer.Sound('die.mp3')
    prev_time = 0
    flag_sun_1 = 0
    flag_sun_2 = 0
    flag_sun_3 = 0
    mouse_x = -100
    cherry_fl = 0
    mouse_y = -100
    lose_fl = 0
    start_time = 0
    now_time = -1
    # ---------------------------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                elif event.key == pygame.K_1:
                    pygame.mixer.music.load('first_music.mp3')
                    pygame.mixer.music.play()
                elif event.key == pygame.K_2:
                    pygame.mixer.music.load('second_music.mp3')
                    pygame.mixer.music.play()
                elif event.key == pygame.K_ESCAPE and fl == "pause":
                    fl = old_fl
                elif event.key == pygame.K_ESCAPE:
                    old_fl = fl
                    fl = "pause"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                cursor = cursor_const
                fl_cursor = "const"
            if event.type == pygame.VIDEOEXPOSE and now_time != -1 and fl != "pause":
                old_fl = fl
                fl = "pause"
            mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            pygame.display.flip()
            clock.tick(60)
            pygame.display.set_caption("Plants vs zombos")
        now_time = time.time()
        open_windows()
        if win_fl == 0 and lose_fl == 0 and fl != "pause":
            draw_plants()
            new_pee_shots()
            new_double_pee_shots()
            draw_pee_shots()
            draw_price()
            draw_reload()
            draw_zombies()
            draw_helmets()
            cherry_bomb()
            draw_sun()
            reload()
        elif win_fl == 1:
            win()
            cursor = cursor_const
        elif lose_fl == 1:
            lose()
            cursor = cursor_const
        draw_cursor((mouse_x, mouse_y))
        pygame.display.flip()
pygame.quit()
