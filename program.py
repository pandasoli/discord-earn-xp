from io import TextIOWrapper
import pyautogui as gui
from typing import Tuple
from time import sleep
import pyperclip
import json
import yaml


def openf(f: str) -> Tuple[str | None, TextIOWrapper | None]:
  try:
    file = open(f, 'r')
    return None, file
  except FileNotFoundError:
    return 'The file does not exist.', None
  except IOError:
    return 'An I/O error occurred while reading the file.', None


class Program:
  lines: list[str]
  chlen: int
  passedchs: int
  props: dict
  bot: dict

  def __init__(self, props: dict):
    self.chlen = 0
    self.passedchs = 0
    self.props = props

    err, file = openf(f"texts/{props['text']}.json")

    if file != None: self.lines = json.load(file)
    else: return print(err)

    err, file = openf(f"ex-bots/{props['ex-bot']}.yml")

    if file != None: self.bot = yaml.safe_load(file)
    else: return print(err)

    self.chlen = sum(len(line) for line in self.lines)

  def run(self):
    gui.write(self.bot['get profile'], interval = 0.08)
    gui.press('enter')

    for i, line in enumerate(self.lines):
      self.print(i)
      self.write(line, i)
      sleep(1.5)

    gui.write(self.bot['get profile'], interval = 0.08)
    gui.press('enter')
    sleep(5)
    gui.write(self.bot['get rank'], interval = 0.08)
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
