import json
# import Enemy_Player_classes
import time #dodanie odstepu pomiedzy wiadomosciami

from PlayerClass import Player
from EnemyClass import Enemy
from GameClass import Game

def main():
    with open('Constructor.json', 'r') as file:
        map_data = json.load(file)

    game = Game(map_data)
    game.new_save()
    game.load_save(1)
    save = game.player_loader()
    # player = Enemy_Player_classes.Player(6, 0, 2)
    player = Player(save[0], save[1], save[2])

    while True:
        game.print_current_location()
        action = input("What do you want to do? (move/player stats/attack/show details/save/exit): ").lower().strip()
        if action == "move":
            direction = input("Choose your next move (north/east/south/west): ").lower().strip()
            game.move(direction)
        elif action == "show details":
            game.current_location.show_details()
        elif action == "exit":
            print("Exiting the game. Goodbye!")
            break
        elif action == "save":
            game.save_the_game(player)
        elif action == "player stats":
            player_heart = player.health
            player_armour = player.armour
            player_damage = player.damage
            player_gold = player.gold
            print("player stats:")
            print(f"Heart: {player_heart}")
            print(f"Armour: {player_armour}")
            print(f"Damage: {player_damage}")
            print(f"Gold: {player_gold}")
            pom_string=""
            for item in player.eq:
                pom_string=pom_string+item["name"]+" "
                
            print(f"Equipment: {pom_string}")
        elif action == "attack":

            enemies = game.get_enemies_in_current_location()
            # być moze lepszym pomyslem bedzie stworzenie metody Game::Get_Current_Location() bo Location ma metode get_enemies()
            if not enemies:
                print("There is no one to attack.")
                time.sleep(0.5)
                continue
            stringer_helper = ""
            for enemy in enemies:
                stringer_helper = stringer_helper + str(enemy) + ", "

            action = input(f"choose what enemy you will attack ({stringer_helper[:-2]}) or go back: ").strip()

            # gracz wybrał poprawnego przeciwnika
            if action in enemies:
                # Game::Fight() jako argument potrzebuje obiektu przeciwnika, a LOCATION zawiera tylko słownik z danymi przeciwnika a nie obiekt
                # dlatego musimy stworzyć obiekt przeciwnika na podstawie danych z mapy
                enemy_index = enemies.index(action)
                enemy_data = game.current_location.enemies[enemy_index]
                if "eq" in enemy_data and enemy_data["eq"] != "":
                    enemyObj = Enemy(enemy_data["name"], enemy_data["hp"], enemy_data["dmg"], enemy_data["eq"])
                else:
                    enemyObj = Enemy(enemy_data["name"], enemy_data["hp"], enemy_data["dmg"], None)

                game.fight(player, enemyObj)
                
            elif action == "go back":
                pass
            else:
                print("Invalid action. Try again.")
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    main()
