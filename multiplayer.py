import pygame

import gui

pygame.init()

# Setting up the win
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Font and colors
font = 'comicsans'
HEADING_FONT = pygame.font.SysFont(font, 35)
FONT = pygame.font.SysFont(font, 25)
BLACK = (0, 0, 0)

text = ""


# Heading
def head():
    heading_txt = 'Enter Hangman Word'
    heading = HEADING_FONT.render(heading_txt, 1, BLACK)
    win.blit(heading, (50, 10))


clock = pygame.time.Clock()


def multiplayer():
    global text, FONT, HEADING_FONT

    HEADING_FONT = pygame.font.SysFont(font, 35)
    FONT = pygame.font.SysFont(font, 25)

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
    Text = False
    for a in text:
        if a.isalpha() == 0:
            if a != " ":
                print("Dont use symbols fuckhead")
                retry()
        else:
            Text = True
    if Text:
        return text
    else:
        print("Type something fucker")
        retry()


def retry():
    global text
    text = ""
    multiplayer()


def update_font(new_font):
    global font
    font = new_font
