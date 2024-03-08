import pyautogui as pag
pag.FAILSAFE = True

scrollSpeed = pag.prompt("How fast do you want to scoll? (1-100), enter a number", "Set Scroll Speed")

def autoScroll(scrollSpeed):
    try:
        while True:
            pag.scroll(scrollSpeed)
    except KeyboardInterrupt:
        pass # ctrl + c

# exceptions
try:  
    scrollSpeed = int(scrollSpeed)
    if 0 < scrollSpeed < 100:
        autoScroll(scrollSpeed)
    else:
        pag.alert("Please enter a number between 1 and 100.") 
except EOFError:
    pass