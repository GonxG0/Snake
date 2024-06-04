import pygame
import sys
import os
import random



class Game():

    def __init__(self):

        self.width, self.height = 620, 620
        self.tile = 20

        self.W_tile = self.width / 20
        self.Q_tile = round(self.width / self.W_tile)
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")

        self.time, self.time_step = 0, 50
        self.pos = [round(self.Q_tile/2),round(self.Q_tile/2)]
        self.dir = 0
        self.lose = False
        self.points = 0
        self.eat = True
        self.body = []

        self.apple_x_pos = 0
        self.apple_y_pos = 0

        self.background_color = (25, 25, 25)

        self.clock = pygame.time.Clock()
        self.step()
    
    
    def step(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.dir !=3:
                        self.dir = 1
                    elif event.key == pygame.K_LEFT  and self.dir !=1:
                        self.dir = 3
                    elif event.key == pygame.K_UP  and self.dir !=2:
                        self.dir = 0
                    elif event.key == pygame.K_DOWN  and self.dir !=0:
                        self.dir = 2
            
            self.time_now = pygame.time.get_ticks()
            if self.time_now - self.time > self.time_step and 1==2:
                self.time = self.time_now

                if self.dir == 1:   #Right
                    self.pos[0] +=1
                elif self.dir == 3: #Left
                    self.pos[0] -=1
                elif self.dir == 0: #Up
                    self.pos[1] -=1
                elif self.dir == 2: #Down
                    self.pos[1] +=1

                self.check_borders()
                self.body.insert(0,self.pos.copy())
                if len(self.body) > self.points+1:
                    self.body.pop()
                print(self.body)
            

            if self.pos[0] == self.apple_x_pos and self.pos[1] == self.apple_y_pos:

                self.eat = True
                self.points +=1
                print(self.points)

            

            self.clock.tick(60)
            self.draw()

    def check_borders(self):
        if self.pos[0] < 0:
            self.pos[0] = self.Q_tile-1
        elif self.pos[1] < 0:
            self.pos[1] = self.Q_tile-1
        elif self.pos[0] > self.Q_tile-1:
            self.pos[0] = 0
        elif self.pos[1] > self.Q_tile-1:
            self.pos[1] = 0

    def draw(self):
        self.window.fill(self.background_color)


        for pos in self.body:
            color = (255,255,255)
            sqare_x = self.W_tile*pos[0]
            sqare_y = self.W_tile*pos[1]

            pygame.draw.rect(self.window, color, (sqare_x+2, sqare_y+2, self.W_tile-4, self.W_tile-4))


        if self.eat == True:

            self.apple_x_pos = random.randint(0,self.Q_tile-1)
            self.apple_y_pos = random.randint(0,self.Q_tile-1)

            self.apple_x = self.W_tile*self.apple_x_pos
            self.apple_y = self.W_tile*self.apple_y_pos
            self.eat = False
        color = (255,0,0)
        pygame.draw.rect(self.window, color, (self.apple_x+2, self.apple_y+2, self.W_tile-4, self.W_tile-4))

        pygame.display.set_caption(f"Snake {self.points}p")
        pygame.display.flip()


Game()


#Colision con el cuerpo
#Que la manzana no pueda spawnear encima del cuerpo
# y si queres que se reinicie el juego cuando perdes
