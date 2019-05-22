import pyautogui
import sys
from time import sleep
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
#print (pyautogui.position())
try:
    i = 0
    while True:
        print(i)
        if i == 10: # i == number of students
            break
        else:
            i += 1
            pyautogui.moveTo(974, 747)
            pyautogui.doubleClick()
            # ^ goto toolbar (change accordingly, varies between two PCs)
            pyautogui.moveTo(111, 685)
            pyautogui.click()
            #goto ^ page1 (change accordingly, varies between two PCs)
            sleep(3)
            pyautogui.moveTo(748, 582)
            pyautogui.click()
            for k in range(0, i):
                pyautogui.hotkey('ctrl', 'down')
                pyautogui.press('enter')
                #pyautogui.press('down')
                #pyautogui.press('enter')
                #pyautogui.click()
                print("*", end=' ')
            print("\r")
            
            # ^ scroll down to next student (change accordingly, varies between two PCs)
            #pyautogui.moveTo(768, 577)
            #pyautogui.click()
            # ^ select student (change accordingly, varies between two PCs)
            sleep(3)
            ##starts
            pyautogui.moveTo(166, 540)
            sleep(1)
            pyautogui.rightClick()
            sleep(1)
            pyautogui.moveTo(168, 575)
            sleep(1)
            pyautogui.moveTo(375, 579)
            sleep(1)
            pyautogui.click()
            # select ph number
            ##ends
            pyautogui.moveTo(31, 30)
            pyautogui.click()
            # ^ goto file (change accordingly, varies between two PCs)
            pyautogui.moveTo(71, 415)
            pyautogui.click()
            # ^ export to pdf (change accordingly, varies between two PCs)
            pyautogui.press('enter')
            sleep(10)
            pyautogui.moveTo(1227, 110)
            pyautogui.doubleClick()
            pyautogui.doubleClick()
            # goto save as icon select save as in edge
            sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.press('left')
            pyautogui.press('enter')
            sleep(8)

except KeyboardInterrupt:
    sys.exit()

