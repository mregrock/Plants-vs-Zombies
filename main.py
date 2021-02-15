import pygame


def draw_cursor(coord, cursor):
    pygame.mouse.set_visible(False)
    screen.fill(pygame.Color('black'))
    screen.blit(cursor, coord)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Plants vs monsters")
    size = width, height = 1500, 1000
    screen = pygame.display.set_mode(size)
    cursor = pygame.image.load("cursor.png")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    draw_cursor(pygame.mouse.get_pos(), cursor)
                else:
                    screen.fill(pygame.Color('black'))
                pygame.display.flip()

    pygame.quit()