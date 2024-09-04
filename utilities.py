import os
import time
from openal import *

def show_dialog(dialogue_data):
    dialogue, audio, position = dialogue_data

    # Primero reproducimos el sonido de teclado
    source = oalOpen("Audios\Teclado.wav")
    source.set_looping(True)
    source.play()

    try:

        for line in dialogue:
            for letter in line:
                print(letter, end='', flush=True)
                time.sleep(0.035)
            time.sleep(0.4)
            print("\n")
    finally:
        source.stop() 

    if audio != "Audios\Teclado.wav":
        extra_source = oalOpen(audio)
        extra_source.set_position(position)
        extra_source.play()

        while extra_source.get_state() == AL_PLAYING:
            time.sleep(0.1)  

        extra_source.stop()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

