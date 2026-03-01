#!/bin/bash

# airmon
if ! command -v airmon-ng &> /dev/null
then
    echo "[*] Installing aircrack-ng ... "
    sudo apt update
    sudo apt install -y aircrack-ng

fi

#Python
if ! command -v python3 &> /dev/null
then
    sudo apt update
    sudo apt install -y python3

fi

# pip
if ! command -v pip3 &> /dev/null
then
    sudo apt install -y python3-pip

fi

#venv
if [ ! -d "venv" ]; then
    python3 -m venv venv

fi

# Active VENV
source venv/bin/activate

# install python requirements
pip install -r requirements.txt > /dev/null 2>&1

# START
python3 main.py

#OFF
deactivate