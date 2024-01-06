class EmptyEnemyNameError(ValueError):
    pass


class NegativeEnemyHpError(ValueError):
    pass


class NegativeEnemyDmgError(ValueError):
    pass

# Klasa, ktora otrzymuje informacje o wrogach z pliku z pliku "Constructor.json"


class Enemy:
    def __init__(self, name, hp, dmg, eq):
        if not name:
            raise EmptyEnemyNameError("Name cannot be empty")
        if hp < 0:
            raise NegativeEnemyHpError("Health points cannot be negative")
        if dmg < 0:
            raise NegativeEnemyDmgError("Damage cannot be negative")
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.eq = eq

        # Metoda, która sprawdza, czy dany wróg żyje
    def is_alive(self):
        return self.hp > 0

        # Setter, który daje nam informacje, ile obrażeń otrzymał nasz wróg
    def take_damage(self, damage: int):
        self.hp -= damage
