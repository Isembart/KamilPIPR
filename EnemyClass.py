
class Enemy:
    def __init__(self, name, hp, dmg, eq):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.eq = eq

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

