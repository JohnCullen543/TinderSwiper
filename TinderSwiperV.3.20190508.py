# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:58:01 2019

@author: Johnny
Tinder Swiper for swiping right on everyone as fast as possible. 
I want to make it automated so I don't have to waste time every day 
swiping to get laid
If you want it to work perfectly you will need to crop the 
Tinder Heart and save it as a png in the
same folder as your saving this script

"""

import pyautogui as py

data = []

def locator():
    test = 'TinderHeart.png'
    cent = py.locateCenterOnScreen(test)
    py.moveTo(cent[0:2])
    py.click(button = 'left')

def Start():
    start = input('')
    if start:
        locator()
        SwipeRight(start)
    else:
        pass

def SwipeRight(start):
    for x in range(101):
        py.press('right', interval = .3)
        
        
Start()
