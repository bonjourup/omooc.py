
#!/usr/bin/env python
# -*- coding: latin-1 -*-  
# a game  "guess the number"
import random
import math
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# initialize global variables
hint = "Welcome"

# user select a game range and start the game
def select1():
    global secretnumber100 #����ΪʲôҪ��������ó�ȫ�ֱ����ˣ���Ϊ�˷�����������������
    secretnumber100 = random.randrange(1,100)
    #return secretnumber100 # �������ǲ��ǿ���ȥ����secretnumber�Ѿ������ǲ��Ǿ��Ѿ��洢�� �����п��ܴ���

def select2():
    global secretnumber1000 
    secretnumber1000 = random.randrange(1,1000)
    #return secretnumber1000 #

def guessnumber(inp):
    guessnumber = int(inp)
    global hint 
    if guessnumber > secretnumber100:
       hint = "lower"
    elif guessnumber < secretnumber100:
         hint = "higher"
    elif guessnumber == secretnumber100:
         hint = "right"
    return hint #���ȥ��return��

# draw the result in canvas  
def draw(canvas):
    canvas.draw_text(hint,[80,150],50,"Red")
    
#0414�о����������û�б�Ҫ��ע�͵��������
#if select1():
#  canvas.draw_text(hint,[80,150],50��"Red")
#elif select2():
#   canvas.draw_text(hint,[60,150],50��"Red")
#draw the results in canvas

# create frame
f = simplegui.create_frame("guess the number",300,300)
# register event handle
f.add_button("1-100",select1,100)
f.add_button("1-1000",select2,100)
f.add_input("Enter your number",guessnumber,80,)
f.set_draw_handler(draw)

f.start() 
 
