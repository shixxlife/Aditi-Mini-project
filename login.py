import pygame
from subprocess import call


pygame.init()
FONT = pygame.font.Font(None, 42)


def main():
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    password = ''

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if password == "password":
                        pygame.quit()
                        call(["python", "gui.py"])
                    print(password)  # I just print it to see if it works.
                    password = ''
                else:  # Add the character to the password string.
                    password += event.unicode

        screen.fill((30, 30, 30))
        # Render the asterisks and blit them.
        password_surface = FONT.render('*'*len(password), True, (70, 200, 150))
        screen.blit(password_surface, (30, 30))

        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    