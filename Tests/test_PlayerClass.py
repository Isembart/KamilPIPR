from PlayerClass import (Player,
                         NegativePlayerHealthError,
                         NegativePlayerArmourError,
                         NegativePlayerDamageError)
import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))


def test_initialization():
    player = Player(100, 50, 20, None)
    assert player.health == 100
    assert player.armour == 50
    assert player.damage == 20
    assert player.eq == None


def test_player_negative_health():
    with pytest.raises(NegativePlayerHealthError):
        Player(-1, 50, 20, None)


def test_player_negative_armour():
    with pytest.raises(NegativePlayerArmourError):
        Player(100, -50, 20, None)


def test_player_negative_damage():
    with pytest.raises(NegativePlayerDamageError):
        Player(100, 50, -20, None)


def test_take_damage():
    player = Player(100, 50, 20, None)
    player.take_damage(20)
    assert player.health == 90


def test_get_armour():
    player = Player(100, 50, 20, None)
    player.get_armour(20)
    assert player.armour == 70


def test_healing():
    player = Player(100, 50, 20, None)
    player.healing(10)
    assert player.health == 110


def test_is_alive():
    player = Player(100, 50, 20, None)
    assert player.is_alive() == True
