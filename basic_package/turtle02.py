import turtle as taobin
import colorsys as cs

taobin.setup(800,800)
taobin.width(2)
taobin.bgcolor("black")
taobin.speed(0)
taobin.tracer(10)

def square(x):
       for i in range(4):
             taobin.forward(x)
             taobin.left(90)

for j in range(30):
      for i in range(15):
            taobin.color(cs.hsv_to_rgb(i/14,j/29,1))
            taobin.right(135)
            square(200-j*2)
            taobin.left(135)
            taobin.circle(50,24)

taobin.done()
