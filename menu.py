import pygame
import single_player_functions as single
import multiplayer

pygame.init()

# Setting up display
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Fonts and colors
BUTTON_FONT = pygame.font.SysFont('comicsans', 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Solo or multiplayer buttons
solo_text = "SINGLE PLAYER"
multiplayer_text = "MULTIPLAYER"

text1 = BUTTON_FONT.render(solo_text, 1, BLACK)
text2 = BUTTON_FONT.render(multiplayer_text, 1, BLACK)

solox = (WIDTH - text1.get_width()) / 2
soloy = (HEIGHT - text1.get_height()) / 2 - text1.get_height() * 2

multix = (WIDTH - text2.get_width()) / 2
multiy = (HEIGHT - text2.get_height()) / 2 + text2.get_height() - 10


def buttons():
    win.fill(WHITE)

    pygame.draw.rect(win, BLACK, pygame.Rect(solox - 30, soloy - 20, text1.get_width() + 60, text1.get_height() + 40),
                     2)
    win.blit(text1, (solox, soloy))

    pygame.draw.rect(win, BLACK, pygame.Rect(multix - 42, multiy - 20, text2.get_width() + 84, text2.get_height() + 40),
                     2)
    win.blit(text2, (multix, multiy))

    pygame.display.update()


# game loop
def main_menu():
    while True:

        buttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # check collision / button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                if (solox - 30 < m_x < solox - 30 + text1.get_width() + 60) and \
                        (soloy - 20 < m_y < soloy - 20 + text1.get_height() + 40):
                    print("SINGLE PLAYER")
                    single.start()

                elif (multix - 42 < m_x < multix - 42 + text2.get_width() + 84) and \
                        (multiy - 20 < m_y < multiy - 20 + text2.get_height() + 40):
                    print("MULTI PLAYER")
                    multiplayer.multiplayer()


def forced_quit():
    pygame.quit()


main_menu()
