import pygame
import sys
import random

class Game:

    def __init__(self):
        self.width = 620
        self.tile = 21
        self.W_tile = self.width / self.tile
        self.Q_tile = round(self.width / self.W_tile)
        self.window = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption("Snake")

        self.time, self.time_step = 0, 100
        self.pos = [self.Q_tile // 2, self.Q_tile // 2]
        self.dir = 0
        self.lose = False
        self.points = 0
        self.eat = True
        self.body = []
        self.apple_x_pos = 0
        self.apple_y_pos = 0
        self.background_color = (25, 25, 25)
        self.block_input = False
        self.clock = pygame.time.Clock()

        self.reset_apple_position()
        self.run()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.change_direction(event.key)

    def change_direction(self, key):
        if not self.block_input:
            if key == pygame.K_RIGHT and self.dir != 3:
                self.dir = 1
            elif key == pygame.K_LEFT and self.dir != 1:
                self.dir = 3
            elif key == pygame.K_UP and self.dir != 2:
                self.dir = 0
            elif key == pygame.K_DOWN and self.dir != 0:
                self.dir = 2
            self.block_input = True

    def update(self):
        self.time_now = pygame.time.get_ticks()
        if self.time_now - self.time > self.time_step:
            self.time = self.time_now
            self.move()
            self.check_collisions()
            self.check_eat_apple()

    def move(self):
        if self.dir == 1:
            self.pos[0] += 1
        elif self.dir == 3:
            self.pos[0] -= 1
        elif self.dir == 0:
            self.pos[1] -= 1
        elif self.dir == 2:
            self.pos[1] += 1
        self.check_borders()
        self.body.insert(0, self.pos.copy())
        if len(self.body) > self.points + 1:
            self.body.pop()
        self.block_input = False

    def check_collisions(self):
        if self.pos in self.body[1:]:
            self.reset_game()

    def reset_game(self):
        self.pos = [self.Q_tile // 2, self.Q_tile // 2]
        self.dir = 0
        self.points = 0
        self.body = []
        self.eat = True
        self.time_step = 100
        self.reset_apple_position()
    
    def upgrade_speed(self):
        if not self.time_step <=20:
            self.time_step -=1

    def check_eat_apple(self):
        if self.pos == [self.apple_x_pos, self.apple_y_pos]:
            self.eat = True
            self.points += 1
            self.upgrade_speed()
            self.reset_apple_position()

    def reset_apple_position(self):
        self.apple_x_pos = random.randint(0, self.Q_tile - 1)
        self.apple_y_pos = random.randint(0, self.Q_tile - 1)
        while [self.apple_x_pos, self.apple_y_pos] in self.body:
            self.apple_x_pos = random.randint(0, self.Q_tile - 1)
            self.apple_y_pos = random.randint(0, self.Q_tile - 1)

    def check_borders(self):
        if self.pos[0] < 0:
            self.pos[0] = self.Q_tile - 1
        elif self.pos[1] < 0:
            self.pos[1] = self.Q_tile - 1
        elif self.pos[0] >= self.Q_tile:
            self.pos[0] = 0
        elif self.pos[1] >= self.Q_tile:
            self.pos[1] = 0

    def draw(self):
        self.window.fill(self.background_color)
        for pos in self.body:
            self.draw_rect(pos, (255, 255, 255))
            #self.draw_rect(pos, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.draw_rect([self.apple_x_pos, self.apple_y_pos], (255, 0, 0))
        pygame.display.set_caption(f"Snake {self.points}p")
        pygame.display.flip()

    def draw_rect(self, pos, color):
        square_x = self.W_tile * pos[0]
        square_y = self.W_tile * pos[1]
        pygame.draw.rect(self.window, color, (square_x + 2, square_y + 2, self.W_tile - 4, self.W_tile - 4))

if __name__ == "__main__":
    pygame.init()
    Game()
