#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"

# Color codes
# printf '\e[48;5;%dm ' {0..255}; printf '\e[0m \n' is a useful one-liner to see all colors on a 256-color terminal
if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    export TERM_TEXT_RED=$(tput setaf 1)
    export TERM_TEXT_GREEN=$(tput setaf 2)
    export TERM_TEXT_YELLOW=$(tput setaf 3)
    export TERM_TEXT_CYAN=$(tput setaf 6)
    export TERM_TEXT_RESET=$(tput sgr0)
else
    export TERM_TEXT_RED=""
    export TERM_TEXT_GREEN=""
    export TERM_TEXT_CYAN=""
    export TERM_TEXT_RESET=""
fi

# Usage: emph text
function emph {
    echo -n "${TERM_TEXT_CYAN}$1${TERM_TEXT_RESET}"
}

# Usage: say message
function say {
    echo "${TERM_TEXT_GREEN}THAvalon:${TERM_TEXT_RESET} $1"
}

# Usage: warn message
function warn {
    echo "${TERM_TEXT_YELLOW}WARNING:${TERM_TEXT_RESET} $1" 1>&2
}

# Usage: error message
function error {
    echo "${TERM_TEXT_RED}ERROR:${TERM_TEXT_RESET} $1" 1>&2
}

# Usage: die message
function die {
    error "$1"
    exit 1
}

# Usage: check_command command-name error-message
function check_command {
    if ! hash "$1"; then
      die "$2"
    fi
}

say "Setting up dev environment in $(emph $ROOT)..."

# Virtualenv setup
check_command python3 "Python 3 not found"

if [[ ! -d "$ROOT/venv" ]]; then
    say "Creating Python virtual environment..."
    python3 -m venv --prompt "THAvalon" "$ROOT/venv"
fi

say "Activating virtual environment..."
if [[ ! -d "$ROOT/venv" ]]; then
  die "Virtualenv does not exist"
fi
source "$ROOT/venv/bin/activate"
say "Using $(emph $(which python)) and $(emph $(which pip))"

say "Updating Pip in the virtual environment..."
pip install -U pip

say "Installing Pipenv in the virtual environment..."
pip install pipenv

say "Installing Python dependencies..."
pipenv install -d

# Frontend setup

# check_command yarn "Yarn is not installed, see $(emph https://yarnpkg.com/lang/en/docs/install)"

# say "Installing frontend dependencies..."
# yarn install

check_command direnv "Direnv is not installed, see $(emph https://direnv.net)"
direnv allow

say "Done!"