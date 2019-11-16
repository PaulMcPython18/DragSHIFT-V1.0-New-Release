import pygame
import math
import random

player_vehicle = pygame.image.load("rally.png")
camper = pygame.image.load("camper.png")
carimg = pygame.image.load("car.png")
treeimg = pygame.image.load("Pine Trees/Tree - Pine 00.png")
start_screen = True


class player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def draw(self):
        win.blit(player_vehicle, (self.x, self.y))
class tree:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def draw(self):
        win.blit(treeimg, (self.x, self.y))
class car:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def draw(self):
        win.blit(carimg, (self.x, self.y))
car1 = car(115, 300, 9.5)
player = player(50, 320, 10)
tree = tree(300, 25, 6)
ranspeed = [1, 1 , 1, 2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.8, 0.6, 0.58, 0.58, 0.18]
car_ranspeed = [0.2, 0.2 , 0.2, 3, 3, 3, 5, 4, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0.18, 0.43, 0.98, 0.68, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90]

pygame.init()
win = pygame.display.set_mode((700, 500))




run = True

while run:
    win.fill((183, 197, 191))
    keypress = pygame.key.get_pressed()
    tree.x-=tree.speed
    if tree.x <= -250:
        tree.x = 750
    if random.randint(0,3) == 1:
        car1.x += ranspeed[random.randint(0,16)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tree.speed += 0.2
                player.x += car_ranspeed[random.randint(0,32)]
    # pygame.draw.rect(win, (183, 70, 0), (0, 360, 900, 250))
    speed = int(tree.speed)
    # speed_label = pygame.font.SysFont('freesansbold.tff', 25).render("Speed: " + str(speed) + " MPH", 1, (0, 0, 0))
    # win.blit(speed_label, (5, 5))
    done = False
    done2 = False
    already_win = False
    verified_dist = 660
    speed_label = pygame.font.SysFont('freesansbold.tff', 25).render("You Lost!", 1, (255, 0, 0))
    winner = pygame.font.SysFont('freesansbold.tff', 25).render("You Won!", 1, (255, 0, 0))
    if car1.x >= verified_dist or done == True:
        if already_win == False:
            win.blit(speed_label, (5, 5))
            done = True
            already_win = True
    if player.x >= verified_dist or done2 == True:
        if already_win == False:
            win.blit(winner, (5, 5))
            done2 = True
            already_win = True
    true_spd = pygame.font.SysFont('freesansbold.tff', 25).render("Press Spacebar | Ingame Speed: " + str(speed), 1, (255, 0, 0))
    win.blit(true_spd, (405, 5))
    done = True
    already_win = True
    pygame.draw.rect(win, (40, 70, 0), (0, 360, 900, 250))
    pygame.draw.rect(win, (70, 70, 70), (0, 370, 900, 250))
    tree.draw()
    car1.draw()
    player.draw()
    pygame.display.update()
pygame.quit()
