from PIL import Image
import ImageDraw 
import random


def work(pos ,color):
    im.putpixel(pos ,color)

x = int(input("x:"))
y = int(input("y:"))
o,i = 1,1
color2 = (255,0,0)
x1 = x-1
y1 = y-1

im = Image.new( "RGB", (x,y) )
draw = ImageDraw.Draw(im )
for i in range(-1,x1):
    i = i+1
    for o in range(-1,y1):
       o = o+1
       R = random.randint(0,255)
       G = random.randint(0,255)
       B = random.randint(0,255)
       color2 = (R,G,B)
       work((i,o),(color2))
im.show()
im.save('01.bmp','bmp')
