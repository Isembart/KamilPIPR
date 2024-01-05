from PlayerClass import Player


class Location:
    def __init__(self, location_data):
        self.id = location_data["Id"]
        self.name = location_data["Name"]
        self.items = location_data["Item"]
        self.allies = location_data["Allies"]
        self.enemies = location_data["Enemies"]
        self.near_locations = location_data["Near"]
        self.description = location_data["Description"] if "Description" in location_data else []

    # Funkcja pozwalająca zamienić objekt lokacji na tekst zawierający jej opis
    def __str__(self):
        return f"{self.name}\nDescription: \n{''.join(desc['description'] for desc in self.description)}"

    # Funkcja wyświetlająca szczegóły lokacji
    def show_details(self):
        print(f"\n{self.name} Details:")
        print("Items:")
        for item in self.items:
            print(f"- {item['name']}")
        print("Allies:")
        for ally in self.allies:
            print(f"- {ally['name']}")
            if ally['name'] == 'Elf Doctor Peter':
                print("You will be as health as fish!")
                print("You will get some gold for shopping")
                player_instance = Player(300, 20, 0, [])
                player_instance.healing(600)
                player_instance.earn_gold(110)
            if ally['name'] == 'Smith':
                print("Hello Edgar, what things do you want to buy?: ")
                print(f"- {ally['eq']}")
                choice = input("Choose item to buy: ")
                if choice == 'Sword':
                    player_instance.loss_gold(60)
                if choice == 'Bow with Arrows':
                    player_instance.loss_gold(60)
                if choice == 'Hammer':
                    player_instance.loss_gold(70)
                if choice == 'Armour':
                    player_instance.loss_gold(50)
                    player_instance.repair_armour(100)
        print("Enemies:")
        for enemy in self.enemies:
            if enemy['hp'] != 0:
                print(f"- {enemy['name']}")
                print(f"hp - {enemy['hp']}")
                print(f"dmg - {enemy['dmg']}")
                print(f"eq - {enemy['eq']}")

    # Funckja zwraca opis lokacji w formie tekstu
    def get_description(self):
        return f"{self.name}\n\nDescription: \n{' '.join(desc['description'] for desc in self.description)}\n"

    # brief Funkcja zwracająca listę przeciwników w aktualnej lokacji
    def get_enemies(self):
        return [x["name"] for x in self.enemies if x["hp"] != 0]
