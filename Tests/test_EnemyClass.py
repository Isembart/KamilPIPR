import pytest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from EnemyClass import Enemy


class TestEnemyClass:
    @pytest.fixture
    def enemy(self):
        return Enemy("Cyclop", 100, 10, "eq")

    def test_initialization(self, enemy):
        assert enemy.name == "Cyclop"
        assert enemy.hp == 100
        assert enemy.dmg == 10
        assert enemy.eq == "eq"

    def test_is_alive(self, enemy):
        assert enemy.is_alive() == True
        enemy.hp = 0
        assert enemy.is_alive() == False
        enemy.hp = -1
        assert enemy.is_alive() == False

    def test_take_damage(self, enemy):
        enemy.take_damage(10)
        assert enemy.hp == 90
        enemy.take_damage(90)
        assert enemy.hp == 0
        enemy.take_damage(10)
        assert enemy.hp == -10
