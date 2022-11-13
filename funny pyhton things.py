import pyautogui as p
import time as t

def openPython():
    p.press('win')
    p.write('python')
    p.press('enter')
    t.sleep(2)
    findFile = p.locateOnScreen('pythonFindFile.png')
    p.click(findFile)
    findNewFile = p.locateOnScreen('pythonFindNewFile.png')
    p.click(findNewFile)

def findOddOrEven(owo):
    p.press('enter')
    p.write(f"print(num,'is {owo}')")
    p.press('enter')
    p.press('backspace')
    
def writeProgram():
    iteration = 1
    p.write("num = int(input('Enter a number: '))")
    p.press('enter')
    p.write('if num == 0:')
    p.press('enter')
    p.write("print(num,'is even')")
    p.press('enter')
    p.press('backspace')
    while 'penis' != '6 inches':
        p.write(f'elif num == {iteration}:')
        if iteration % 2 == 0:
           findOddOrEven('even')
        else:
            findOddOrEven('odd')
        iteration += 1


openPython()
while 'my ass' != 'small':
    writeProgram()
