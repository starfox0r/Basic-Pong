import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Set the speed of the paddles
PADDLE_SPEED = 5

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Pong")

# Set up the paddles
paddle_a = pygame.Rect(50, SCREEN_HEIGHT // 2 - 50, 10, 100)
paddle_b = pygame.Rect(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - 50, 10, 100)

# Set up the ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT // 2 - 10, 20, 20)
ball_speed_x = 3
ball_speed_y = 3

# Set up the score
score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_s]:
        paddle_a.move_ip(0, PADDLE_SPEED)
    if keys[pygame.K_UP]:
        paddle_b.move_ip(0, -PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        paddle_b.move_ip(0, PADDLE_SPEED)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Check for collisions with walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0:
        score_b += 1
        ball_speed_x = 3
        ball_speed_y = 3
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    if ball.right >= SCREEN_WIDTH:
        score_a += 1
        ball_speed_x = -3
        ball_speed_y = -3
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Check for collisions with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x = -ball_speed_x

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_text = font.render(str(score_a) + " - " + str(score_b), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
