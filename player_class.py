import pygame
from game_map import board
import time

Width = 560
Height = 750
h_b = Height// 32
w_b = Width// 27
clock = pygame.time.Clock() 


#print(dot)

ANIMATION = [pygame.image.load('photo/pacman/animation/0.png'),
         pygame.image.load('photo/pacman/animation/1.png'),
          pygame.image.load('photo/pacman/animation/2.png'),
         pygame.image.load('photo/pacman/animation/3.png'),
         pygame.image.load('photo/pacman/animation/4.png'),
         pygame.image.load('photo/pacman/animation/5.png'),
         pygame.image.load('photo/pacman/animation/6.png'),
         pygame.image.load('photo/pacman/animation/7.png')]

for idx,img in enumerate(ANIMATION):
        ANIMATION[idx] = pygame.transform.scale(img, (30, 30))

class Player (pygame.sprite.Sprite):
    def count_dot(self, board):
        self.dot = sum([i.count(11) for i in board]) + 4


    def get_dot(self):
        return self.dot
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (Width//2, (24+0.5)*h_b)
        self.speed = 3
        self.bigdot = False
        self.start = 0  #record time when pac-man eats the big dot
        self.lives = 3

        self.row = self.rect.centery//h_b
        self.col = self.rect.centerx//w_b

    def check_collision(self, direction, board):
        # Check the player's next position to see if it will collide with a wall
        next_x, next_y = self.rect.center

        # Now check if the next position is a wall (assuming walls are represented by a specific value in the board array)
        cur_row = next_y // h_b
        cur_col = next_x // w_b

        if direction == 1:  # Right
            cur_col+=1
            if cur_col>=28:
                cur_col=27
        elif direction == 0:  # Left
            cur_col-=1
            if cur_col<0:
                cur_col=0
        elif direction == 2:  # Up
            cur_row-=1
            if cur_row<0:
                cur_row=0
        elif direction == 3:  # Down
            cur_row+=1
            if cur_row>=32:
                cur_row = 31
        
        if board[cur_row][cur_col] in [10,11,12]: 
            if board[cur_row][cur_col] == 11:
                board[cur_row][cur_col] = 10
                self.dot-=1
            elif board[cur_row][cur_col] == 12:
                board[cur_row][cur_col] = 10
                self.dot-=1
                self.bigdot = True
                self.start = time.time()
            self.row = cur_row
            self.col = cur_col
            return True
        
        if direction == 0:
            cur_col+=1
        elif direction == 1:
            cur_col-=1
        elif direction == 2:
            cur_row+=1
        elif direction == 3:
            cur_row-=1
        self.row = cur_row
        self.col = cur_col
        self.rect.centery = ((self.row)+0.5)*h_b
        self.rect.centerx = ((self.col)+0.5)*w_b
        return False
    
    
    def update(self,direction):
        if direction==1:
            if self.rect.right<Width:
                self.rect.centerx += self.speed
            else:
                self.rect.right = 0
            self.rect.centery = (self.row+0.5)*h_b

        elif direction==0:
            if self.rect.x>0:
                self.rect.centerx -= self.speed
            else:
                self.rect.x = Width
            self.rect.centery = (self.row+0.5)*h_b

        elif direction==2:
            if self.rect.y>0:
                self.rect.centery -= self.speed
            self.rect.centerx = (self.col+0.5)*w_b
            
        elif direction==3:
            if self.rect.bottom<=Height:
                self.rect.centery += self.speed
            self.rect.centerx = (self.col+0.5)*w_b
    
    def death(self,screen, db, line_color, board): #play death animation and lives-=1
        for frame in ANIMATION:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.fill((0, 0, 0))  
            screen.blit(frame, self.rect)  
            db(screen, line_color, h_b, w_b, board)
            pygame.display.flip()
            clock.tick(4)  # 0.25 sec per frame

        self.lives -= 1
        #print(self.lives)

        
        
