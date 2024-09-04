# map.py
from player import Player
import os
import time
from utilities import show_dialog, clear_screen
from openal import *

class Map:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.left = None
        self.right = None
        self.key = 0

def create_map():
    office = Map("The Office")
    lounge = Map("The Lounge")
    kitchen = Map("The Kitchen")
    master_bedroom = Map("The Master Bedroom")
    butlers_room = Map("The Butler's Room")
    basement = Map("The Basement")
    stable = Map("The Stable")

    office.left = lounge
    
    lounge.prev = office
    lounge.left = kitchen
    lounge.right = master_bedroom
    
    master_bedroom.prev = lounge
    master_bedroom.left = stable
    
    kitchen.prev = lounge
    kitchen.left = butlers_room
    
    butlers_room.prev = kitchen
    butlers_room.left = basement
    butlers_room.right = stable
    
    stable.prev = butlers_room
    stable.left = master_bedroom
    
    basement.prev = butlers_room
    
    return office

def check_locations(current):
    print("You can move to:\n")
    counter = 1
    print("0. I don't want to move.\n")
    if current.prev:
        current.prev.key = counter
        print(f"{counter}. {current.prev.name}\n")
        counter += 1
    if current.right:
        current.right.key = counter
        print(f"{counter}. {current.right.name}\n")
        counter += 1
    if current.left:
        current.left.key = counter
        print(f"{counter}. {current.left.name}\n")
        counter += 1

def move_player(current, key):
    if key == 0:
        return current
    if key == 1:
        if current.prev and current.prev.key == 1:
            return current.prev
        if current.right and current.right.key == 1:
            return current.right
        if current.left and current.left.key == 1:
            return current.left
    elif key == 2:
        if current.prev and current.prev.key == 2:
            return current.prev
        if current.right and current.right.key == 2:
            return current.right
        if current.left and current.left.key == 2:
            return current.left
    elif key == 3:
        if current.prev and current.prev.key == 3:
            return current.prev
        if current.right and current.right.key == 3:
            return current.right
        if current.left and current.left.key == 3:
            return current.left
    print("\n\nInvalid value entered\n\n")
    return current

def current_area(current):
    print(f"\nYou are currently in: {current.name}\n")

def investigate_area(current, protagonist):
    info_text = {"wardrobe_Low_Anxiety": [["There is a book about poisons"], "Audios\Teclado.wav", ()],
                     "wardrobe_High_Anxiety": [["There is nothing"], "Audios\Teclado.wav", ()],
                     "bed": [["There is nothing"], "Audios\Teclado.wav", ()],
                     "bed2": [["There is a blood stain on the sheet"], "Audios\Teclado.wav", ()],
                     "letter": [["The morning of September 23, 1954, will be remembered as a day of unspeakable tragedy", "The lifeless body of Natally Stradel, Duchess of London, was found in her bedroom, dressed in the same gown she had worn the previous night to the welcome party of Count Magus Artis", "The absence of her husband, Duke Marcos Stephan, who was away on a business trip, has raised a series of unanswered questions", "The butler and his wife, who were the only ones present in the house at the time of the incident, claim to have heard nothing unusual during the night", "However, the lack of any signs of force or injury on the Duchess's body suggests that the crime may have been committed with a subtlety and cunning that defies imagination", "The investigation, which has only just begun, has failed to find the murder weapon, adding to the sense of mystery and confusion surrounding this case", "The question on everyone's mind is: who could have committed such a heinous crime, and how did they do it without leaving a trace?", "The police are working tirelessly to solve this enigma, but for now, the case of the Duchess of London's death remains a mystery that challenges the brightest mind"], "Audios\Teclado.wav", ()]}
    if current.name == "The Office":
        text = [[["In front of you is the door to exit."], "Audios\Door.wav", (0.0, 0.0, -5.0)], [["To your right, there is a wardrobe."], "Audios\Wood.wav", (5.0, 0.0, 0.0)], [["Behind you, there is a bed."], "Audios\Teclado.wav", ()], [["In your hands is the letter that explains what happened."], "Audios\Teclado.wav", ()]]
        while True:
            clear_screen()
            print("**************")
            print("OFFICE MENU")
            print("**************")
            current_area(current)
            protagonist.show_anxiety()
            print("1. Check Tools\n2. Inventory\n3. Look around\n4. Investigate wardrobe\n5. Read the letter\n0. Back menu")
            choice = int(input())
            if choice == 0:
                return protagonist
            elif choice == 1:
                protagonist.tool_status()
            elif choice == 2:
                protagonist.show_inventory()
            elif choice == 3:
                for i in text:
                    show_dialog(i)
                time.sleep(1)
            elif choice == 4:
                if protagonist.getAnxiety() < 40:
                    show_dialog(info_text["wardrobe_Low_Anxiety"])
                else:
                    show_dialog(info_text["wardrobe_High_Anxiety"])
                time.sleep(3)
            elif choice == 5:
                clear_screen()
                show_dialog(info_text["letter"])
                protagonist.setAnxiety(5)
                time.sleep(3)
    #if current.name == "The Lounge":
    
"""
    lounge = Map()
    kitchen = Map("The Kitchen")
    master_bedroom = Map("The Master Bedroom")
    butlers_room = Map("The Butler's Room")
    basement = Map("The Basement")
    stable = Map("The Stable")
"""
