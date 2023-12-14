import pygame

pygame.init()

# Setting up display
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Fonts and Colours
font_name = 'comicsans'
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fonts_exit_x = 0
fonts_exit_y = 0

# Custom_fonts
arial = 'arial'
free_mono = 'freemono'
comicsans = 'comicsans'

option_arial = pygame.font.SysFont(arial, 40)
option_free_mono = pygame.font.SysFont(free_mono, 40)
option_comicsans = pygame.font.SysFont(comicsans, 40)

# Variables

font_1 = option_arial.render(arial, 1, BLACK)
font_2 = option_free_mono.render(free_mono, 1, BLACK)
font_3 = option_comicsans.render(comicsans, 1, BLACK)


# Drawing the buttons
def font_buttons():
    win.fill(WHITE)

    global font_name, fonts_exit_x, fonts_exit_y

    # heading
    heading1 = pygame.font.SysFont(font_name, 50)
    fonts_heading = heading1.render("FONTS", 1, BLACK)
    win.blit(fonts_heading, (10, 10))

    # confirm
    confirm = pygame.font.SysFont(font_name, 30)
    fonts_exit = confirm.render("OK->", 1, BLACK)
    win.blit(fonts_exit, (910, 440))
    fonts_exit_x = fonts_exit.get_width()
    fonts_exit_y = fonts_exit.get_height()

    pygame.draw.rect(win, BLACK, pygame.Rect(900, 430, fonts_exit_x + 20, fonts_exit_y + 20), 2)


    # Custom fonts
    pygame.draw.rect(win, BLACK, pygame.Rect(font_1.get_width() + 20, 160, 30, 30), 2)
    win.blit(font_1, (10, 150))
    if font_name == arial:
        pygame.draw.rect(win, BLACK, pygame.Rect(font_1.get_width() + 27.75, 167.75, 15, 15))

    pygame.draw.rect(win, BLACK, pygame.Rect(font_2.get_width() + 20, 260, 30, 30), 2)
    win.blit(font_2, (10, 250))
    if font_name == free_mono:
        pygame.draw.rect(win, BLACK, pygame.Rect(font_2.get_width() + 27.75, 267.75, 15, 15))

    pygame.draw.rect(win, BLACK, pygame.Rect(font_3.get_width() + 20, 370, 30, 30), 2)
    win.blit(font_3, (10, 350))
    if font_name == comicsans:
        pygame.draw.rect(win, BLACK, pygame.Rect(font_3.get_width() + 27.75, 377.75, 15, 15))

    pygame.display.update()


# Game loop

def settings():
    while True:
        font_buttons()

        global font_name, fonts_exit_x, fonts_exit_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check collision / button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                if (font_1.get_width() + 20 < m_x < font_1.get_width() + 50) and \
                        (160 < m_y < 190):
                    font_name = arial
                elif (font_2.get_width() + 20 < m_x < font_2.get_width() + 50) and \
                        (260 < m_y < 290):
                    font_name = free_mono
                elif (font_3.get_width() + 20 < m_x < font_3.get_width() + 50) and \
                        (370 < m_y < 400):
                    font_name = comicsans
                elif (900 < m_x < 920 + fonts_exit_x) and (430 < m_y < 450 + fonts_exit_y):
                    return font_name


def settings_start():
    return settings()
