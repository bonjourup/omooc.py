
#!/usr/bin/env python
# -*- coding: latin-1 -*-  
# a game  "guess the number"
import random
import math
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initialize global variables
hint = "Welcome"
global secretnumber100
global secretnumber1000

# user select a game range and start the game
def select1():
    global secretnumber100 #忘了为什么要把这个设置成全局变量了，是为了方便其他函数调用吗？
    secretnumber100 = random.randrange(1,100)
    return secretnumber100 # 这个语句是不是可以去掉，secretnumber已经产生是不是就已经存储了 问题有可能错误

def select2():
    global secretnumber1000 
    secretnumber1000 = random.randrange(1,1000)
    return secretnumber1000 #这个语句不能去掉，下面的函数guessthenumber需要调用这个数值

def guessnumber(inp):
    if select1():
        guessnumber = int(inp)
        global hint
#        global secretnumber100
        if guessnumber > secretnumber100:
           hint = "lower"
        elif guessnumber < secretnumber100:
             hint = "higher"
        elif guessnumber == secretnumber100:
             hint = "right"
             return hint
    elif select2():
        guessnumber = int(inp)
        global hint
#        global secretnumber1000
        if guessnumber > secretnumber1000:
           hint = "lower"
        elif guessnumber < secretnumber1000:
             hint = "higher"
        elif guessnumber == secretnumber1000:
             hint = "right"
        return hint

      
# draw the result in canvas  
def draw(canvas):
    canvas.draw_text(hint,[80,150],50,"Red")
    
#0414感觉这后面的语句没有必要，注释掉看看情况
#if select1():
#   canvas.draw_text(hint,[80,150],50,"Red")
#elif select2():
#     canvas.draw_text(hint,[80,150],50,"Red")
#draw the results in canvas

# create frame
f = simplegui.create_frame("guess the number",300,300)
# register event handle
f.add_button("1-100",select1,100)
f.add_button("1-1000",select2,100)
f.add_input("Enter your number",guessnumber,80,)
f.set_draw_handler(draw)

f.start() 
 
