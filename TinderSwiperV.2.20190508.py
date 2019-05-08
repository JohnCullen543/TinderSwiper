# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:58:01 2019

@author: Johnny
Tinder Swiper for swiping right on everyone as fast as possible. 
I want to make it automated so I don't have to waste time every day 
swiping to get laid
"""

import pyautogui as py

def Start():
    start = input('')
    if start:
        SwipeRight(start)
    else:
        pass

def SwipeRight(start):
    for x in range(101):
        py.press('right', interval = .2)
        
        
Start()