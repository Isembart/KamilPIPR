import math
import json


class Player:
    def __init__(self, health: int, armour: int, damage: int):
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

    def equip_armour(self, plate):
        self.new_armour = plate
        self.armour = plate

    def drop_weapon(self):
        pass

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


class Enemy:
    def __init__(self, name, hp, dmg, eq):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.eq = eq

    def is_alive(self):
        return self.hp > 0

    def taking_dmg(self, damage):
        self.hp -= damage

    '''def attack_player(self, player):
        damage ='''

def main():
    with open('Constructor.json', 'r') as file:
        enemy = json.load(file)

