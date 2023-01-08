import pyautogui as gui
from time import sleep
import pyperclip
import json

for i in range(0, 5):
  print(f'{5 - i}...', end = '\r')
  sleep(1)

class Program:
  lines: list[str]
  chlen: int
  passedchs: int

  def __init__(self):
    self.chlen = 0
    self.passedchs = 0

    with open('movie-script.json', 'r') as f:
      self.lines = json.load(f)

    for line in self.lines:
      self.chlen += len(line)

  def run(self):
    gui.write('+profile', interval = 0.08)
    gui.press('enter')

    for i, line in enumerate(self.lines):
      self.print(i)
      self.write(line, i)
      sleep(1.5)

    gui.write('+profile', interval = 0.08)
    gui.press('enter')
    sleep(3)
    gui.write('+rank', interval = 0.08)
    gui.press('enter')

  def print(self, i: int):
    per = self.passedchs / self.chlen * 100
    print(f'{i} of {len(self.lines)} lines, it means {per:.3}%        ', end = '\r')

  def write(self, txt: str, linei: int):
    lines = txt.split('\n')

    for line in lines:
      # Formatting
      line = line.replace('(', '_(')
      line = line.replace(')', ')_')

      if line != '' and line.upper() == line:
        line = f'**{line}**'

      # Printing percentage
      self.passedchs += len(line)
      self.print(linei)

      # Writing
      pyperclip.copy(line + '\n')
      gui.hotkey('ctrl', 'v')
      sleep(0.05)

    gui.press('enter')

Program().run()

