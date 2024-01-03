import math
import json


class Player:
    def __init__(self, health: int, armour: int, damage: int, eq: list):
        if health < 0:
            raise ValueError("Health cannot be negative")
        if armour < 0:
            raise ValueError("Armour cannot be negative")
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self.health = health
        self.armour = armour
        self.damage = damage
        self.new_armour = 0
        self.gold = 0
        self.eq = eq

    def equip_armour(self, plate):
        self.new_armour = plate
        self.armour = plate

    def drop_weapon(self):
        pass

    def take_damage(self, dmg):
        self.health = self.health - math.floor(dmg*(1-(self.armour/100)))

    def repair_armour(self, prize):
        self.armour = self.new_armour
        self.gold -= prize

    def getting_rich(self, money):
        self.gold += money

    def healing(self, hp):
        self.health += hp
        if self.health > 6:
            self.health = 6

    def steal_gold(self, money):
        self.gold -= money

    def is_alive(self):
        return self.health > 0