#Alexander Wolf
#9/27/14
#a pong game

from cs1lib import *
from time import sleep
from random import uniform

#define variables that never change
WINDOW_LENGTH=400
WINDOW_HEIGHT=400
PADDLE_WIDTH=20
PADDLE_HEIGHT=80
PADDLE1UP="a"
PADDLE1DOWN="z"
PADDLE2UP="k"
PADDLE2DOWN="m"
MOVE_Y=10
NAP=.02
LOWER_Y_LIMIT=320
UPPER_Y_LIMIT=0
START_NEW_GAME=" "
QUIT="q"
BALL_RADIUS=7
STARTING_BALL_X=200
STARTING_BALL_Y=200



def draw_paddles(paddle1_y, paddle2_y):#function that draws paddles taking parameters of the height of the two paddles
    set_fill_color(0,1,0)
    disable_stroke()
    draw_rectangle(0, paddle1_y,PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(380,paddle2_y,PADDLE_WIDTH,PADDLE_HEIGHT)

def ball(ball_x_location,ball_y_location):#function that draws ball
    r=uniform(0.0,1.0)
    g=uniform(0.0,1.0)
    b=uniform(0.0,1.0)
    set_fill_color(r,g,b)
    enable_smoothing()
    disable_stroke()
    draw_circle(ball_x_location, ball_y_location, BALL_RADIUS)
    
    
    
def main():#main function which sets a background, and runs a while loop that draws and changes location of paddle based off buttons pressed
    set_clear_color(0,0,1)
    paddle1_y=0
    paddle2_y=320
    ball_x_location=200
    ball_y_location=200
    x_velocity=3
    y_velocity=3
   
        
    while not window_closed():
        clear()
        draw_paddles(paddle1_y,paddle2_y)#draws paddles
        
        #if statements used to move paddle locations when keys are pressed
        if is_key_pressed(PADDLE1UP) and paddle1_y>UPPER_Y_LIMIT:
            paddle1_y=paddle1_y-MOVE_Y
        if is_key_pressed(PADDLE1DOWN) and paddle1_y<LOWER_Y_LIMIT:
            paddle1_y=paddle1_y+MOVE_Y
        if is_key_pressed(PADDLE2UP) and paddle2_y>UPPER_Y_LIMIT:
            paddle2_y= paddle2_y-MOVE_Y
        if is_key_pressed(PADDLE2DOWN) and paddle2_y<LOWER_Y_LIMIT:
            paddle2_y = paddle2_y +MOVE_Y
        
        ball(ball_x_location, ball_y_location)#draws ball
        
        #resets location of ball by changing the x and y coordinates of the ball
        ball_x_location= ball_x_location+x_velocity
        ball_y_location= ball_y_location+y_velocity
        
        #CHanges ball y velocity when it hits a horizontal wall
        if ball_y_location+BALL_RADIUS>=400:
            y_velocity=-3
        if ball_y_location-BALL_RADIUS<=0:
            y_velocity=3
            
        #Ends games if ball hits vertical wall
        if ball_x_location+BALL_RADIUS<=0:
            x_velocity=0
            y_velocity=0
            enable_stroke()
            set_stroke_color(1,1,1)
            draw_text("Game Over",170,200)
        if ball_x_location+BALL_RADIUS>=400:
            x_velocity=0
            y_velocity=0
            enable_stroke()
            set_stroke_color(1,1,1)
            draw_text("Game Over",170,200)
            
        #changes the velocity of ball when it hits a paddle
        if x_velocity!=0:
            if ball_x_location-BALL_RADIUS<=PADDLE_WIDTH and ball_y_location>=paddle1_y and ball_y_location<=paddle1_y+PADDLE_HEIGHT:
                x_velocity= 3
        if x_velocity!=0:
            if ball_x_location+BALL_RADIUS>=PADDLE_WIDTH+360 and ball_y_location>=paddle2_y and paddle2_y+PADDLE_HEIGHT>=ball_y_location:
                x_velocity= -3
                
        #starts new game when space bar is pressed
        if is_key_pressed(START_NEW_GAME):
            ball_x_location=STARTING_BALL_X
            ball_y_location=STARTING_BALL_Y
            x_velocity=3
            y_velocity=3
        
        #Quits game when q is pressed
        if is_key_pressed(QUIT):
            cs1_quit()
            
            
        #updates the window     
        request_redraw()
        #has while loop nap for .02 so we can see paddle move 
        sleep(NAP)
            
#graphics called with main function used
start_graphics(main,"Pong Game", WINDOW_LENGTH, WINDOW_HEIGHT)