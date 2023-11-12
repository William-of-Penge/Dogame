import pygame
import random

print('game start')
#I {HBMT-GitHub} entered this myself!
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

player_pos = pygame.Vector2(screen.get_width() / 2, 
                            screen.get_height() / 2)
cat_pos = pygame.Vector2(screen.get_width() / 2, 
                         screen.get_height() / 2 + 80)




class Hound():
    CHASING_CAT = 0
    RUNNING_AWAY = 1
    STANDING = 2
    RUNNING_AROUND = 3
    CHASING_SPEED = 200
    RUNNING_AWAY_SPEED = 300
    SCARED_DISTANCE = 90

    def __init__(self):
        self.pos = pygame.Vector2(random.uniform(0, screen.get_width()), -100)
        self.mode = self.CHASING_CAT

    def update(self, dt, cat_pos, player_pos):
        me_to_player = (player_pos - self.pos)
        if me_to_player.magnitude() <= self.SCARED_DISTANCE:
            print('running away')
            self.mode = self.RUNNING_AWAY
        
        if self.mode == self.CHASING_CAT:
            me_to_cat_direction = (cat_pos - self.pos).normalize()
            self.pos = self.pos + dt * self.CHASING_SPEED * me_to_cat_direction
            return
        if self.mode == self.RUNNING_AWAY:
            me_to_player_direction = me_to_player.normalize()
            self.pos = self.pos - dt * self.RUNNING_AWAY_SPEED * me_to_player_direction


    def render(self, screen):
        pygame.draw.circle(screen, 'brown', self.pos, 40)

dt = 0

hounds = []

def release_hound():
    new_hound = Hound()
    hounds.append(new_hound)

release_hound()
while running:
    key_down = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key_down[pygame.K_ESCAPE]:
            # pygame.QUIT event means the user clicked X to close your window
            running = False

    screen.fill('darkgreen')

    # rendering...
    pygame.draw.circle(screen, 'white', player_pos, 40)
    pygame.draw.circle(screen, 'orange', cat_pos, 40)

    if random.random() < 0.005:
        print('release hound')
        release_hound()

    for hound in hounds:
        hound.render(screen)

    for hound in hounds:
        hound.update(dt, cat_pos, player_pos)

    if key_down[pygame.K_w]:
        player_pos.y = player_pos.y - 300 * dt
    if key_down[pygame.K_d]:
        player_pos.x = player_pos.x + 300 * dt
    if key_down[pygame.K_s]:
        player_pos.y = player_pos.y + 300 * dt
    if key_down[pygame.K_a]:
        player_pos.x = player_pos.x - 300 * dt

    if key_down[pygame.K_UP]:
        cat_pos.y = cat_pos.y - 300 * dt
    if key_down[pygame.K_RIGHT]:
        cat_pos.x = cat_pos.x + 300 * dt
    if key_down[pygame.K_DOWN]:
        cat_pos.y = cat_pos.y + 300 * dt
    if key_down[pygame.K_LEFT]:
        cat_pos.x = cat_pos.x - 300 * dt


    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000


