from tkinter import Y
import pyautogui
import time
from PIL import Image
from pytesseract import *
import win32api
import os

pytesseract.tesseract_cmd = r'C:\Users\Benge\AppData\Local\Tesseract-OCR\tesseract.exe'

# state_left = win32api.GetKeyState(0x02)  # Left button down = 0 or 1. Button up = -127 or -128

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

# Example


def isTuple(x): return type(x) == tuple
 
def flatten(T):
    if not isTuple(T): return (T,)
    elif len(T) == 0: return ()
    else: return flatten(T[0]) + flatten(T[1:])

def clickCheck(check):
    trigger = 0
    start = None
    stop = None


    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)

    clicked = False

    while check:

        if(trigger == 0):
            start = pyautogui.mouseinfo.position()
        if(trigger == 2):
            stop = pyautogui.mouseinfo.position()
        

        
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)


        if(a != state_left):
            trigger += 1
            state_left = a
            if a < 0:
                clicked = True
            else:
                clicked = False

        if(start and stop != None):
            check = not check
        # print(clicked, trigger)

        time.sleep(0.001)

    return (start, stop)
                
        

check = True

cords = clickCheck(check)
# cords = flatten(cords)

def trbl(cords):
    x0, x1, y0, y1 = cords
    x = y0, x1
    y = x0, y1
    return (x, y)
def brtl(cords):
    y, x = cords
    print(y, x)
    return (x, y)
def bltr(cords):
    x0, x1, y0, y1 = cords
    x = x0, y1
    y = y0, x1
    return (x, y)
def translate(x, y):
    t = y[0]-x[0]
    u = y[1]-x[1]
    return (x, t, u)

def rtnCords(cords):
    x, y = cords

    if(x[0]>y[0]):
        if(x[1] < y[1]): #top-right to bottom-left
            print("trbl")
            return trbl(flatten(cords))
        else: #bottom-right to top-left
            print("brtl")
            return brtl(cords)
    elif(x[1]>y[1]):
        print("bltr")
        return bltr(flatten(cords))
    print("tlbr")
    return x,y



#print(x,y)



# def ltr(cords):
#     if(cords[0][0]>cords[1][0]):
#         y, x = cords
#     else:
#         x, y = cords

#     z = []
#     z.append(y[0]-x[0])
#     z.append(y[1]-x[1])
#     t,u = z

#     return (x, t,u)

 
# cords = ltr(cords)
# print(cords)
# cords = flatten(cords)


cords = rtnCords(cords)
print(cords)
x, y = cords
print(x, y)
cords = flatten(translate(x, y))

print(cords)
save = pyautogui.screenshot(region = cords)

save.save("screenshot.png")
img = Image.open("screenshot.png")
output = pytesseract.image_to_string(img)

print(output)