import pyautogui
import time
import psutil
import random

array = [r"RandomeChroma\black.png", 
        r"RandomeChroma\blue.png",
        r"RandomeChroma\cyan.png",
        r"RandomeChroma\green.png",
        r"RandomeChroma\none.png",
        r"RandomeChroma\orange.png",
        r"RandomeChroma\pink.png",
        r"RandomeChroma\red.png",
        r"RandomeChroma\white.png"]

while "LeagueClientUxRender.exe" in (i.name() for i in psutil.process_iter()):
    time.sleep(1)
    r=None 
    r=pyautogui.locateOnScreen(r"RandomeChroma\unknown.png", grayscale=False, confidence=0.8)
    if(r!=None):
        pyautogui.moveTo(r)
        pyautogui.leftClick(r)
        colorrand = random.choice(array)
        a = pyautogui.locateOnScreen("{}".format(colorrand), grayscale=False, confidence=0.8)
        pyautogui.leftClick(a)
        continue