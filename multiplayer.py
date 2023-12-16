import pygame
import gui
import menu

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

word_text = ""

player1ready = False
player2ready = False

player1 = ''
player2 = ''

player1_turn = True
player2_turn = False

player1_score = 0
player2_score = 0


# Heading
def head():
    heading_txt = 'Enter Hangman Word'
    heading = HEADING_FONT.render(heading_txt, 1, BLACK)
    win.blit(heading, (50, 10))


clock = pygame.time.Clock()


def multiplayer():
    global word_text, FONT, HEADING_FONT, player1, player2, player1_score, player2_score, \
        player1ready, player2ready, player1_turn, player2_turn

    HEADING_FONT = pygame.font.SysFont(font, 35)
    FONT = pygame.font.SysFont(font, 25)

    word_text = ""

    while True:

        win.fill((255, 255, 255))

        # Display prompts for typing name
        if player1ready == 0:
            player1_text = HEADING_FONT.render("Enter player one's name", 1, BLACK)
            win.blit(player1_text, (50, 10))
            player1_surface = FONT.render(player1, 1, BLACK)
            win.blit(player1_surface, (50, 100))

        elif player2ready == 0:
            player2_text = HEADING_FONT.render("Enter player two's name", 1, BLACK)
            win.blit(player2_text, (50, 10))
            player2_surface = FONT.render(player2, 1, BLACK)
            win.blit(player2_surface, (50, 100))

        # Display prompts for typing word
        if player1ready and player2ready:
            if player1_turn:
                text = HEADING_FONT.render(player1 + 's turn, Enter the hangman word: ', 1, BLACK)
                win.blit(text, (50, 10))

            elif player2_turn:
                text = HEADING_FONT.render(player2 + 's turn, Enter the hangman word: ', 1, BLACK)
                win.blit(text, (50, 10))

            word_surface = FONT.render(word_text, 1, BLACK)
            win.blit(word_surface, (50, 100))

        # Game start loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if player1ready == 0:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player1ready = True
                    elif event.key == pygame.K_BACKSPACE:
                        player1 = player1[:-1]
                    else:
                        player1 += event.unicode

            elif player2ready == 0:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player2ready = True
                    elif event.key == pygame.K_BACKSPACE:
                        player2 = player2[:-1]
                    else:
                        player2 += event.unicode

            if player1ready and player2ready:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gui.reset_multi()
                        pygame.quit()
                    elif event.key == pygame.K_BACKSPACE:
                        word_text = word_text[:-1]
                    else:
                        word_text += event.unicode


        pygame.display.update()
        clock.tick(30)


def get_word():
    Text = False
    for a in word_text:
        if a.isalpha() == 0:
            if a != " ":
                print("Dont use symbols fuckhead")
                retry()
        else:
            Text = True
    if Text:
        return word_text
    else:
        print("Type something fucker")
        retry()


def retry():
    global word_text
    word_text = ""
    multiplayer()


def update_font(new_font):
    global font
    font = new_font


def winning_screen(status):

    global player1, player2, player1ready, player2ready

    if (player1ready == 0) and (player2ready == 0):
        menu.main_menu()

    elif status == "win":
        if player1_turn:
            print(player1, "wins")
        elif player2_turn:
            print(player2, "wins")

    elif status == "lose":
        if player1_turn:
            print(player1, "loses")
        elif player2_turn:
            print(player2, "loses")


def check_multiplayer():
    if (player1ready == 0) and (player2ready == 0):
        return False
    else:
        return True

