import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

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

lobby_background = pygame.image.load("lobby.png")
lobby_background = pygame.transform.scale(lobby_background, (WIDTH, HEIGHT))

start_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)
exit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50 - 20, 200, 40)

def draw_lobby_screen():
    screen.blit(lobby_background, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    start_button_color = DARK_GRAY if start_button_rect.collidepoint(mouse_pos) else WHITE
    exit_button_color = DARK_GRAY if exit_button_rect.collidepoint(mouse_pos) else WHITE

    pygame.draw.rect(screen, start_button_color, start_button_rect)
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)

    start_button = FONT.render("Game Start", True, BLACK)
    exit_button = FONT.render("Exit", True, BLACK)

    screen.blit(start_button, (start_button_rect.centerx - start_button.get_width() // 2, start_button_rect.centery - start_button.get_height() // 2))
    screen.blit(exit_button, (exit_button_rect.centerx - exit_button.get_width() // 2, exit_button_rect.centery - exit_button.get_height() // 2))

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_state == STATE_LOBBY:
                    if start_button_rect.collidepoint(event.pos):
                        current_state = STATE_LOADING
                    elif exit_button_rect.collidepoint(event.pos):
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