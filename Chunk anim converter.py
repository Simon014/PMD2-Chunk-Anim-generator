#chuck anim to tile anims
from pil import Image
import os
import time as t
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()
print("Full chuck to tile generator for animations")
print("Before using, make sure that the chucks you")
print("want animated is stacked vertically.")
print("The format will be checked before conversion.")
print("for more information check the read me.")
#todo : that read me file
print("============================================")
print("select the image:")
img = askopenfilename()
print("select the output folder:")
out = askdirectory()
print(f"{img} selected to convert, {out} selected as output folder.")
input("Press enter to continue :")

#start
im = Image.open(f"{img}")
x,y = im.size
if x != 24:
    print("width is not 24 pixels. Exiting.")
    quit()
if y % 24 != 0:
    print("Height is not divisable by 24. Exiting")
    quit()
lpn = int(y/24)
print(lpn)
imf = Image.new(mode="RGB",size=(int(8*lpn), 8*9))

xs = 0
ys = 0
xsf = 0
ysf = 0
for l in range(3): #first pass
    for i in range(lpn):#create row
        box = (xs, ys, xs +8 , ys + 8)
        tmp = im.crop(box)
        imf.paste(tmp, (xsf, ysf))
        ys += 24
        xsf += 8
    xsf = 0
    ysf += 8
    ys = 0
    xs += 8

xs = 0
ys = 8
xsf = 0
ysf = 24
for l in range(3): #second pass
    for i in range(lpn):#create row
        box = (xs, ys, xs +8 , ys + 8)
        tmp = im.crop(box)
        imf.paste(tmp, (xsf, ysf))
        ys += 24
        xsf += 8
    xsf = 0
    ysf += 8
    ys = 8
    xs += 8

xs = 0
ys = 16
xsf = 0
ysf = 48
for l in range(3): #third pass
    for i in range(lpn):#create row
        box = (xs, ys, xs +8 , ys + 8)
        tmp = im.crop(box)
        imf.paste(tmp, (xsf, ysf))
        ys += 24
        xsf += 8
    xsf = 0
    ysf += 8
    ys = 8
    xs += 8
imf.save(f"{out}\\converted.png")

