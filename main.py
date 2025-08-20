#!/usr/bin/env python3
import google.generativeai as genai
import os
import time

# ANSI цвета
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"

# Путь к конфигу
CONFIG_PATH = os.path.expanduser("~/.cli-gemini/api.conf")

# Читаем API ключ
if not os.path.exists(CONFIG_PATH):
    print(f"{RED}[Ошибка]{RESET} API ключ не найден.")
    print(f"Создай файл {CYAN}{CONFIG_PATH}{RESET} и вставь туда свой ключ (одной строкой).")
    print("Как получить ключ: https://aistudio.google.com/app/apikey")
    exit(1)

with open(CONFIG_PATH, "r") as f:
    api_key = f.read().strip()

if not api_key.startswith("AIza"):
    print(f"{RED}[Ошибка]{RESET} В конфиге неправильный ключ!")
    exit(1)

# Настройка
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# История чата
chat_history = [
    {"role": "user", "parts": ["Ты — дружелюбный собеседник. Отвечай человечно, кратко и понятно."]}
]

print(f"{GREEN}Gemini started! type 'exit' to stop Gemini.{RESET}")

while True:
    try:
        user_input = input(f"{CYAN}You > {RESET}")
        if user_input.lower() in ["exit", "quit"]:
            print(f"{RED}Exiting...{RESET}")
            break

        chat_history.append({"role": "user", "parts": [user_input]})

        response = model.generate_content(chat_history)
        reply = response.text

        print(f"{GREEN}Gemini > {reply}{RESET}")

        chat_history.append({"role": "model", "parts": [reply]})

    except Exception as e:
        print(f"{RED}Ошибка:{RESET}", e)
        time.sleep(2)
