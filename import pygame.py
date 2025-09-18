import pygame
import math
import time

# Initialize PyGame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Anime Girl Dance")
clock = pygame.time.Clock()

# Load anime girl image
anime_img = pygame.image.load("anime_girl.png")  # single character image
anime_img = pygame.transform.scale(anime_img, (150, 300))  # scale to fit screen

# Load horror sound (optional)
try:
    horror_sound = pygame.mixer.Sound("animegirl.mp3")
    horror_sound.set_volume(0.5)
    horror_sound.play(-1)
except:
    print("Horror sound not found!")

# Center position
center_x, center_y = 400, 300

# Function to rotate image around its center
def blit_rotate_center(surf, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated_image, new_rect.topleft)

# Time for movement simulation
start_time = time.time()
running = True

while running:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = time.time() - start_time

    # Simulate simple dance by slightly rotating the whole character
    angle = math.sin(t * 2) * 10  # small rocking motion

    blit_rotate_center(screen, anime_img, (center_x - 75, center_y - 150), angle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
