import pygame
import math

pygame.init()

# Setup display
WIDTH, HEIGHT = 800, 500
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
LETTER_FONT = pygame.font.SysFont('comicsans', 25)

# Loading images
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 6

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Max FPS
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


# Game loop
while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        # Exit game
        if event.type == pygame.QUIT:
            run = False

        # check collision / button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False

pygame.quit()
