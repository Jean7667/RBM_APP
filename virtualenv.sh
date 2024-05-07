#!/bin/bash

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs

echo "Activating virtual environment..."
source ~/.local/bin/virtualenvwrapper.sh
workon rbm_app_3.12_virt_env
