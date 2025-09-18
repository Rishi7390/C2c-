import pygame
import math

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Skeleton Avatar with Images")
clock = pygame.time.Clock()

# Load avatar images
head_img = pygame.image.load("avatar_head.png")
head_img = pygame.transform.scale(head_img, (50, 50))

body_img = pygame.image.load("avatar_body.png")
body_img = pygame.transform.scale(body_img, (40, 80))

arm_img = pygame.image.load("avatar_arm.png")
arm_img = pygame.transform.scale(arm_img, (10, 60))

leg_img = pygame.image.load("avatar_leg.png")
leg_img = pygame.transform.scale(leg_img, (10, 70))

# Avatar positions
center_x, center_y = 400, 300

# Rotation angles
angles = {"head": 0, "right_arm": 0, "left_arm": 0, "right_leg": 0, "left_leg": 0}

# Function to rotate image around its center
def blit_rotate_center(surf, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: angles["right_arm"] += 2
    if keys[pygame.K_s]: angles["right_arm"] -= 2
    if keys[pygame.K_a]: angles["left_arm"] += 2
    if keys[pygame.K_d]: angles["left_arm"] -= 2
    if keys[pygame.K_UP]: angles["head"] += 2
    if keys[pygame.K_DOWN]: angles["head"] -= 2

    # Draw legs
    blit_rotate_center(screen, leg_img, (center_x + 15, center_y + 80), angles["right_leg"])
    blit_rotate_center(screen, leg_img, (center_x - 25, center_y + 80), angles["left_leg"])

    # Draw arms
    blit_rotate_center(screen, arm_img, (center_x + 25, center_y + 40), angles["right_arm"])
    blit_rotate_center(screen, pygame.transform.flip(arm_img, True, False), (center_x - 35, center_y + 40), angles["left_arm"])

    # Draw body
    screen.blit(body_img, (center_x - 20, center_y))

    # Draw head
    blit_rotate_center(screen, head_img, (center_x - 25, center_y - 50), angles["head"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
