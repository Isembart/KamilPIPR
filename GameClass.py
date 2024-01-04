import json
from LocationClass import Location
import random
import os
import shutil
import time
from PlayerClass import Player

from PlayerClass import Player #potrzebne aby stworzyc logike walki
from EnemyClass import Enemy #potrzebne aby stworzyc logike walki
import time #dodanie odstepu pomiedzy wiadomosciami podczas walki

from delayedPrint import delayedPrint

def fightEnemyTurn(player, enemy):
    #Przeciwnik atakuje gracza
    delayedPrint(f"{enemy.name} attacks you for {enemy.dmg} damage!")
    player.take_damage(enemy.dmg)
    time.sleep(0.5)
    if not player.is_alive():
        delayedPrint("You are dead!")
        exit(0)

class Game:
    def __init__(self, map_data):
        self.locations = [Location(location_data) for location_data in map_data["Locations"]]
        self.i = len(os.listdir(os.path.dirname(__file__)+"\\saves"))
        
        
    
    def new_save(self):
        newSave = os.path.dirname(__file__)+"\\saves\\save"+str(self.i)+".json"
        shutil.copy("Constructor.json", newSave)
        self.current_save = newSave

    def load_save(self, number: int):
        self.current_save = os.path.dirname(__file__)+"\\saves\\save"+str(number)+".json"

    def save_the_game(self, player, fight=True, enemy=None):
        with open(self.current_save, "r") as file:
            save = json.load(file)
        save["player"]["armour"] = player.armour
        save["player"]["health"] = player.health
        save["player"]["damage"] = player.damage
        save["player"]["eq"] = player.eq
        save["player"]["current location"] = self.current_location_name

        if fight:
            i=0
            for x in save["Locations"]:
                if x["Name"] == self.current_location_name:
                    ii = 0
                    for y in x["Enemies"]:
                        if y["name"] == enemy.name:
                            break
                        ii+=1
                    break
                i+=1
            save["Locations"][i]["Enemies"][ii]["hp"] = 0
            


        with open(self.current_save, "w") as file:
            json.dump(save, file)
        print("Game was saved")


    def player_loader(self):
        with open(self.current_save, "r") as file:
            save = json.load(file)
        player = save["player"]
        self.current_location = self.get_location(player["current location"])
        self.current_location_name = player["current location"]
        health = player["health"]
        armour = player["armour"]
        damage = player["damage"]
        eq = player["eq"]
        return [health, armour, damage, eq]

    def get_location(self, location_name):
        for location in self.locations:
            if location.name.lower() == location_name.lower():
                return location
        return None

    def print_current_location(self):
        delayedPrint(self.current_location.get_description())

    def move(self, direction):
        next_location_name = self.current_location.near_locations.get(direction)
        if next_location_name:
            next_location = self.get_location(next_location_name)
            if next_location:
                self.current_location = next_location
                self.current_location_name = next_location.name
                delayedPrint(f"You moved to {next_location.name} \n")
            else:
                delayedPrint("Invalid location.")
        else:
            delayedPrint("Invalid move. Try again.")

    def get_enemies_in_current_location(self):
        return self.current_location.get_enemies()

    def fight(self, player, enemy):
        while True:
            delayedPrint(f"Your HP:{player.health}\nEnemy HP:{enemy.hp}\n")
            action = input(f"Run or Attack?").strip().lower()
            if(action == "attack"):
                #Gracz atakuje przeciwnika:
                enemy.take_damage(player.damage)
                delayedPrint(f"You deal {player.damage} damage to {enemy.name}")
                time.sleep(0.5)
                if not enemy.is_alive():
                    delayedPrint(f"You felled {enemy.name}!") 
                    # check if enemy's eq is not empty
                    if enemy.eq:
                        # if not, add it to player's eq
                        for item in enemy.eq:
                            player.eq.append(item)
                            delayedPrint(f"You found {item['name']}!")
                            time.sleep(0.5)
                    self.save_the_game(player, True, enemy)
                    #wychodzimy z funkcji bo przeciwnik umarł i nie będzie już atakować gracza
                    return  

                fightEnemyTurn(player, enemy)
                
            
            if(action == "run"):
                #Gracz ucieka z walki
                player_chance = random.randint(0,10)
                if player_chance > 5:
                    delayedPrint("You run away!")    
                    break
                        
                delayedPrint("You dont run away!") 
                fightEnemyTurn(player, enemy)





