import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from EnemyClass import (Enemy,
                        EmptyEnemyNameError,
                        NegativeEnemyDmgError,
                        NegativeEnemyHpError)

# Testy, które zostały utworzone do klasy Enemy
# Testują one atrybuty i metody danej klasy


def test_enemy_init():
    enemy = Enemy("Cyclop", 100, 10, "eq")
    assert enemy.name == "Cyclop"
    assert enemy.hp == 100
    assert enemy.dmg == 10
    assert enemy.eq == "eq"


def test_enemy_empty_name():
    with pytest.raises(EmptyEnemyNameError):
        Enemy("", 100, 10, "eq")


def test_enemy_negative_hp():
    with pytest.raises(NegativeEnemyHpError):
        Enemy("Cyclop", -100, 10, "eq")


def test_enemy_negative_damage():
    with pytest.raises(NegativeEnemyDmgError):
        Enemy("Cyclop", 100, -10, "eq")


def test_enemy_is_alive():
    enemy = Enemy("Cyclop", 100, 10, "eq")
    assert enemy.is_alive() == True


def test_enemy_take_damage():
    enemy = Enemy("Cyclop", 100, 10, "eq")
    enemy.take_damage(5)
    assert enemy.hp == 95
