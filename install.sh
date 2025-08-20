#!/bin/bash

set -e

# Установка зависимостей
echo "[+] Installing dependencies..."
pip install --upgrade google-generativeai

# Создаём папку для конфига
mkdir -p ~/.cli-gemini

# Создаём пустой конфиг если его нет
if [ ! -f ~/.cli-gemini/api.conf ]; then
    echo "[!] File api.conf not found"
    echo "Paste your API key (one line)" > ~/.cli-gemini/api.conf
    echo "[+] Now open ~/.cli-gemini/api.conf and paste your API key."
fi

# Делаем исполняемым
chmod +x main.py

# Линкуем в /usr/local/bin
sudo ln -sf "$(pwd)/main.py" /usr/local/bin/cli-gemini

echo "[+] Installed!"
echo "You can run: cli-gemini"
