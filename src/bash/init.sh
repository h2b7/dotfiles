#!/bin/bash

export _ALIASES="$DOTFILES/bash/aliases"
export _PROMPT="$DOTFILES/bash/prompt"
export _TOOLS="$DOTFILES/bash/tools"

. "$_ALIASES/init.sh"
. "$_PROMPT/init.sh"
. "$_TOOLS/init.sh"
