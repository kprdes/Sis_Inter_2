# main.py

from mapa import create_map, check_locations, move_player, current_area, investigate_area
from player import Player
from utilities import show_dialog, clear_screen
import os
import time
from openal import *

def vote():
    clear_screen()
    text = {"begin":[["At this moment you are going to give your verdict as an investigator,",
                        "your life depends on it, so it is advisable"
                            ,"that you investigate all areas thoroughly."],"Audios\Teclado.wav", (0.0, 0.0, 5.0)],
            "butler" : [["That could be true, but he claims not,",
                        "because of your accusation he was locked up and developed so much hatred for you"
                        , "that he paid a hitman to take your life, and so he did.", "You have lost."],"Audios\Impact.wav", (0.0, 0.0, 5.0)],
            "butler wife" : [["Everything points to it being her, the evidence is not very solid",
                            "and because of her imprisonment the butler developed a great hatred towards you,",
                            "for that reason he killed you with his own hands.",
                            "You have lost."], "Audios\Impact.wav", (0.0, 0.0, 5.0)],
            "Count" : [["Because of your accusation, the count lost all his reputation",
                        "and ended up taking his own life in his cell."
                        "You have lost"],"Audios\Impact.wav", (0.0, 0.0, 5.0)],
            "No one" : [["You failed to find out who did it,",
                            "you ended up losing all your reputation as a detective",
                            "and you took your own life.",
                            "You have lost"],"Audios\Impact.wav", (0.0, 0.0, 5.0)],
            "Everyone" : [["Your excellent skills realized that Count Magus Artis had been buying a strong chemical",
                            "for a long time thanks to the invoice you found in his pocket,",
                            "the wife of the employee who was in charge of being in the kitchen injected this strong chemical",
                            "into each food and the butler was in charge of serving it especially to Mrs. Natally Stradel.",
                            "They were all involved in the murder of the lady,",
                            "each for personal reasons that coincided to kill her,",
                            "Mrs. Natally Stradel had begun to secretly meet with the daughter of her butlers",
                            "to consume opium and sleep with other men,",
                            "this made everyone develop a special hatred for her and began a slow and silent murder with mercury",
                            "\n\nYou discovered the killers, excellent last case"], "Audios\Impact.wav", (0.0, 0.0, 5.0)]
    }
    show_dialog(text["begin"])
    time.sleep(3)
    clear_screen()
    print("**************")
    print("MAIN MENU")
    print("**************")
    print("You are going to claim that: \n1. The butler did it\n2. The butler's wife did it\n3. Count Magus Artis did it\n4. The person who did it is not present\n5. Everyone in this list did it\n0. I am not sure")
    choice = int(input())
    if choice == 1:
        show_dialog(text["butler"])
        time.sleep(3)
        exit(0)
    if choice == 2:
        show_dialog(text["butler wife"])
        time.sleep(3)
        exit(0)
    if choice == 3:
        show_dialog(text["Count"])
        time.sleep(3)
        exit(0)
    if choice == 4:
        show_dialog(text["No one"])
        time.sleep(3)
        exit(0)
    if choice == 5:
        show_dialog(text["Everyone"])
        time.sleep(3)
        exit(0)


def main():
    clear_screen()
    initial_dialogue = [[
        "Welcome to The Last Job.",
        "The game where your survival depends on the decisions you make as a detective...",
        "Sir Thomas Romanov is a successful detective with excellent skills...",
        "Your survival in this task depends on making the right decisions.",
        "Good luck.",
        "Press 1 to start",
        "Press 2 if you're not ready yet."
    ], "Audios\Teclado.wav", (0.0, 0.0, 0.0)]

    show_dialog(initial_dialogue)

    new_game = int(input())
    if new_game == 2:
        exit(0)
    
    clear_screen()

    letter_dialogue = [[
        "London, England. September 23, 1954.",
        "Sir Thomas Romanov, your services are requested...",
        "The scene is presumably untouched...",
        "Sincerely,",
        "Colonel of the police Gregory Smith."], "Audios\Teclado.wav", (0.0, 0.0, 0.0)]

    show_dialog(letter_dialogue)

    print("\n\n**The letter has been saved in your pocket**\n\n")
    time.sleep(3)
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
        print("1. Check Tools\n2. Inventory\n3. Investigate current area\n4. Move\n5. Say who did it\n0. Surrender")
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
            protagonist.anxiety = protagonist.anxiety + 5
        elif choice == 5:
            vote()


if __name__ == "__main__":
    main()
