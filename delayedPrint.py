import time
import random

def delayedPrint(text):
    for letter in text:
        # end="" sprawia że delayedPrint nie kończy się nową linia
        # flush=True pozwala wyświetlać po jednej literce
        print(letter, end="", flush=True)
        if( letter == " "):
            time.sleep(random.randint(5, 20) / 1000)
            continue
        time.sleep(random.randint(1, 10) / 1000)
    print() #dodanie nowej linii po zakonczeniu delayedPrint
