import pytest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


from PlayerClass import Player
import math #potrzebne do obliczenia pancerza

class TestPlayerClass:
    @pytest.fixture
    def player(self):
        return Player(100, 50, 20, None)

    def test_initialization(self, player):
        assert player.health == 100
        assert player.armour == 50
        assert player.damage == 20
        assert player.eq == None

    def test_take_damage(self, player):
        player.take_damage(20)
        assert player.health == 100 - math.floor(20*(1-(50/100)))

    def test_repair_armour(self, player):
        player.gold = 100
        player.repair_armour(20,60)
        assert player.armour == 60
        assert player.gold == 80

    def test_getting_rich(self, player):
        player.getting_rich(200)
        assert player.gold == 200

    def test_healing(self, player):
        player.healing(10)
        assert player.health == 110
