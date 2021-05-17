#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from mini_pwd import Pwd
from git_bs import Git


if __name__ == '__main__':
  cwd = sys.argv[1]
  prompt = ' '.join(sys.argv[2:])

  prompt = Pwd(cwd, prompt).main()
  prompt = Git(prompt).main()

  sys.stdout.write(prompt.decode())
