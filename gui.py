import pygame
import math
import menu
import single_player_functions as func_file
import multiplayer

pygame.init()

# Setup display
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# button variable
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(65 + i), True])

# fonts
font = 'comicsans'
LETTER_FONT = pygame.font.SysFont(font, 25)
WORD_FONT = pygame.font.SysFont(font, 40)
TITLE_FONT = pygame.font.SysFont(font, 50)

# Loading images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 6
word = ""
hint = ""
guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Max FPS
FPS = 60
clock = pygame.time.Clock()
run = True


# hint function
def show_hint():
    if hint != "":
        hint_text = LETTER_FONT.render("HINT:" + hint, 1, BLACK)
        win.blit(hint_text, (225, 100))


def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width()) / 2, 10))

    # display hint
    show_hint()

    # draw word and underscored
    display_word = ""
    for letter in word:
        if letter == " ":
            display_word += "  "
        elif letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # draw hangman and update display
    win.blit(images[hangman_status], (50, 100))
    pygame.display.update()


# win or lose
def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    ans_text = LETTER_FONT.render(word, 1, BLACK)
    win.blit(text, ((WIDTH - text.get_width()) / 2, (HEIGHT - text.get_height()) / 2))

    if message == "YOU LOSE":
        win.blit(ans_text, ((WIDTH - text.get_width()) / 2 + 20, (HEIGHT - text.get_height()) / 2 + 50))

    pygame.display.update()
    pygame.time.delay(3000)


def main():
    # getting global variables
    global run, hangman_status, LETTER_FONT, WORD_FONT, TITLE_FONT
    LETTER_FONT = pygame.font.SysFont(font, 25)
    WORD_FONT = pygame.font.SysFont(font, 40)
    TITLE_FONT = pygame.font.SysFont(font, 50)

    # Game loop
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Exit game
            if event.type == pygame.QUIT:
                run = False
                menu.forced_quit()

            # check collision / button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status -= 1

            # check collision / keyboard input
            elif event.type == pygame.KEYDOWN:
                for letter in letters:
                    input_ = event.unicode

                    if input_ == letter[2].lower():
                        letter[3] = False
                        guessed.append(letter[2])
                        if letter[2] not in word:
                            hangman_status -= 1



        draw()

        # winning status
        won = True
        for letter in word:
            if letter not in guessed:
                if letter != " ":
                    won = False
                    break

        if won:
            if multiplayer.check_multiplayer():
                multiplayer.winning_screen("won")
                pygame.quit()
            else:
                display_message("YOU WIN")
                menu.main_menu()
                break

        if hangman_status == 0:
            if multiplayer.check_multiplayer():
                multiplayer.winning_screen("lose")
                pygame.quit()
            else:
                display_message("YOU LOST")
                menu.main_menu()
                break



def reset_single():
    global hangman_status, word, guessed, hint

    hangman_status = 6
    word = (func_file.word()[0]).upper()
    if len(func_file.word()) == 2:
        hint = func_file.word()[1]
    print(word)
    print(hint)
    guessed = []

    for letter in letters:
        letter[3] = "visible"
    main()


def reset_multi():
    global hangman_status, guessed, word

    hangman_status = 6
    word = multiplayer.get_word().upper()

    print(word)
    print("Executed")
    guessed = []
    for letter in letters:
        letter[3] = "visible"
    main()


def update_font(new_font):
    global font
    font = new_font

