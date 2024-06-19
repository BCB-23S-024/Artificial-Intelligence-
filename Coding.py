import pygame
import time
import random

# Initialize pygame
pygame.init()

# Constants
snake_speed = 15
window_x = 720
window_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake default position
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Default direction
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Fonts
font = pygame.font.SysFont('times new roman', 35)
small_font = pygame.font.SysFont('times new roman', 25)

# Display score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    main_menu()

# Main menu
def main_menu():
    while True:
        game_window.fill(black)
        main_menu_text = font.render("Main Menu", True, white)
        start_text = small_font.render("Start Game", True, white)
        replay_text = small_font.render("Replay Game", True, white)
        options_text = small_font.render("Options", True, white)
        quit_text = small_font.render("Quit", True, white)

        game_window.blit(main_menu_text, (window_x / 2 - main_menu_text.get_width() / 2, window_y / 4))
        game_window.blit(start_text, (window_x / 2 - start_text.get_width() / 2, window_y / 2))
        game_window.blit(replay_text, (window_x / 2 - replay_text.get_width() / 2, window_y / 2 + 50))
        game_window.blit(options_text, (window_x / 2 - options_text.get_width() / 2, window_y / 2 + 100))
        game_window.blit(quit_text, (window_x / 2 - quit_text.get_width() / 2, window_y / 2 + 150))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if window_x / 2 - start_text.get_width() / 2 <= mouse_pos[0] <= window_x / 2 + start_text.get_width() / 2:
                    if window_y / 2 <= mouse_pos[1] <= window_y / 2 + start_text.get_height():
                        game_loop()
                    if window_y / 2 + 50 <= mouse_pos[1] <= window_y / 2 + 50 + replay_text.get_height():
                        game_loop()
                    if window_y / 2 + 100 <= mouse_pos[1] <= window_y / 2 + 100 + options_text.get_height():
                        options_menu()
                    if window_y / 2 + 150 <= mouse_pos[1] <= window_y / 2 + 150 + quit_text.get_height():
                        pygame.quit()
                        quit()

# Options menu
def options_menu():
    while True:
        game_window.fill(black)
        options_menu_text = font.render("Options", True, white)
        back_text = small_font.render("Back to Menu", True, white)

        game_window.blit(options_menu_text, (window_x / 2 - options_menu_text.get_width() / 2, window_y / 4))
        game_window.blit(back_text, (window_x / 2 - back_text.get_width() / 2, window_y / 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if window_x / 2 - back_text.get_width() / 2 <= mouse_pos[0] <= window_x / 2 + back_text.get_width() / 2:
                    if window_y / 2 <= mouse_pos[1] <= window_y / 2 + back_text.get_height():
                        main_menu()

# Game loop
def game_loop():
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score

    # Reinitialize variables
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        fps.tick(snake_speed)

main_menu()