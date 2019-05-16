import pyautogui
from time import sleep
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
#print (pyautogui.position())

i = 0
while True:
    print(i)
    if i == 5:
        break
    else:
        i += 1
        pyautogui.moveTo(974, 747)
        pyautogui.doubleClick()
        #toolbar
        pyautogui.moveTo(111, 685)
        pyautogui.click()
        #page1
        for k in range(0, i):
            pyautogui.moveTo(959, 608)
            pyautogui.click()
            print("*", end=' ')
        print("\r")
        #select down
        pyautogui.moveTo(864, 569)
        pyautogui.click()
        # select student
        pyautogui.moveTo(31, 30)
        pyautogui.click()
        # file
        pyautogui.moveTo(71, 415)
        pyautogui.click()
        # explore to pdf
        pyautogui.press('enter')
        sleep(10)
