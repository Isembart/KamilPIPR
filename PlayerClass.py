import math


class NegativePlayerHealthError(ValueError):
    pass


class NegativePlayerArmourError(ValueError):
    pass


class NegativePlayerDamageError(ValueError):
    pass

# Klasa Player pobiera informacje o naszym graczu, czyli jaką wartość życia ma itp.
class Player:
    def __init__(self, health: int, armour: int, damage: int, eq):
        if health < 0:
            raise NegativePlayerHealthError("Health cannot be negative")
        if armour < 0:
            raise NegativePlayerArmourError("Armour cannot be negative")
        if damage < 0:
            raise NegativePlayerDamageError("Damage cannot be negative")
        self.health = health
        self.armour = armour
        self.damage = damage
        self.gold = 0
        self.eq = eq

        # Metoda służąca do pobierania itemów od zabitych stworów
    def pick_up_item(self, item):
        pass

        # Metoda służąca do opuszczania itemów
    def drop_weapon(self, item):
        pass

        # Metoda, która odpowiada za przyjmowanie przez postać damage od wrogów
    def take_damage(self, dmg):
        self.health = self.health - math.floor(dmg*(1-(self.armour/100)))

        # Setter, który pobiera informacje odnośnie wzrostu poziomu pancerza
    def get_armour(self, plate):
        self.armour += plate

        # Setter, który pobiera informacje odnośnie wzrostu poziomu życia
    def healing(self, hp):
        self.health += hp

        # Getter, który sprawdza za pomocą wyrażenia typu bool czy nasz gracz żyję
    def is_alive(self):
        return self.health > 0
