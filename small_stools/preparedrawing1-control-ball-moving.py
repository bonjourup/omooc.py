# -*- coding: utf-8 -*-
# control the velocity of a ball using the arrow keys

import math
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#Initialize global
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]


#define event handlers
def draw(canvas):
    
    #Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Yellow")

def keydown(key):
    vel = 4
    if key ==simplegui.KEY_MAP["left"]:
       ball_pos[0] -= vel
    elif key ==simplegui.KEY_MAP["right"]:
       ball_pos[0] += vel
    elif key ==simplegui.KEY_MAP["up"]:
       ball_pos[1] -= vel
    elif key ==simplegui.KEY_MAP["down"]:  
       ball_pos[1] += vel
       
       print ball_pos
       
# create frame
frame = simplegui.create_frame("control ball moving",WIDTH, HEIGHT)

# register event handler
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame

frame.start() #居然在start下面忘了（），导致程序无法运行，这个格式太重要了！

