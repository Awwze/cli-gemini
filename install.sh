#!/bin/bash

set -e

echo "[+] Installing dependencies..."
pip install --upgrade google-generativeai

mkdir -p ~/.cli-gemini

if [ ! -f ~/.cli-gemini/api.conf ]; then
    echo "[!] File api.conf not found"
    echo "Paste your API key (one line)" > ~/.cli-gemini/api.conf
    echo "[+] Now open ~/.cli-gemini/api.conf and paste your API key."
fi

chmod +x main.py

sudo ln -sf "$(pwd)/main.py" /usr/local/bin/cli-gemini

echo "[+] Installed!"
echo "You can run: cli-gemini"
