# Example file showing a basic pygame "game loop"
import pygame
import random
# Setup a list of y posisiotn changes
y_pos_list = [-3, -2, -1, 0, 1, 2, 3]
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1461, 806))
clock = pygame.time.Clock()
running = True
# Inialise variables
lb_ypos = 300
rb_ypos = 300
lb_move = 0
rb_move = 0
left_score = 0
right_score = 0
ball_xpos = 625
ball_ypos = 350
x_move = 10
y_move =0 

# Load the background image, bat and ball
pitch = pygame.image.load('tennis-court-dimensions.jpg')
ball = pygame.image.load('Monkey.png')
left_bat = pygame.image.load('Bat.png')    # Height size of 120px
right_bat = pygame.image.load('Bat2.png')  # Height size of 120px

# Load font
font_message = pygame.font.SysFont('arial', 64)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                lb_move = -10
            elif event.key == pygame.K_s:
                lb_move = 10
            elif event.key == pygame.K_UP:
                rb_move = -10
            elif event.key == pygame.K_DOWN:
                rb_move = 10
                
    # Logic section
    ball_xpos += x_move
    ball_ypos += y_move
    lb_ypos += lb_move
    rb_ypos += rb_move
    
    # Check if ball at edge
    if ball_xpos >= 900:
        if ball_ypos >= rb_ypos and ball_ypos <= rb_ypos+120:
            x_move = -10
        else:
            left_score += 1
            ball_xpos = 470
    elif ball_xpos <= 150:
        if ball_ypos >= lb_ypos and ball_ypos <= lb_ypos+120:
            x_move = 10
        else:
            right_score += 1
            ball_xpos = 470
            
    elif ball_xpos <= 60:
        if ball_ypos >= lb_ypos and ball_ypos <= lb_ypos+120:
            x_move = 10
            y_move = random.sample(y_pos_list, 1)[0]
        else:
            right_score += 1
            ball_xpos = 470
            
    # Stop bats moving off window
    lb_move = 0
    if lb_ypos > 520:
        lb_move = 0
    if rb_ypos < 10:
        rb_move = 0
    if rb_ypos > 520:
        rb_move = 0
        
    # Stop ball from moving off window - make it bounce
    if ball_ypos < 0 or ball_ypos > 620:
        y_move *= -1
        
    # Stop ball from moving off window - make it bounce
        if ball_ypos < 0 or ball_ypos > 620:
            y_move *= -1

               
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(pitch, (0,0))
    
    # RENDER YOUR GAME HERE
    screen.blit(left_bat, (20,lb_ypos))
    screen.blit(right_bat, (900,rb_ypos))
    screen.blit(ball, (ball_xpos,ball_ypos))
    
    # Display score text
    text = font_message.render(f'{left_score} SCORE {right_score}', True, (0,0,0))
    screen.blit(text, (325, 0))
       
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(999)  # limits FPS to 60
