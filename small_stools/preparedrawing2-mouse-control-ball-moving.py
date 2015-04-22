# -*- coding: utf-8 -*-
# control the velocity of a ball using mouse

import math
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Initialize global
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 15
ball_color = "Yellow"

ball_pos = [WIDTH / 2, HEIGHT / 2]


#define event handlers
def distance(p, q):
    return math.sqrt( (p[0]-q[0]) ** 2 + (p[1]-q[1]) ** 2)

def draw(canvas):
    
    #Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", ball_color)

def click(pos):
    global ball_pos, ball_color #为什么要申明ballcolor为全局变量？当不申明ball_color是全局变量时，点击小球内部小球颜色不变
    if distance(pos, ball_pos) < BALL_RADIUS:
        ball_color = "Blue"
    else:
        ball_pos = list(pos)
        ball_color = "Yellow"
      
       
# create frame
frame = simplegui.create_frame("mouse control ball moving",WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start() #居然在start下面忘了（），导致程序无法运行，这个格式太重要了！

