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

    office.left = lounge
    
    lounge.prev = office
    lounge.left = kitchen
    lounge.right = master_bedroom
    
    master_bedroom.prev = lounge
    
    kitchen.prev = lounge
    
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
    info_text = {"wardrobe_Low_Anxiety": [["There is a book about poisons"], "Audios\Impact.wav", (0.0, 0.0, -5.0)],
                     "wardrobe_High_Anxiety": [["There is nothing"], "Audios\Teclado.wav", ()],
                     "bed": [["There is nothing"], "Audios\Teclado.wav", ()],
                     "bed2": [["There is a blood stain on the sheet"], "Audios\Impact.wav", ()],
                     "letter": [["The morning of September 23, 1954, will be remembered as a day of unspeakable tragedy", "The lifeless body of Natally Stradel, Duchess of London, was found in her bedroom, dressed in the same gown she had worn the previous night to the welcome party of Count Magus Artis", "The absence of her husband, Duke Marcos Stephan, who was away on a business trip, has raised a series of unanswered questions", "The butler and his wife, who were the only ones present in the house at the time of the incident, claim to have heard nothing unusual during the night", "However, the lack of any signs of force or injury on the Duchess's body suggests that the crime may have been committed with a subtlety and cunning that defies imagination", "The investigation, which has only just begun, has failed to find the murder weapon, adding to the sense of mystery and confusion surrounding this case", "The question on everyone's mind is: who could have committed such a heinous crime, and how did they do it without leaving a trace?", "The police are working tirelessly to solve this enigma, but for now, the case of the Duchess of London's death remains a mystery that challenges the brightest mind"], "Audios\Teclado.wav", ()],
                     "furniture": [["There is nothing"], "Audios\Teclado.wav", ()],
                     "drawers1" : [["At first you didn't find anything weird, ", "but looking further you found a small syringe."], "Audios\Impact.wav", (0.0, 0.0, -5.0)],
                     "drawers2" : [["There is nothing out of the ordinary"], "Audios\Teclado.wav", ()],
                     "groceries1" : [["You had to use your magnifying glass", "to find some small holes in the fruits."], "Audios\Impact.wav", (0.0, 0.0, -5.0)],
                     "groceries2" : [["There is nothing out of the ordinary"], "Audios\Teclado.wav", ()],
                     "glass1" : [["The bottle that fell has a strong chemical smell and a silver color."], "Audios\Impact.wav", (0.0, 0.0, -5.0)],
                     "glass2": [["There is nothing out of the ordinary, just a break bottle"], "Audios\Teclado.wav", ()],
                     "closet1": [["Searching through each pocket of Count Magus Artis's suits you found a receipt from ", "Chemical Stores", "which only had one item ", "The same as always"], "Audios\Impact.wav", (0.0, 0.0, -5.0)],
                     "closet2" : [["There is nothing out of the ordinary"], "Audios\Teclado.wav", ()],
                     "body1" : [["You searched too well but just as the first police report said,"
                                 ," there are no marks on the body of violent death or any type of injury,"
                                 ,"there are no apparent signs of homicide."] , "Audios\Impact.wav", (0.0, 0.0, -5.0)]   
                     }
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
            try:
                choice = int(input("Choose an option: "))  # Pedimos la opción y la convertimos a entero
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")  # Si no se puede convertir a entero, mostramos un mensaje
                time.sleep(1)  # Pausa breve para que el usuario pueda ver el mensaje
                continue  # Volvemos al inicio del bucle
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
    if current.name == "The Lounge":
        text = [[["Behind of you is the door to get the Office."], "Audios\Door.wav", (0.0, 0.0, 5.0)],
                [["In the center of lounge there are three pieces of furniture", "and a center table."], "Audios\Teclado.wav", (0.0, 0.0, 0.0)]]
        while True:
            clear_screen()
            print("**************")
            print("LOUNGE MENU")
            print("**************")
            current_area(current)
            protagonist.show_anxiety()
            print("1. Check Tools\n2. Inventory\n3. Look around\n4. Investigate furniture\n0. Back menu")
            try:
                choice = int(input("Choose an option: "))  # Pedimos la opción y la convertimos a entero
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")  # Si no se puede convertir a entero, mostramos un mensaje
                time.sleep(1)  # Pausa breve para que el usuario pueda ver el mensaje
                continue  # Volvemos al inicio del bucle
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
                show_dialog(info_text["furniture"])
                protagonist.setAnxiety(12)
    if current.name == "The Kitchen":
        text = [[["Behind of you is the door to get the Lounge."], "Audios\Door.wav", (0.0, 0.0, 5.0)],
                [["On the left side there are several drawers"], "Audios\Wood.wav", (-5.0, 0.0, 0.0)],
                [["On the right side there are groceries."], "Audios\Teclado.wav", (5.0, 0.0, 0.0)],
                [["A glass has just fallen at your left"], "Audios\Glass.wav", (-5.0, 0.0, 0.0)]]
        while True:
            clear_screen()
            print("**************")
            print("KITCHEN MENU")
            print("**************")
            current_area(current)
            protagonist.show_anxiety()
            print("1. Check Tools\n2. Inventory\n3. Look around\n4. Investigate drawers\n5. Investigate groceries\n6. Investigate the glass sound\n0. Back menu")
            try:
                choice = int(input("Choose an option: "))  # Pedimos la opción y la convertimos a entero
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")  # Si no se puede convertir a entero, mostramos un mensaje
                time.sleep(1)  # Pausa breve para que el usuario pueda ver el mensaje
                continue  # Volvemos al inicio del bucle
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
                #drawers
                if protagonist.getAnxiety() < 20:
                    show_dialog(info_text["drawers1"])
                    protagonist.setAnxiety(5)
                else:
                    show_dialog(info_text["drawers2"])
                    protagonist.setAnxiety(15)
                time.sleep(3)
            elif choice == 5:
                #groceries
                if protagonist.getAnxiety() < 20:
                    show_dialog(info_text["groceries1"])
                    protagonist.setAnxiety(5)
                else:
                    show_dialog(info_text["groceries2"])
                    protagonist.setAnxiety(15)
                time.sleep(3)
            elif choice == 6:
                #glass
                if protagonist.getAnxiety() < 40:
                    show_dialog(info_text["glass1"])
                    protagonist.setAnxiety(5)
                else:
                    show_dialog(info_text["glass2"])
                    protagonist.setAnxiety(15)
                time.sleep(3)
    if current.name == "The Master Bedroom":
        text = [[["Behind of you is the door to get the lounge."], "Audios\Door.wav", (0.0, 0.0, 5.0)],
                [["In the middle of the room is ", "the lifeless body of Natally Stradel"], "Audios\Impact.wav", (0.0, 0.0, 5.0)],
                [["On the left side there the closet"], "Audios\Wood.wav", (-5.0, 0.0, 0.0)],
                [["On the right side there is the bed."], "Audios\Teclado.wav", (5.0, 0.0, 0.0)]
        ]
        while True:
            clear_screen()
            print("**************")
            print("MASTER BEDROOM MENU")
            print("**************")
            current_area(current)
            protagonist.show_anxiety()
            print("1. Check Tools\n2. Inventory\n3. Look around\n4. Investigate the lifeless body of Natally Stradel\n5. Investigate closet\n6. Investigate the bed\n0. Back menu")
            try:
                choice = int(input("Choose an option: "))  # Pedimos la opción y la convertimos a entero
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")  # Si no se puede convertir a entero, mostramos un mensaje
                time.sleep(1)  # Pausa breve para que el usuario pueda ver el mensaje
                continue  # Volvemos al inicio del bucle
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
                #Natally Stradel
                show_dialog(info_text["body1"])
                protagonist.setAnxiety(15)
                
                time.sleep(3)
            elif choice == 5:
                #closet
                if protagonist.getAnxiety() < 20:
                    show_dialog(info_text["closet1"])
                    protagonist.setAnxiety(5)
                else:
                    show_dialog(info_text["closet2"])
                    protagonist.setAnxiety(15)
                time.sleep(3)
            elif choice == 6:
                #bed
                if protagonist.getAnxiety() < 40:
                    show_dialog(info_text["bed"])
                    protagonist.setAnxiety(5)
                else:
                    show_dialog(info_text["bed2"])
                    protagonist.setAnxiety(15)
                time.sleep(3)
    
        
    return protagonist
