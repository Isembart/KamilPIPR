import time
import random
import keyboard  # wykrywanie klawiszy
import threading  # wykrywanie wcisniecia jednoczesnie z wypisywaniem tekstu

# Global flag to indicate if a key has been pressed
key_pressed = False

# Funkcja sprawdzająca czy został wciśnięty jakiś klawisz
def listen_for_keypress():
    global key_pressed
    keyboard.read_hotkey(suppress=True) # suppress = wcisniety klawisz nie zostanie wpisany do terminala
    key_pressed = True

# Funkcja, która umożliwia pojawianie się liter po kolei
def delayedPrint(text):
    global key_pressed
    key_pressed = False
    listener = threading.Thread(target=listen_for_keypress)
    listener.start()

    for letter in text:
        # end="" sprawia że delayedPrint nie kończy się nową linia
        # flush = True pozwala wyświetlać po jednej literce
        print(letter, end="", flush=True)
        if (letter == " "):
            time.sleep(random.randint(5, 20) / 1000)
            continue
        time.sleep(random.randint(1, 10) / 1000)

        # jesli gracz nacisnał klawisz, przerwij pisanie i wyswietl caly napis od razu
        if key_pressed:  
            print(text[text.index(letter)+1:], end="", flush=True)  
            break 

    print()  # dodanie nowej linii po zakonczeniu delayedPrint