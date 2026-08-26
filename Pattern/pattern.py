from turtle import *
import colorsys

speed(15)
bgcolor("black")
h=0

for i in range(7):
    for j in range (15):
        c= colorsys.hsv_to_rgb(h,1,1)
        color(c)
        h+=0.006
        rt(90)
        circle(175-j*6, 90)
        lt(90)
        circle(175-j *6, 90)
        
    circle(2,26)
done()