#Alexander Wolf
#9/27/14
#a pong game

from cs1lib import*
from time import sleep

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


def draw_paddles(paddle1_y, paddle2_y):#function that draws paddles taking parameters of the height of the two paddles
    set_fill_color(0,1,0)
    disable_stroke()
    draw_rectangle(0, paddle1_y,PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(380,paddle2_y,PADDLE_WIDTH,PADDLE_HEIGHT)
    
def main():#main function which sets a background, and runs a while loop that draws and changes location of paddle based off buttons pressed
    set_clear_color(0,0,0)
    paddle1_y=0
    paddle2_y=320
        
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
        #refreshes the window     
        request_redraw()
        #has while loop nap for .02 so we can see paddle move 
        sleep(NAP)
            
#graphics called with main function used
start_graphics(main,"Pong Game", WINDOW_LENGTH, WINDOW_HEIGHT)