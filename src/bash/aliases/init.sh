#!/bin/bash

#
# `cd` to the target directory ($1) and changing the pwd in the PS1
#
function ncd() {
  cd $1;
  . "$DOTFILES/bash/prompt/init.sh"
}

alias cd=ncd $1

. "$_ALIASES/.tmux"
. "$_ALIASES/.fs"
