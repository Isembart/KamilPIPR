import math


class Player:
    def __init__(self, health: int, armour: int, damage: int, eq):
        if health < 0:
            raise ValueError("Health cannot be negative")
        if armour < 0:
            raise ValueError("Armour cannot be negative")
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.health = health
        self.armour = armour
        self.damage = damage
        self.gold = 0
        self.eq = eq

    def pick_up_item(self, item):
        pass

    def drop_weapon(self, item):
        pass

    def take_damage(self, dmg):
        self.health = self.health - math.floor(dmg*(1-(self.armour/100)))

    def repair_armour(self, plate):
        self.armour += plate

    def earn_gold(self, money):
        self.gold += money

    def healing(self, hp):
        self.health += hp

    def loss_gold(self, money):
        self.gold -= money

    def is_alive(self):
        return self.health > 0
