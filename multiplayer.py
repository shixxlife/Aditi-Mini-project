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
                text = HEADING_FONT.render(player1 + "'s turn, Enter the hangman word: ", 1, BLACK)
                win.blit(text, (50, 10))

            elif player2_turn:
                text = HEADING_FONT.render(player2 + "'s turn, Enter the hangman word: ", 1, BLACK)
                win.blit(text, (50, 10))

            word_surface = FONT.render(word_text, 1, BLACK)
            win.blit(word_surface, (50, 100))

        # Game start loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if player1ready and player2ready:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("executed")
                        gui.reset_multi()
                        pygame.quit()
                    elif event.key == pygame.K_BACKSPACE:
                        word_text = word_text[:-1]
                    else:
                        word_text += event.unicode

            elif player1ready == 0:

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


def buttons():
    continue_button = HEADING_FONT.render("Next round ->", 1, BLACK)
    win.blit(continue_button, (1000 - continue_button.get_width() - 10,
                               500 - continue_button.get_height() - 10))
    pygame.draw.rect(win, BLACK,
                     pygame.Rect(1000 - continue_button.get_width() - 15, 500 - continue_button.get_height() - 10,
                                 continue_button.get_width() + 10,
                                 continue_button.get_height() + 5), 2)


    finish_button = HEADING_FONT.render("Finish game", 1, BLACK)
    win.blit(finish_button, (10, 500 - continue_button.get_height() - 10))
    pygame.draw.rect(win, BLACK,
                     pygame.Rect(5, 500 - finish_button.get_height() - 10, finish_button.get_width() + 10,
                                 finish_button.get_height() + 5), 2)


def winning_screen(status):
    global player1, player2, player1ready, player2ready, player2_score, player1_score, player1_turn, player2_turn

    current_player = None

    if player1_turn:
        if status == "wins":
            player2_score += 5
        current_player = player2
    elif player2_turn:
        if status == "wins":
            player1_score += 5
        current_player = player1

    # Game is single player
    if (player1ready == 0) and (player2ready == 0):
        menu.main_menu()

    else:
        while True:
            win.fill((255, 255, 255))

            # Display who won
            result_text = HEADING_FONT.render(current_player + " " + status, 1, BLACK)
            win.blit(result_text, (50, 10))

            # Display scores
            score1 = HEADING_FONT.render(player1 + ": " + str(player1_score) + " points", 1, BLACK)
            score2 = HEADING_FONT.render(player2 + ": " + str(player2_score) + " points", 1, BLACK)

            win.blit(score1, (50, 100))
            win.blit(score2, (50, 150))

            # Put continue or finish buttons
            buttons()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()

                    if (761 < m_x < 761 + 234) and (441 < m_y < 441 + 54):
                        print("conitnue?")
                        next_round()

                    elif (5 < m_x < 5 + 199) and (441 < m_y < 441 + 54):
                        print("finish?")

                        win.fill((255, 255, 255))

                        winner = None

                        if player1_score == player2_score:
                            winner_text = HEADING_FONT.render("TIE", 1, BLACK)
                        else:
                            if player1_score > player2_score:
                                winner = player1
                            elif player2_score > player1_score:
                                winner = player2

                            winner_text = HEADING_FONT.render(winner + " " + status, 1, BLACK)

                        win.blit(winner_text, (500, 250))

                        pygame.display.update()
                        pygame.time.delay(3000)
                        reset_values()

                        menu.main_menu()

                    print(m_x, m_y)


            pygame.display.update()


def check_multiplayer():
    if (player1ready == 0) and (player2ready == 0):
        return False
    else:
        return True


def next_round():

    global player1_turn, player2_turn

    if player1_turn:
        player2_turn = True
        player1_turn = False

    elif player2_turn:
        player1_turn = True
        player2_turn = False

    multiplayer()


def reset_values():

    global player1, player2, player1_score, player2_score, \
           player1_turn, player2_turn, player1ready, player2ready

    player1ready = False
    player2ready = False
    player1_turn = True
    player2_turn = False
    player1 = ""
    player2 = ""
    player1_score = 0
    player2_score = 0
