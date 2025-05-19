import pygame 
import time
import copy
from game_map import board
from draw_board import db
import player_class
import ghost_class


# ------pygame initiation------

FPS = 60
Background = (0,0,0)
line_color = (0,0,220) 
Width = 560
Height = 750
h_b = (Height) // 32
w_b = Width // 27 
original_borad =  copy.deepcopy(board)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((Width, Height+50)) #set the screen
screen.fill(Background) #set the color 
pygame.display.set_caption("Pac-Man") #title
clock = pygame.time.Clock() 


PACMAN = [[pygame.image.load(f'photo/pacman/{i}.png') for i in (0,1,0,2)] for _ in range(4)]
BLINKY = [pygame.image.load(f'photo/ghost/blinky/{i}.png') for i in range(4)]
PINKY = [pygame.image.load(f'photo/ghost/pinky/{i}.png') for i in range(4)]
INKY = [pygame.image.load(f'photo/ghost/inky/{i}.png') for i in range(4)]
CLYDE = [pygame.image.load(f'photo/ghost/clyde/{i}.png') for i in range(4)]
EATEN = [pygame.image.load(f'photo/ghost/eaten/{i}.png') for i in range(4)]
WARNNING = [pygame.image.load(f'photo/ghost/{i}.png') for i in ("chase", "warning")]

          
for i in [BLINKY,PINKY,INKY,CLYDE,WARNNING, EATEN]:
    for idx,img in enumerate(i):
        i[idx] = pygame.transform.scale(img, (30, 30))

for g,i in enumerate(PACMAN):
    for idx,img in enumerate(i):
        if g==0:
            i[idx] = pygame.transform.rotate(img, 180)
        elif g==2:
            i[idx] = pygame.transform.rotate(img, 90)
        elif g==3:
            i[idx] = pygame.transform.rotate(img, 270)
        i[idx] = pygame.transform.scale(i[idx], (30, 30))


icon = pygame.image.load('photo/icon.png')
pygame.display.set_icon(icon)


# ------game variable & object setup------
original_board = copy.deepcopy(board)

player = player_class.Player()
direction = None
pac_img = PACMAN[1]
pac_frame = 0
final = 0 #record the end time
last_frame_change = time.time()
player.count_dot(original_board)

blinky = ghost_class.Blinky()
pinky = ghost_class.Pinky()
inky = ghost_class.Inky()
clyde = ghost_class.Clyde()
ghost_frame = 0
last_frame_change_ghost = time.time()


font = font = pygame.font.Font('Grand9k Pixel.ttf', 20)
text_dot = font.render(f"Remaining: {player.get_dot()}", True, (255, 255, 255))  # white color
text_rect_dot = text_dot.get_rect(center=(Width-100, Height))
text_time = font.render(f"Time: {0} seconds", True, (255, 255, 255))  # white color
text_rect_time = text_time.get_rect(center=(Width-95, Height+25))
text_result = font.render(f"", True, (255, 0, 0))  # red color
text_rect_result = text_result.get_rect(center=(Width//2-45, int((12+0.5) * h_b)))
text_restart = font.render(f"Press R to Restart", True, (255, 255, 255))  # white color
text_rect_restart = text_restart.get_rect(center=(Width//2, int((18+0.5) * h_b)))

lives_rect = pygame.Rect(0, Height-12.5, 30, 30)

# ------main game------
running = True
start  = time.time()
while running: 
    clock.tick(FPS)

    # ------keyboard input-----
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  #if user press quit, close the window
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: #0:left, 1:right, 2:up, 3:down
                if player.check_collision(0,board):
                    direction = 0
                    pac_img = PACMAN[0]
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if player.check_collision(1,board):
                    direction = 1
                    pac_img = PACMAN[1]
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if player.check_collision(2, board):
                    direction = 2
                    pac_img = PACMAN[2]
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if player.check_collision(3, board):
                    direction = 3
                    pac_img = PACMAN[3]
            elif event.key == pygame.K_ESCAPE:   #quit button
                running = False
            elif event.key == pygame.K_r:  #reset button
                board = copy.deepcopy(original_board)
                start  = time.time()

                player = player_class.Player()
                direction = None
                pac_img = PACMAN[1]
                pac_frame = 0
                final = 0 #record the end time
                last_frame_change = time.time()
                player.count_dot(board)

                blinky = ghost_class.Blinky()
                pinky = ghost_class.Pinky()
                inky = ghost_class.Inky()
                clyde = ghost_class.Clyde()
                ghost_frame = 0
                last_frame_change_ghost = time.time()

    # ------game ending setup-----           
    if not player.get_dot():
       if final==0:
           final = time.time()
       screen.fill(Background)
       db(screen, line_color, h_b, w_b, board)
       player.rect.center = (Width//2, (24+0.5)*h_b)
       screen.blit(PACMAN[1][0], player.rect)
       text_time = font.render(f"Time: {round(final-start)} seconds", True, (255, 255, 255))  # white color
       text_dot = font.render(f"Remaining: {player.get_dot()}", True, (255, 255, 255))  # white color
       text_result = font.render(f"YOU WIN", True, (0, 255, 0))  # green color
       screen.blit(text_dot, text_rect_dot)
       screen.blit(text_time, text_rect_time)
       screen.blit(text_result, text_rect_result)
       screen.blit(text_restart, text_rect_restart)
       pygame.display.update()
       continue

    if not player.lives:
       if final==0:
           final = time.time()
           for i in range(32):
               board[i] = [10 if j==11 or j==12 else j for j in board[i]]
       screen.fill(Background)
       
       db(screen, line_color, h_b, w_b, board)
       text_time = font.render(f"Time: {round(final-start)} seconds", True, (255, 255, 255))  # white color
       text_dot = font.render(f"Remaining: {player.get_dot()}", True, (255, 255, 255))  # white color
       text_rect_result = text_time.get_rect(center=(Width//2+25, int((12+0.5) * h_b)))
       text_result = font.render(f"GAME OVER", True, (255, 0, 0))  # green color
       screen.blit(text_dot, text_rect_dot)
       screen.blit(text_time, text_rect_time)
       screen.blit(text_result, text_rect_result)
       screen.blit(text_restart, text_rect_restart)
       pygame.display.update()
       continue

    screen.fill(Background)
    db(screen, line_color, h_b, w_b, board)

    if not player.check_collision(direction, board):
        direction = None
    player.update(direction)
    if time.time()-last_frame_change>0.125:
        pac_frame+=1
        if pac_frame>=4:
            pac_frame = 0
        last_frame_change = time.time()
    screen.blit(pac_img[pac_frame], player.rect)

    '''
    if player.bigdot:
        blinky.image.fill((33,33,222))
        pinky.image.fill((33,33,222))
        inky.image.fill((33,33,222))
        clyde.image.fill((33,33,222))
    elif not player.bigdot:
        blinky.image.fill((255,0,0))
        pinky.image.fill((255,184,255))
        inky.image.fill((0,255,255))
        clyde.image.fill((255,184,82))
    '''
    if player.bigdot:
        blinky.chase = pinky.chase = inky.chase = clyde.chase = True
        ghost_frame = 0
        player.bigdot = False
    
    if time.time()-player.start >=10: #if 10 sec passed, ghost became unchased
        blinky.chase = pinky.chase = inky.chase = clyde.chase = False

    #player and ghost collision
    for ghost in [blinky,pinky,inky,clyde]:
        if ghost.rect.colliderect(player.rect):
            if ghost.chase:
                ghost.eaten = True
            elif not ghost.eaten:
                player.death(screen, db, line_color, board)
                player.rect.center = (Width//2, (24+0.5)*h_b)
                player.bigdot = False
                direction = None
                pac_img = PACMAN[1]
                blinky.rect.center = (Width//2, (14+0.5)*h_b) 
                pinky.rect.center = (Width//2, (16+0.5)*h_b) 
                inky.rect.center = (Width//2-2*w_b, (16+0.5)*h_b) 
                clyde.rect.center = (Width//2+2*w_b, (16+0.5)*h_b) 
                blinky.allow, pinky.allow, inky.allow, clyde.allow = [10,11,12,25], [10,11,12,25],[10,11,12,25],[10,11,12,25]
                blinky.door = pinky.door = inky.door =  clyde.door =True
                blinky.chase = pinky.chase = inky.chase = clyde.chase = False
                blinky.eaten = pinky.eaten = inky.eaten = clyde.eaten = False
                continue


    #blinky movement
    if blinky.door:
        blinky.update((Width // 2, int((11+0.5) * h_b)),blinky.chase)
    elif blinky.eaten:
        blinky.update((Width // 2, int((14+0.5) * h_b)),blinky.chase)
    else:
        blinky.update(player.rect.center,blinky.chase)
    
    #pinky movement
    pinky_target = pinky.cal_target(direction, player.rect.center)
    pinky_dist_target = int(((pinky_target[0]-pinky.rect.centerx)**2+(pinky_target[1]-pinky.rect.centery)**2)**0.5)
    #print(pinky_dist_target)
    if pinky.door:
        pinky.update((Width // 2, int((11+0.5) * h_b)),pinky.chase)
    elif pinky.eaten:
        pinky.update((Width // 2, int((11+0.5) * h_b)),pinky.chase)
    elif pinky_dist_target<=int(4.5*w_b):
        pinky.update(player.rect.center, pinky.chase)
    else:
        pinky.update(pinky_target, pinky.chase)

    #inky movement
    inky_target = inky.cal_target((player.rect.centerx+12.5,player.rect.centery+12.5) , blinky.rect.center)
    inky_dist_target = int(((inky_target[0]-inky.rect.centerx)**2+(inky_target[1]-inky.rect.centery)**2)**0.5)
    if inky.door:
        inky.update((Width // 2, int((11+0.5) * h_b)), inky.chase)
    elif inky.eaten:
        inky.update((Width // 2, int((11+0.5) * h_b)), inky.chase)
    elif inky_dist_target<=100:
        inky.update(player.rect.center, inky.chase)
    else:
        inky.update(inky_target, inky.chase)

    #clyde movement
    clyde_space = int(((clyde.rect.centerx - player.rect.centerx)**2 +(clyde.rect.centery - player.rect.centery)**2)**0.5)
    if clyde.door:
        clyde.update((Width // 2, int((11+0.5) * h_b)), clyde.chase)
        #pygame.draw.circle(screen, (255,184,82),clyde.target_rect.center, 5) #draw clyde's target point
    elif clyde.eaten:
        clyde.update((Width // 2, int((14+0.5) * h_b)), clyde.chase)
    elif clyde_space <= 6*w_b:
        clyde.update(player.rect.center, clyde.chase)
        #pygame.draw.circle(screen, (255,184,82),clyde.target_rect.center, 5) #draw clyde's target point
    else:
        clyde.wander()

    
    
    for ghost in [(BLINKY, blinky), (PINKY, pinky), (INKY, inky),(CLYDE, clyde)]:
        if not ghost[1].chase:
            ghost[1].eaten =  False
            screen.blit(ghost[0][ghost[1].last_dir], ghost[1].rect)
        else:
            if time.time()-player.start>7 and time.time()-last_frame_change_ghost>0.25: #change sprite every 0.25s after 7 second
                ghost_frame+=1
                if ghost_frame>=2:
                    ghost_frame = 0
                last_frame_change_ghost = time.time()
            if ghost[1].eaten:
                screen.blit(EATEN[ghost[1].last_dir], ghost[1].rect)
            else:
                screen.blit(WARNNING[ghost_frame], ghost[1].rect)
    

    #draw target point  (# can be removed if wanting to see ghosts' target.)
    #pygame.draw.circle(screen, (255,0,0),blinky.target_rect.center, 5) #blinky
    #pygame.draw.circle(screen, (255,184,255),pinky.target_rect.center, 5) #pinky
    #pygame.draw.circle(screen, (0,255,255),inky.target_rect.center, 5) #inky
    #pygame.draw.circle(screen, (255,184,82),player.rect.center, 6*w_b, 5) #clyde


    #draw lives
    for i in range(player.lives):
        screen.blit(PACMAN[1][0], (lives_rect.centerx+40*i, lives_rect.centery))

    

    text_dot = font.render(f"Remaining: {player.get_dot()}", True, (255, 255, 255))  # white color
    text_time = font.render(f"Time: {round(time.time()-start)} seconds", True, (255, 255, 255))  # white color

    screen.blit(text_dot, text_rect_dot)
    screen.blit(text_time, text_rect_time)
    
    pygame.display.update()
