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
vel = [0, 0]


#define event handlers
def draw(canvas):
    #Upddate ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    #Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Yellow")

def keydown(key):
    acc = 2
    if key ==simplegui.KEY_MAP["left"]:
       vel[0] -= acc  # 将小球位置改变成了vel向量值的增加或者减少
    elif key ==simplegui.KEY_MAP["right"]:
       vel[0] += acc
    elif key ==simplegui.KEY_MAP["up"]:
       vel[1] -= acc
    elif key ==simplegui.KEY_MAP["down"]:  
       vel[1] += acc
       
       print ball_pos, vel
       
# create frame
frame = simplegui.create_frame("control ball moving",WIDTH, HEIGHT)

# register event handler
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame

frame.start() #居然在start下面忘了（），导致程序无法运行，这个格式太重要了！

