import time
from Tkinter import *

window = Tk()
canvas = Canvas(window, width=800, height=600, bg='#cecece')
canvas.pack()

# ---------------ROBOT COORDS------------
x1r = 2
x2r = 22
y1r = 40
y2r = 60
#---------------VELOCITY----------------
vx = 1.0
vy = 1.0
#---------------OBSTACLES---------------
x11 = 65
x21 = 95
y11 = 0
y21 = 79
obstacle1 = canvas.create_rectangle(x11, y11, x21, y21, outline='#ef9800', fill='#ef9800')

x12 = 65
x22 = 95
y12 = 101
y22 = 600
obstacle2 = canvas.create_rectangle(x12, y12, x22, y22, outline='#ef9800', fill='#ef9800')

x13 = 145
x23 = 175
y13 = 0
y23 = 159
obstacle3 = canvas.create_rectangle(x13, y13, x23, y23, outline='#ef9800', fill='#ef9800')

x14 = 145
x24 = 175
y14 = 181
y24 = 600
obstacle4 = canvas.create_rectangle(x14, y14, x24, y24, outline='#ef9800', fill='#ef9800')

x15 = 225
x25 = 255
y15 = 0
y25 = 159
obstacle5 = canvas.create_rectangle(x15, y15, x25, y25, outline='#ef9800', fill='#ef9800')

x16 = 225
x26 = 255
y16 = 181
y26 = 600
obstacle6 = canvas.create_rectangle(x16, y16, x26, y26, outline='#ef9800', fill='#ef9800')

x17 = 305
x27 = 335
y17 = 0
y27 = 579
obstacle7 = canvas.create_rectangle(x17, y17, x27, y27, outline='#ef9800', fill='#ef9800')

x18 = 385
x28 = 415
y18 = 25
y28 = 600
obstacle8 = canvas.create_rectangle(x18, y18, x28, y28, outline='#ef9800', fill='#ef9800')

x19 = 465
x29 = 495
y19 = 0
y29 = 49
obstacle9 = canvas.create_rectangle(x19, y19, x29, y29, outline='#ef9800', fill='#ef9800')

x110 = 465
x210 = 495
y110 = 71
y210 = 600
obstacle10 = canvas.create_rectangle(x110, y110, x210, y210, outline='#ef9800', fill='#ef9800')

x111 = 545
x211 = 575
y111 = 0
y211 = 449
obstacle11 = canvas.create_rectangle(x111, y111, x211, y211, outline='#ef9800', fill='#ef9800')

x112 = 545
x212 = 575
y112 = 471
y212 = 600
obstacle12 = canvas.create_rectangle(x112, y112, x212, y212, outline='#ef9800', fill='#ef9800')

x113 = 625
x213 = 655
y113 = 0
y213 = 79
obstacle13 = canvas.create_rectangle(x113, y113, x213, y213, outline='#ef9800', fill='#ef9800')

x114 = 625
x214 = 655
y114 = 101
y214 = 499
obstacle14 = canvas.create_rectangle(x114, y114, x214, y214, outline='#ef9800', fill='#ef9800')

x115 = 625
x215 = 655
y115 = 521
y215 = 600
obstacle15 = canvas.create_rectangle(x115, y115, x215, y215, outline='#ef9800', fill='#ef9800')

x116 = 705
x216 = 735
y116 = 0
y216 = 49
obstacle16 = canvas.create_rectangle(x116, y116, x216, y216, outline='#ef9800', fill='#ef9800')

x117 = 705
x217 = 735
y117 = 71
y217 = 600
obstacle17 = canvas.create_rectangle(x117, y117, x217, y217, outline='#ef9800', fill='#ef9800')

#---------------ROBOT--------------------
robot = canvas.create_rectangle(x1r, y1r, x2r, y2r, outline='#0d8201', fill='#0d8201')
x1r, y1r, x2r, y2r = canvas.coords(robot)
canvas.coords(robot, x1r, y1r, x2r, y2r)
canvas.update()

#---------------START--------------------
x1s = 2
x2s = 22
y1s = 40
y2s = 60
start = canvas.create_rectangle(x1s, y1s, x2s, y2s, outline='#63a9ff', fill='#63a9ff')

#---------------END----------------------
x1e = 780
x2e = 800
y1e = 540
y2e = 560
end = canvas.create_rectangle(x1e, y1e, x2e, y2e, outline='#043d82', fill='#043d82')
#---------------MOTION LOOPS-------------
t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x11 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == (y21 + 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x13 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == (y23 + 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x17 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == (y27 + 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x18 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r - vy
    y2r = y2r - vy
    if y2r == (y18 - 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x19 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == (y29 + 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x111 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == (y211 + 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x114 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r - vy
    y2r = y2r - vy
    if y2r == (y114 - 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x117 - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r - vy
    y2r = y2r - vy
    if y2r == (y117 - 1):
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == (x1e - 1):
        t = 0

while t == 0:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    y1r = y1r + vy
    y2r = y2r + vy
    if y1r == y1e:
        t = 1

while t == 1:
    canvas.coords(robot, x1r, y1r, x2r, y2r)
    canvas.update()
    time.sleep(0.01)
    x1r = x1r + vx
    x2r = x2r + vx
    if x2r == x2e:
        t = 0

window.mainloop()

