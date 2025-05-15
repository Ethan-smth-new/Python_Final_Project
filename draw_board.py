import pygame

def db(screen, line_color, h_b, w_b, board):
    for i, lst in enumerate(board):
        for j , val in enumerate(lst):
            if val == 11:
                pygame.draw.circle(screen, (255,255,255), ((j+0.5)*w_b, (i+0.5)*h_b), 4)
            elif val == 12:
                pygame.draw.circle(screen, (255,255,255), ((j+0.5)*w_b, (i+0.5)*h_b), 10)
            elif val == 13:
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, i*h_b), ((j+0.5)*w_b, (i+1)*h_b), 3)
            elif val == 14:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.5)*h_b),  ((j+1)*w_b, (i+0.5)*h_b), 3)
            elif val == 15:
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i+1)*h_b), ((j+0.5)*w_b, (i+0.7)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.8)*w_b, (i+0.5)*h_b),  ((j+1.2)*w_b, (i+0.5)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.6)*w_b, (i+0.6)*h_b), ((j+0.75)*w_b, (i+0.6)*h_b), 4)
            elif val == 16:
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i+1)*h_b), ((j+0.5)*w_b, (i+0.7)*h_b), 3)
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.5)*h_b),  ((j+0.2)*w_b, (i+0.5)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, (i+0.6)*h_b), ((j+0.4)*w_b, (i+0.6)*h_b), 4)
            elif val == 17:
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i-0.2)*h_b), ((j+0.5)*w_b, (i+0.3)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.8)*w_b, (i+0.5)*h_b),  ((j+1.2)*w_b, (i+0.5)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.59)*w_b, (i+0.37)*h_b), ((j+0.72)*w_b, (i+0.37)*h_b), 4)
            elif val == 18:
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i-0.2)*h_b), ((j+0.5)*w_b, (i+0.3)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j)*w_b, (i+0.5)*h_b),  ((j+0.2)*w_b, (i+0.5)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, (i+0.37)*h_b), ((j+0.4)*w_b, (i+0.37)*h_b), 4)
            elif val == 19:
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, i*h_b), ((j+0.75)*w_b, (i+1)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, i*h_b), ((j+0.25)*w_b, (i+1)*h_b), 3)
            elif val == 20:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.25)*h_b),  ((j+1)*w_b, (i+0.25)*h_b), 3)
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.75)*h_b),  ((j+1)*w_b, (i+0.75)*h_b), 3)
            elif val == 21:
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, (i+1)*h_b), ((j+0.25)*w_b, (i+0.6)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, (i+0.25)*h_b),  ((j+1)*w_b, (i+0.25)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.4)*w_b, (i+0.5)*h_b), ((j+0.4)*w_b, (i+0.6)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.55)*w_b, (i+0.38)*h_b), ((j+0.7)*w_b, (i+0.38)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, (i+1)*h_b), ((j+0.75)*w_b, (i+0.99)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.85)*w_b, (i+0.85)*h_b), ((j+0.97)*w_b, (i+0.85)*h_b), 4)
            elif val==22:
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, (i+1)*h_b), ((j+0.75)*w_b, (i+0.6)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.3)*w_b, (i+0.25)*h_b),  ((j)*w_b, (i+0.25)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.6)*w_b, (i+0.5)*h_b), ((j+0.6)*w_b, (i+0.6)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i+0.38)*h_b), ((j+0.35)*w_b, (i+0.38)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, (i+1)*h_b), ((j+0.25)*w_b, (i+0.99)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.2)*w_b, (i+0.85)*h_b), ((j+0.05)*w_b, (i+0.85)*h_b), 4)
            elif val == 23:
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, (i+0.4)*h_b), ((j+0.25)*w_b, (i)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+1)*w_b, (i+0.75)*h_b),  ((j+0.7)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.6)*w_b, (i+0.7)*h_b), ((j+0.6)*w_b, (i+0.57)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.5)*w_b, (i+0.5)*h_b), ((j+0.35)*w_b, (i+0.5)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.8)*w_b, (i+0.12)*h_b), ((j+0.99)*w_b, (i+0.12)*h_b), 4)
            elif val==24:
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, (i+0.4)*h_b), ((j+0.75)*w_b, (i)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j)*w_b, (i+0.75)*h_b),  ((j+0.26)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.3)*w_b, (i+0.7)*h_b), ((j+0.3)*w_b, (i+0.57)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.47)*w_b, (i+0.5)*h_b), ((j+0.65)*w_b, (i+0.5)*h_b), 4)
                pygame.draw.line(screen, line_color, ((j+0.05)*w_b, (i+0.1)*h_b), ((j+0.2)*w_b, (i+0.1)*h_b), 4)
            elif val == 25:
                pygame.draw.line(screen, (255,255,255), (j*w_b, (i+0.5)*h_b), ((j+1)*w_b, (i+0.5)*h_b), 7)
            elif val==26:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.25)*h_b),  ((j+1)*w_b, (i+0.25)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.85)*w_b, (i+0.75)*h_b), ((j+1)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.6)*w_b, (i+0.85)*h_b), ((j+0.78)*w_b, (i+0.85)*h_b), 4)
            elif val == 27:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.25)*h_b),  ((j+1)*w_b, (i+0.25)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.1)*w_b, (i+0.75)*h_b), ((j)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.4)*w_b, (i+0.85)*h_b), ((j+0.2)*w_b, (i+0.85)*h_b), 4)
            elif val==28:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.75)*h_b),  ((j+1)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.05)*w_b, (i+0.1)*h_b), ((j+0.4)*w_b, (i+0.1)*h_b), 4)
            elif val == 29:
                pygame.draw.line(screen, line_color, (j*w_b, (i+0.75)*h_b),  ((j+1)*w_b, (i+0.75)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.6)*w_b, (i+0.1)*h_b), ((j+0.97)*w_b, (i+0.1)*h_b), 4)
            elif val==30:
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, i*h_b), ((j+0.25)*w_b, (i+1)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.9)*w_b, (i+0.95)*h_b), ((j+0.9)*w_b, (i+0.65)*h_b), 4)
            elif val == 31:
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, i*h_b), ((j+0.75)*w_b, (i+1)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.07)*w_b, (i+0.95)*h_b), ((j+0.07)*w_b, (i+0.65)*h_b), 4)
            elif val==32:
                pygame.draw.line(screen, line_color, ((j+0.75)*w_b, i*h_b), ((j+0.75)*w_b, (i+1)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.07)*w_b, (i+0.35)*h_b), ((j+0.07)*w_b, (i+0.1)*h_b), 4)
            elif val == 33:
                pygame.draw.line(screen, line_color, ((j+0.25)*w_b, i*h_b), ((j+0.25)*w_b, (i+1)*h_b), 3)
                pygame.draw.line(screen, line_color, ((j+0.9)*w_b, (i+0.35)*h_b), ((j+0.9)*w_b, (i+0.1)*h_b), 4)
                


            
