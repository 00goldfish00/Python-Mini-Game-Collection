import pygame
from pygame import mixer
import math
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENTA = (250, 0, 125)
PURPLE = (10, 0, 15)

# initialize pygame and window
pygame.init()

resX, resY = 1280, 720
screen = pygame.display.set_mode((resX, resY))
pygame.display.set_caption("space invaders")
pygame.display.set_icon(pygame.image.load("resources/aqualung.png"))

# music
# mixer.music.load("background.wav")
# mixer.music.play(-1)    # '-1' specifies to play on loop

# sound fx
laser_sound = mixer.Sound('laser.wav')
explosion_sound = mixer.Sound('explosion.wav')

# player
player_img = pygame.image.load("resources/spaceship.png")
player_x, player_y, player_shift = ((resX / 2) - 64), (resY - 74), 0

# laser
laser_img = pygame.image.load("resources/laser.png")
laser_x, laser_y, laser_shift = 0, player_y, 1
laser_state = "primed"  # "primed" - not visible, "fire" - fires bullet

# enemies
enemy_count = 7
aircraft_img = []
enemy_x = []
enemy_y = []
enemy_shift_x = []
enemy_shift_y = []

for i in range(enemy_count):
    aircraft_img.append(pygame.image.load("resources/aircraft.png"))
    enemy_x.append(random.randint(0, (resX - 64)))
    enemy_y.append(64)
    enemy_shift_x.append(0.5)
    enemy_shift_y.append(0)

# score
score_value = 0
score_x, score_y = 20, 20
score_font = pygame.font.SysFont('vgafix.fon', 32, True)

# game over
game_over_font = pygame.font.SysFont('vgafix.fon', 128, True)


def player(x, y):
    screen.blit(player_img, (x, y))


def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser_img, (x, y))
    global laser_x, laser_y
    laser_x, laser_y = x, y


def isCollide(x1, y1, x2, y2):  # laser_x, laser_y, enemy_x, enemy_y
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    if distance < 32:
        return True
    else:
        return False


def aircraft(x, y, count):
    screen.blit(aircraft_img[count], (x, y))


def showScore(x, y):
    score = score_font.render("score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOver():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, ((resX/4), (resY/3)))


running = True
while running:
    screen.fill(PURPLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit events
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # player movement and attack
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            player_shift = 0.5
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            player_shift = -0.5
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            player_shift = 0
        if keys[pygame.K_UP] and laser_state == "primed":
            laser_sound.play()
            laser_x = player_x
            laser_y = player_y
            fire_laser(laser_x, laser_y)

    player(player_x, player_y)

    # player movement
    player_x += player_shift
    if player_x < 0:
        player_x = 0
    elif player_x > (resX - 64):
        player_x = resX - 64

    # laser movement
    if laser_y <= 0:
        laser_x = player_x
        laser_y = player_y
        laser_state = "primed"
    if laser_state == "fire":
        fire_laser(laser_x, laser_y)
        laser_y -= laser_shift

    # enemy movement
    for i in range(enemy_count):

        # game over
        if enemy_y[i] > 200:
            for j in range(enemy_count):
                enemy_y[j] = resY
            gameOver()

        enemy_x[i] += enemy_shift_x[i]
        if enemy_x[i] <= 0:
            enemy_shift_x[i] *= -1
            enemy_shift_y[i] += 1
            if enemy_shift_y[i] % 2 == 0:
                enemy_y[i] += 64
        elif enemy_x[i] >= (resX - 64):
            enemy_shift_x[i] *= -1
            enemy_shift_y[i] += 1
            if enemy_shift_y[i] % 2 == 0:
                enemy_y[i] += 64

        # collision
        collision = isCollide(laser_x, laser_y, enemy_x[i], enemy_y[i])
        if collision:
            explosion_sound.play()
            laser_y = player_y
            laser_state = "primed"
            score_value += 1
            enemy_x[i], enemy_y[i], = random.randint(0, (resX - 64)), 6

        aircraft(enemy_x[i], enemy_y[i], i)

    showScore(score_x, score_y)

    pygame.display.update()


# Credits:
# Freepik at https://www.flaticon.com/authors/freepik
# Window icon
# Spaceship
# UFO
# UFO 3
# Laser
# Explosion
# Becris at https://www.flaticon.com/authors/becris
# Spacecraft
# Nhor Phai at <a href="https://www.flaticon.com/authors/nhor-phai
# Aircraft
# Good Ware at https://www.flaticon.com/authors/good-ware
# UFO 2
