import pygame
from game_map import board
from random import choice
Width = 560
Height = 750
h_b = (Height) // 32
w_b = Width // 27 
speed = 2
movement  = [(-1,0),(1,0), (0,-1), (0,1)]
#allow = [10,11,12,25]


class Blinky(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.image.fill((255,0,0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (Width//2, (14+0.5)*h_b) 

        self.target = pygame.Surface((5,5))
        self.target.fill((255,0,0))
        self.target_rect = self.target.get_rect()
        self.speed = speed
        self.last_dir = 0 #Prevent jitter
        self.row = self.rect.centery // h_b
        self.col = self.rect.centerx // w_b
        self.allow = [10,11,12,25]
        self.possible = []
        self.door = True
        self.chase = False
        self.eaten = False

    def check_collision(self, direction):
        row = self.rect.centery // h_b
        col = self.rect.centerx // w_b

        if direction == 0:  # left
            col -= 1
        elif direction == 1:  # right
            col += 1
        elif direction == 2:  # up
            row -= 1
        elif direction == 3:  # down
            row += 1

        if self.eaten:
            if board[row][col] == 25 and self.rect.centery // h_b == 12:
                self.eaten = False
                self.chase = False

        # Boundary check
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            tile = board[row][col]
            if tile in self.allow:
                if tile == 25 and self.rect.centery // h_b == 12:
                    self.allow.remove(25)
                    self.door = False
                
                return True
        return False

    def ghost_route(self):
        next_x, next_y = self.rect.center

        #convert pixel coordinate to row/col
        self.row = next_y // h_b
        self.col = next_x // w_b

        self.possible = []

        for i, (dx, dy) in enumerate(movement):
            if self.check_collision(i):
                self.possible.append((i, self.row+dy, self.col+dx))



    def update(self, target):
        self.target_rect.center = (target[0], target[1])
        
        self.ghost_route()

        calculation = {}
        for direction_index, r, c in self.possible:
            y = (r+0.5)*h_b
            x = (c+0.5)*w_b
            dis = int(((x - target[0])**2 + (y - target[1])**2) ** 0.5)
            calculation[direction_index] = dis

        if self.chase and not self.eaten:
            calculation = dict(reversed(sorted(calculation.items(), key=lambda item: item[1])))
        else:
            calculation = dict(sorted(calculation.items(), key=lambda item: item[1]))
        best_direction = next(iter(calculation))

        if self.last_dir in calculation and self.last_dir != best_direction:
            diff = abs(calculation[self.last_dir]-calculation[best_direction])
            if diff<=15:
                best_direction = self.last_dir

        if self.check_collision(best_direction):
            if best_direction == 0:  # left
                self.rect.x -= self.speed
                self.rect.centery = ((self.row)+0.5)*h_b
            
            elif best_direction == 1:  # right
                self.rect.centerx += self.speed
                self.rect.centery = ((self.row)+0.5)*h_b
            

            elif best_direction == 2:  # up
                    self.rect.centery -= self.speed
                    self.rect.centerx = ((self.col)+0.5)*w_b
            
            elif best_direction == 3 :  # down
                    self.rect.centery += self.speed
                    self.rect.centerx = ((self.col)+0.5)*w_b
                
            self.last_dir = best_direction
        
        #print(calculation)
        

        
class Pinky(Blinky):
    def __init__(self):
        Blinky.__init__(self)
        self.image.fill((255,184,255)) 
        self.rect.center = (Width//2, (16+0.5)*h_b) 
        self.target.fill((255,184,255)) 
    
    def cal_target(self, direction, position):
        if direction == None:
            return position
        if direction == 0:
            dx,dy = -1,0
        elif direction == 1:
            dx,dy = 1,0
        elif direction == 2:
            dx,dy = 0,-1
        elif direction == 3:
            dx,dy = 0,1
        dx = int(4.5*w_b)*dx
        dy = int(4.5*h_b)*dy
        return (position[0]+dx, position[1]+dy)

class Inky(Blinky):
    def __init__(self):
        Blinky.__init__(self)
        self.image.fill((0,255,255))
        self.rect.center = (Width//2-2*w_b, (16+0.5)*h_b) 
        self.target.fill((0,255,255))
    
    def cal_target(self, player_pos, blinky_pos):
        diff_x = blinky_pos[0] - player_pos[0]
        diff_y = blinky_pos[1] - player_pos[1]
        return (player_pos[0]-diff_x, player_pos[1]-diff_y)
    
class Clyde(Blinky):
    def __init__(self):
        Blinky.__init__(self)
        self.image.fill((255,184,82))
        self.rect.center = (Width//2+2*w_b, (16+0.5)*h_b) 
        self.target.fill((255,184,82))
        self.last_len = 0 #check for changes
        self.clyde_direction = -1
        self.last_dir = 0
    
    def wander(self):
        self.ghost_route()
        #print(self.possible)
        check = [i[0] for i in self.possible]
        if len(check)>1:
            if self.last_dir == 0 and 1 in check: #prevent turning back
                check.remove(1)
            elif self.last_dir == 1 and 0 in check:
                check.remove(0)
            elif self.last_dir == 2 and 3 in check:
                check.remove(3)
            elif self.last_dir == 3 and 2 in check:
                check.remove(2)

        #print(check)
        if self.last_len != len(self.possible) or self.clyde_direction not in check:
            self.clyde_direction = choice(check)
        #print(self.clyde_direction)
        if self.check_collision(self.clyde_direction):
            if self.clyde_direction == 0:  # left
                self.rect.x -= self.speed
                self.rect.centery = ((self.row)+0.5)*h_b
            
            elif self.clyde_direction == 1:  # right
                self.rect.centerx += self.speed
                self.rect.centery = ((self.row)+0.5)*h_b
            

            elif self.clyde_direction == 2:  # up
                    self.rect.centery -= self.speed
                    self.rect.centerx = ((self.col)+0.5)*w_b
            
            elif self.clyde_direction == 3 :  # down
                    self.rect.centery += self.speed
                    self.rect.centerx = ((self.col)+0.5)*w_b
                
        self.last_len = len(self.possible)
        self.last_dir = self.clyde_direction
        
    
