import time
import random
from pynput import keyboard  # wykrywanie wcisniecia jednoczesnie z wypisywaniem tekstu
import threading  # wykrywanie wcisniecia jednoczesnie z wypisywaniem tekstu

# Event to indicate if a key has been pressed
key_pressed = threading.Event()

# Funkcja sprawdzająca czy został wciśnięty jakiś klawisz
def on_press(key):
    key_pressed.set()

# Funkcja, która umożliwia pojawianie się liter po kolei
def delayedPrint(text):
    key_pressed.clear()
    with keyboard.Listener(on_press=on_press, suppress=True) as listener:  # suppress key presses

        for letter in text:
            # end="" sprawia że delayedPrint nie kończy się nową linia
            # flush = True pozwala wyświetlać po jednej literce
            print(letter, end="", flush=True)
            if (letter == " "):
                time.sleep(random.randint(5, 20) / 1000)
                continue
            if not key_pressed.wait(timeout=random.randint(1, 10) / 1000):  # wait for a key press or timeout
                continue

            # Check if any key is pressed
            print(text[text.index(letter)+1:], end="", flush=True)  # print the rest of the text
            break  # exit the loop

        print()  # dodanie nowej linii po zakonczeniu delayedPrint