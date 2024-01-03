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
            if enemy['hp'] != 0:
                print(f"- {enemy['name']}")
                print(f"hp - {enemy['hp']}")
                print(f"dmg - {enemy['dmg']}")
                print(f"eq - {enemy['eq']}")

    def get_description(self):
        return f"{self.name}\n\nDescription: \n{' '.join(desc['description'] for desc in self.description)}\n"

    def get_enemies(self):
        return [x["name"] for x in self.enemies if x["hp"] != 0]
