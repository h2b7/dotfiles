#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


"""Target sub-string to replace: (G:main) | (G:main *)

bash: sed -re 's/[(]G:\w*\W*\)/''/g''
python: re.sub
"""


@dataclass
class Git:
  prompt: str

  def main(self):
    new_prompt = b''
    ignore_mode = False

    for cidx, char in enumerate(self.prompt.decode()):
      if char == ')':
        if ignore_mode:
          # \b - backspace; git adding space arround the git status
          return (new_prompt + b'\b' + self.prompt[cidx+1:])

      if (char == '(') and (self.prompt[cidx+1] == ord('G')):
        if not ignore_mode:
          ignore_mode = True

      if ignore_mode:
        continue

      new_prompt += char.encode()

    return new_prompt
