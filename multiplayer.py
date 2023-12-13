import pygame

import gui

pygame.init()

# Setting up the win
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Font and colors
HEADING_FONT = pygame.font.SysFont('comicsans', 35)
FONT = pygame.font.SysFont('comicsans', 25)
BLACK = (0, 0, 0)

text = ""


# Heading
def head():
    heading_txt = 'Enter Hangman Word'
    heading = HEADING_FONT.render(heading_txt, 1, BLACK)
    win.blit(heading, (50, 10))


clock = pygame.time.Clock()


def multiplayer():
    global text
    text = ""

    while True:

        win.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gui.reset_multi()
                    pygame.quit()
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode


        txt_surface = FONT.render(text, 1, BLACK)
        win.blit(txt_surface, (50, 100))
        head()

        pygame.display.update()
        clock.tick(30)


def get_word():
    for a in text:
        if a.isalpha() == 0:
            if a != " ":
                print("Dont use symbols fuckhead")
                retry()

    return text


def retry():
    global text
    text = ""
    multiplayer()
