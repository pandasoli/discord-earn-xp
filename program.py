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
  props = {}
  bot = {}
  spam = {}

  def __init__(self, props: dict):
    self.chlen = 0
    self.passedchs = 0
    self.props = props

    err, file = openf(f"texts/{props.get('text')}.json")

    if file != None: self.lines = json.load(file)
    else: return print(err)

    err, file = openf(f"ex-bots/{props.get('ex-bot')}.yml")

    if file != None: self.bot = yaml.safe_load(file)
    else: return print(err)

    if props.get('anti-spam'):
      err, file = openf(f"anti-spam/{props.get('anti-spam')}.yml")

      if file != None:
        self.spam = yaml.safe_load(file)

        self.spam['msg time'] |= 0
      else: return print(err)

    self.chlen = sum(len(line) for line in self.lines)

  def run(self):
    self.send(self.bot.get('get profile') or '')

    for i, line in enumerate(self.lines):
      self.print(i)
      self.send(line, i)
      sleep(self.spam.get('msg time') or 1.5)

    self.send(self.bot.get('get profile') or '')
    self.send(self.bot.get('get rank') or '')

  def print(self, i: int):
    per = self.passedchs / self.chlen * 100
    print(f'{i} of {len(self.lines)} lines, it means {per:.3}%        ', end = '\r')

  def send(self, text: str, linei: int = -1):
    self.write(text, linei)
    gui.press('enter')

  def write(self, txt: str, linei: int = -1):
    lines = txt.split('\n')

    for line in lines:
      # Formatting
      line = line.replace('(', '_(')
      line = line.replace(')', ')_')

      if line != '' and line.upper() == line:
        line = f'**{line}**'

      # Printing percentage
      if linei > -1:
        self.passedchs += len(line)
        self.print(linei)

      # Writing
      pyperclip.copy(line + '\n')
      gui.hotkey('ctrl', 'v')

      sleep(0.05)
