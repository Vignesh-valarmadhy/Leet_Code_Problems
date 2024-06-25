import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height
player_speed = 10

# Falling object settings
object_width = 30
object_height = 30
object_speed = 7
object_list = []

# Score
score = 0

# Font for displaying the score
font = pygame.font.SysFont(None, 35)

def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

def draw_object(x, y):
    pygame.draw.rect(screen, red, [x, y, object_width, object_height])

def display_score(score):
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, [10, 10])

def game_loop():
    global player_x, player_y, score
    game_exit = False

    # Main game loop
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Boundary conditions
        if player_x < 0:
            player_x = 0
        if player_x > screen_width - player_width:
            player_x = screen_width - player_width

        # Update objects
        if random.randint(1, 20) == 1:  # Randomly create a new object
            obj_x = random.randint(0, screen_width - object_width)
            obj_y = -object_height
            object_list.append([obj_x, obj_y])

        for obj in object_list:
            obj[1] += object_speed

        # Check for collision
        for obj in object_list:
            if (player_y < obj[1] + object_height and
                player_y + player_height > obj[1] and
                player_x < obj[0] + object_width and
                player_x + player_width > obj[0]):
                score += 1
                object_list.remove(obj)

        # Remove objects that fall off the screen
        object_list[:] = [obj for obj in object_list if obj[1] < screen_height]

        # Drawing everything
        screen.fill(black)
        draw_player(player_x, player_y)
        for obj in object_list:
            draw_object(obj[0], obj[1])
        display_score(score)
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate
        clock.tick(30)

    pygame.quit()
    quit()

# Start the game
game_loop()
