#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Pwd:
  cwd: str
  prompt: str

  def replace_prev_mini_cwd(self):
    """Cwd will not help me to find which was the last directory to replace it.

    Will iterate it and find all *os.path.sep ('/' - for linux) till the backslash '\\'
    """
    new_prompt = b''
    replace_mode = False

    for cidx, char in enumerate(self.prompt):

      if char == '\\':
        if replace_mode:
          replace_mode = False
          new_prompt += b'\w'

      if char == os.path.sep:
        if not replace_mode:
          replace_mode = True
          continue

      if replace_mode:
        continue

      new_prompt += char.encode()

    return new_prompt.decode()

  def mini_cwd(self):
    """Minimizing the directory names till the last one (the current one).
    """
    parts = Path(self.cwd).parts
    mini_path = []

    for part in parts[:-1]:
      mini_path.append(part[0])

    mini_path.append(parts[-1])

    return os.path.join(*mini_path)

  def cwd2mini(self):
    """Replacing (editing) the default PS1 working_directory ('\w') with my own.
    """
    new_prompt = b''
    skip_me = 0

    for cidx, char in enumerate(self.prompt):

      if skip_me > 0:
        skip_me -= 1
        continue

      # \w - working directory
      if (char == '\\') and (self.prompt[cidx+1] == 'w'):
        new_prompt += self.mini_cwd().encode()
        skip_me += 1
        continue

      new_prompt += char.encode()

    return new_prompt

  def main(self):
    self.prompt = self.replace_prev_mini_cwd()
    return self.cwd2mini()

    # pipe
    # sys.stdout.write(self.prompt)
