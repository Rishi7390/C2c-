import pygame
import math
import random
import time

# Initialize PyGame
pygame.init()
pygame.mixer.init()  # Initialize sound
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Horror Skeleton Dance")
clock = pygame.time.Clock()

# Load avatar images
head_img = pygame.image.load("skeleton_head.png")
head_img = pygame.transform.scale(head_img, (50, 50))

body_img = pygame.image.load("skeleton_body.png")
body_img = pygame.transform.scale(body_img, (40, 80))

arm_img = pygame.image.load("avatar_head.png")
arm_img = pygame.transform.scale(arm_img, (10, 60))

leg_img = pygame.image.load("skeleton_leg.png")
leg_img = pygame.transform.scale(leg_img, (10, 70))

# Load horror sound
horror_sound = pygame.mixer.Sound("horror_sound.mp3")
horror_sound.set_volume(0.5)  # Adjust volume (0.0 to 1.0)
horror_sound.play(-1)  # Loop indefinitely

# Avatar positions
center_x, center_y = 400, 300

# Rotation angles
angles = {"head": 0, "right_arm": 0, "left_arm": 0, "right_leg": 0, "left_leg": 0}

# Function to rotate image around its center
def blit_rotate_center(surf, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated_image, new_rect.topleft)

# Start time for dancing animation
start_time = time.time()

running = True
while running:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Horror dance movements
    t = time.time() - start_time
    angles["right_arm"] = math.sin(t * random.uniform(5,10)) * random.randint(30, 60)
    angles["left_arm"] = math.sin(t * random.uniform(5,10) + math.pi) * random.randint(30, 60)
    angles["right_leg"] = math.sin(t * random.uniform(3,7)) * random.randint(20, 40)
    angles["left_leg"] = -math.sin(t * random.uniform(3,7)) * random.randint(20, 40)
    angles["head"] = math.sin(t * random.uniform(2,5)) * random.randint(5, 20)

    # Draw legs
    blit_rotate_center(screen, leg_img, (center_x + 15, center_y + 80), angles["right_leg"])
    blit_rotate_center(screen, leg_img, (center_x - 25, center_y + 80), angles["left_leg"])

    # Draw arms
    blit_rotate_center(screen, arm_img, (center_x + 25, center_y + 40), angles["right_arm"])
    blit_rotate_center(screen, pygame.transform.flip(arm_img, True, False), (center_x - 35, center_y + 40), angles["left_arm"])

    # Draw body
    screen.blit(body_img, (center_x - 20, center_y))

    # Draw head (skeleton head)
    blit_rotate_center(screen, head_img, (center_x - 25, center_y - 50), angles["head"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
