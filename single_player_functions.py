import pygame
import Hangman_Draft_with_Hints_and_Scramble as func_file
import gui

HANGMAN_WORD = ""

pygame.init()

# Setting up display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Fonts and colors
BUTTON_FONT = pygame.font.SysFont('comicsans', 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setting up texts
heading = "Which topic do you choose to play Hangman"
sub_heading = "Options are -->"
options = ["Movies", "TV-Shows", "Sports", "Fruits", "Animals",
           "Random Words", "If you want to learn new words"]


# Displaying the text and boxes
def display_text():
    win.fill(WHITE)

    # main heading
    text_x = 10
    text_y = 10

    text1_main = BUTTON_FONT.render(heading, 1, BLACK)
    win.blit(text1_main, (text_x, text_y))

    text_y += 75

    # sub heading
    text2_main = BUTTON_FONT.render(sub_heading, 1, BLACK)
    win.blit(text2_main, (text_x, text_y))
    text_y += 60

    for words in options:
        text_sub = BUTTON_FONT.render(words, 1, BLACK)
        win.blit(text_sub, (text_x, text_y))

        pygame.draw.rect(win, BLACK, pygame.Rect(text_x - 5, text_y, text_sub.get_width() + 10,
                                                 text_sub.get_height() + 5), 2)

        text_y += 50

    pygame.display.update()


def start():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Collision detection and choosing topic
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                x = 10
                y = 145

                for words in options:

                    text_sub = BUTTON_FONT.render(words, 1, BLACK)

                    if (x - 5 < m_x < x + text_sub.get_width() + 5) and (y < m_y < y + text_sub.get_height()):
                        global HANGMAN_WORD
                        HANGMAN_WORD = func_file.choosing_word(words)
                        gui.reset()

                    y += 50

        display_text()


def word():
    global HANGMAN_WORD
    return HANGMAN_WORD