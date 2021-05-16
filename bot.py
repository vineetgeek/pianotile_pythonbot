import pyautogui
from pynput.mouse import Button , Controller
import keyboard

mouse = Controller()
 # lets make the function to click the button 

def clickTile( x , y ):
    mouse.position = (x , y)
    mouse.click(Button.left , 1)

 

# X:  511 Y:  512 RGB: ( 59,  56,  63)
# X:  402 Y:  517 RGB: (235, 235, 236)
# X:  297 Y:  495 RGB: (235, 235, 236)
# X:  203 Y:  493 RGB: (235, 235, 236)

# y position can be constant


yPosition = 510 

while keyboard.is_pressed("q") == False:
    # check the button value

    try:
        if pyautogui.pixel( 511 , yPosition )[0] == 59:
            clickTile(511 , yPosition)
        if pyautogui.pixel( 402 , yPosition )[0] == 59:
            clickTile(402 , yPosition)
        if pyautogui.pixel( 297 , yPosition )[0] == 59:
            clickTile(297 , yPosition)
        if pyautogui.pixel( 203 , yPosition )[0] == 59:
            clickTile(203 , yPosition)

    except:
        print("could not find the button ")