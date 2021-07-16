import pygame
import random
import math
import time
pygame.init()

win_width = 500
win_height = 500

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
fps = 8

# INITIALISING HEAD
head_x = 1
head_y = 1
head_width = win_width // 20 - 1
head_height = win_height // 20 - 1
head_vel = 25

#

up = False
down = False
left = False
right = False

#


class Body(object):

    def __init__(self, x, y, width=head_width, height=head_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(window, (0, 225, 225), (self.x + 1, self.y + 1, self.width, self.height))


#


# INITIALIZING FOOD
# INITIALIZING BODY
# INITIALIZING BODY LIST
# INITIALIZING CHECK LIST
food_x = random.randint(0, 20) * win_width // 20 + 1
food_y = random.randint(0, 20) * win_height // 20 + 1
body = Body(1000, 1000)
body_list = []
checklist = []
#


def grid():

    for gridx in range(1, 20):
        for gridy in range(1, 20):
            pygame.draw.line(window, (225, 0, 0), (gridx * win_width // 20, 0),
                             (gridx * win_width // 20, win_height))
            pygame.draw.line(window, (225, 0, 0), (0, gridy * win_height // 20),
                             (win_width, gridy * win_width // 20))


def key_mapping():
    global up, down, right, left, head_x, head_y, head_vel
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and not left:
        right = True
        left = False
        down = False
        up = False

    elif keys[pygame.K_LEFT] and not right:
        right = False
        left = True
        down = False
        up = False

    elif keys[pygame.K_UP] and not down:
        right = False
        left = False
        down = False
        up = True

    elif keys[pygame.K_DOWN] and not up:
        right = False
        left = False
        down = True
        up = False

    if right:
        head_x += head_vel
    if left:
        head_x -= head_vel
    if up:
        head_y -= head_vel
    if down:
        head_y += head_vel


while True:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break

    grid()

    key_mapping()

    head = pygame.draw.rect(window, (0, 0, 225), (head_x, head_y, head_width, head_height))

    if math.hypot(head_x - food_x, head_y - food_y) == 0:
        print('hit')
        body_list.append(Body(1000, 1000))
        food_x = random.randint(1, 19) * win_width // 20 + 1
        food_y = random.randint(1, 19) * win_height // 20 + 1
        print(body_list)
        checklist = body_list[:]
        checklist.pop(0)
        print(checklist)

    food = pygame.draw.rect(window, (0, 225, 0), (food_x, food_y, head_height, head_height))

    #

    for index in range(len(body_list) - 1, 0, -1):
        body_list[index].x, body_list[index].y = body_list[index - 1].x, body_list[index - 1].y
        body_list[index].draw()

    #

    if len(body_list) > 0:
        body_list[0].x, body_list[0].y = head_x, head_y
        body_list[0].draw()

        for part in checklist:
            if math.hypot(body_list[0].x - part.x, body_list[0].y - part.y) == 0:
                time.sleep(1)
                body_list.clear()
                checklist.clear()
                head_x = 1
                head_y = 1
                right = False
                left = False
                down = False
                up = False
    #
    if head_x >= 525 or head_x < 0 or head_y < 0 or head_y >= 525:
        time.sleep(1)
        body_list.clear()
        checklist.clear()
        head_x = 1
        head_y = 1
        right = False
        left = False
        down = False
        up = False

    pygame.display.update()
    window.fill((0, 0, 0))
