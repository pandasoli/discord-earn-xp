from time import sleep

print('gonna wait')
sleep(2)
print('waited')

import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
import pyautogui as gui
gui.hotkey('ctrl', 'v')

