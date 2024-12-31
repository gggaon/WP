import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

pygame.font.init()
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beneath the Surface")

STATE_LOBBY = "lobby"
STATE_STAGE = "stage"
STATE_LOADING = "loading"
STATE_1 = "1"
STATE_END = "end"
current_state = STATE_LOBBY

def draw_lobby_screen():
    screen.fill(WHITE)
    title = FONT.render("Beneath the Surface", True, BLACK)
    start_button = FONT.render("Game Start", True, BLACK)
    exit_button = FONT.render("Exit", True, BLACK)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(start_button, (WIDTH // 2 - start_button.get_width() // 2, HEIGHT // 2))
    screen.blit(exit_button, (WIDTH // 2 - exit_button.get_width() // 2, HEIGHT // 2 + 50))

def draw_loading_screen():
    screen.fill(GRAY)
    text = FONT.render("Entering...", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

def main():
    global current_state

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if current_state == STATE_LOBBY:
                    if event.key == pygame.K_RETURN:
                        current_state = STATE_LOADING
                    elif event.key == pygame.K_ESCAPE:
                        running = False

        if current_state == STATE_LOBBY:
            draw_lobby_screen()
        elif current_state == STATE_LOADING:
            draw_loading_screen()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()