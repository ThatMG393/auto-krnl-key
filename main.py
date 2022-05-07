from threading import Thread
from PIL import ImageGrab
from turtle import up
import pyautogui
import time
import pytesseract
from pytesseract import Output

def run():
    
    try: checkpoint = int(input("Please enter your current checkpoint: ")) 
    except ValueError: 
        print("Please enter an integer!")
        return run()
    
    if checkpoint < 1 or checkpoint > 4: 
        print("Invalid checkpoint number!")
        return run()

    print("You have 7 seconds to switch to \"cdn.krnl.ca/getkey.php\"!")
    time.sleep(7)
    start(checkpoint)
    print("Yey")

def start(cp: int):
    i = cp
    while i <= 6:
        if cp == 1:
            check()
            i += 1
        elif cp == 2:
            check()
            i += 1
        elif cp == 3:
            check()
            i += 1
        elif cp == 4:
            check()
            i += 1
        elif cp >= 5:
            print("Finished!")
            break
        else: 
            print("Fatal error!")
            print("You managed to bypass the checkpoint limit.")
            print("Exiting...")
            exit(69420)

def check():

    check_box = pyautogui.pixel(808,343)
    check_mark = pyautogui.pixel(825,339)

    if check_box == (193, 193, 193) or check_box == (255, 0, 0): # Possible wrong check in check_box == (255, 0, 0)
        print("Unchecked.")
        captcha()
        while True:
            check_mark = pyautogui.pixel(825,339) # Updates the color
            if check_mark == (0, 158, 85): break
    elif check_mark == (0, 158, 85):
        print("Checked.")  
    else:
        print("Fatal error!")
        print("Are you in \"cdn.krnl.ca/getkey.php\"?")
        print("Exiting...") 
        exit(69420)

    print("1")
    proceed()
    time.sleep(7)
    ss = ImageGrab.grab(bbox=(233,37,549,63))
    ss_gs = ss.convert('L')

    # 233, 37 to 549, 63 address bar 
    # 660, 277 to 1256, 307 token display

    url = pytesseract.image_to_boxes(ss_gs, output_type = Output.DICT)
    print(url)
    while True:
        
        break
    time.sleep(20)

def captcha(): pyautogui.click(820,346)
def proceed(): pyautogui.click(824,416)

if __name__ == "__main__":
    get1 = input('\nPlace cursor at the top left of the region you want to capture, and then press enter \n')
    pos1 = pyautogui.position()

    get2 = input('Now place your cursor at the bottom right of the region you want to capture, and press enter \n')
    pos2 = pyautogui.position()

    width = pos2[0] - pos1[0]
    height = pos2[1] - pos1[1]

    print('Your region is... \n')

    print('region=('+str(pos1[0])+','+str(pos1[1])+','+str(width)+','+str(height)+') \n')


    print("This is just a test.")
    print("After you enter your current checkpoint, switch to \"cdn.krnl.ca/getkey.php\" or else it will gonna exit.")
    run()