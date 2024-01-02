import json
import Enemy_Player_classes


class Location:
    def __init__(self, location_data):
        self.id = location_data["Id"]
        self.name = location_data["Name"]
        self.items = location_data["Item"]
        self.allies = location_data["Allies"]
        self.enemies = location_data["Enemies"]
        self.seen = location_data["Seen"]
        self.near_locations = location_data["Near"]
        self.description = location_data["Description"] if "Description" in location_data else []

    def __str__(self):
        return f"{self.name}\nDescription: \n{''.join(desc['description'] for desc in self.description)}"

    def show_details(self):
        print(f"\n{self.name} Details:")
        print("Items:")
        for item in self.items:
            print(f"- {item['name']}")
        print("Allies:")
        for ally in self.allies:
            print(f"- {ally['name']}")
        print("Enemies:")
        for enemy in self.enemies:
            print(f"- {enemy['name']}")
            print(f"hp - {enemy['hp']}")
            print(f"dmg - {enemy['dmg']}")
            print(f"eq - {enemy['eq']}")

    def get_description(self):
        return f"{self.name}\nDescription: \n{' '.join(desc['description'] for desc in self.description)}"

    def get_enemies(self):
        return [x["name"] for x in self.enemies]


class Game:
    def __init__(self, map_data):
        self.locations = [Location(location_data) for location_data in map_data["Locations"]]
        self.current_location = self.get_location("Elven Valley")

    def get_location(self, location_name):
        for location in self.locations:
            if location.name.lower() == location_name.lower():
                return location
        return None

    def print_current_location(self):
        print(self.current_location.get_description())

    def move(self, direction):
        next_location_name = self.current_location.near_locations.get(direction)
        if next_location_name:
            next_location = self.get_location(next_location_name)
            if next_location:
                self.current_location = next_location
                print("You moved to", next_location.name, "\n")
            else:
                print("Invalid location.")
        else:
            print("Invalid move. Try again.")

    def Print_Enemies(self):
        return self.current_location.get_enemies()


def main():
    with open('Constructor.json', 'r') as file:
        map_data = json.load(file)

    game = Game(map_data)
    player = Enemy_Player_classes.Player(6, 0, 2)
    while True:
        game.print_current_location()
        action = input("What do you want to do? (move/player stats/attack/show details/exit): ").lower()
        if action == "move":
            direction = input("Choose your next move (north/east/south/west): ").lower()
            game.move(direction)
        elif action == "show details":
            game.current_location.show_details()
        elif action == "exit":
            print("Exiting the game. Goodbye!")
            break
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
        elif action == "attack":
            '''for enemy in game.Print_Enemies():
                    print(f"- {enemy}")'''
            stringer_helper = ""
            for x in game.Print_Enemies():
                stringer_helper = stringer_helper + str(x) + ", "
            action = input(f"choose what enemy you will attack ({stringer_helper[:-2]}) or go back: ")
            if action in game.Print_Enemies():
                print(action)
            elif action == "go back":
                pass
            else:
                print("Invalid action. Try again.")
        else:
            print("Invalid action. Try again.")


if __name__ == "__main__":
    main()
