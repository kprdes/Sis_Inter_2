# main.py

from mapa import create_map, check_locations, move_player, current_area, investigate_area
from player import Player
from utilities import show_dialog, clear_screen
import os
import time
from openal import *

def main():

    clear_screen()
    protagonist = Player()
    main_map = create_map()
    current_location = main_map

    clear_screen()

    while True:
        clear_screen()
        print("**************")
        print("MAIN MENU")
        print("**************")
        current_area(current_location)
        source = oalOpen("Audios\Office.wav")
        source.set_looping(True)  
        source.play()
        protagonist.show_anxiety()
        print("1. Check Tools\n2. Inventory\n3. Investigate current area\n4. Move\n0. Surrender")
        choice = int(input())
        if choice == 0:
            exit(0)
        elif choice == 1:
            protagonist.tool_status()
        elif choice == 2:
            protagonist.show_inventory()
        elif choice == 3:
            protagonist = investigate_area(current_location, protagonist)
            time.sleep(2)
        elif choice == 4:
            clear_screen()
            check_locations(current_location)
            new_location = int(input("Enter the number of the option you want to perform: "))
            current_location = move_player(current_location, new_location)

if __name__ == "__main__":
    main()
