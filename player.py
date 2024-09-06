# player.py

import time

class Player:
    def __init__(self):
        self.name = "Thomas Romanov"
        self.anxiety = 15
        self.magnifying_glass = True
        self.flashlight = True
        self.cigarettes = 7
        self.gun_name = "Smith & Wesson Model 10"
        self.current_bullets = 6
        self.spare_bullets = 4
        self.clue_count = 0
        self.batteries = 1

    def tool_status(self):
        if self.magnifying_glass:
            print("\nThe magnifying glass is in good condition")
        if self.flashlight:
            print("\nThe flashlight still has batteries\n")
        time.sleep(2)

    def show_anxiety(self):
        if self.anxiety >= 0 and self.anxiety < 20:
            print("Low level of anxiety")
        elif self.anxiety >= 20 and self.anxiety < 60:
            print("Moderate level of anxiety")
        elif self.anxiety >= 60:
            print("High level of anxiety")
        print("\n")

    def show_inventory(self):
        print("You currently have in your possession:\n")
        if self.current_bullets > 0:
            print(f"You have {self.current_bullets} bullets in your {self.gun_name}")
        if self.spare_bullets > 0:
            print(f"You have {self.spare_bullets} spare bullets")
        if self.cigarettes > 0:
            print(f"You have {self.cigarettes} cigarettes")
        if self.batteries > 0:
            print(f"You have {self.batteries} battery/batteries for the flashlight")

        num = int(input("\nWhat would you like to do?\n\n1. Smoke a cigarette\n2. Reload the gun\n3. Change the flashlight battery\n4. Nothing\n"))
        if num == 1:
            print("\n**You smoked a cigarette**")
            self.anxiety = 0
            self.cigarettes -= 1
            time.sleep(2)
        elif num == 2:
            if self.current_bullets == 6:
                print("\nNo need to reload the gun")
            elif self.current_bullets < 6:
                while self.current_bullets < 6 and self.spare_bullets > 0:
                    self.current_bullets += 1
                    self.spare_bullets -= 1
                print("\n**You have reloaded the gun**")
            elif self.spare_bullets == 0:
                print("\nYou don't have enough bullets to reload the gun")
            time.sleep(2)
        elif num == 3:
            if self.batteries != 0:
                self.flashlight = True
                self.batteries -= 1
                print("\n**You changed the flashlight batteries**")
            else:
                print("\nYou don't have enough batteries to change")
            time.sleep(2)

    def setAnxiety(self, NewValue):
        self.anxiety = self.anxiety + NewValue

    def getAnxiety(self):
        return self.anxiety