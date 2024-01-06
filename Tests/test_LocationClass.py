import pytest
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from LocationClass import Location

# Klasa testowa, która została utworzona, by testować rozmieszczenie lokacji oraz elementów w danej lokacji


class TestLocationClass:
    @pytest.fixture
    
    def location(self):
        jsonData = {"Id":"SA","Name":"Elven Valley","Item":[],"Allies":[],"Enemies":[],"Near":{"north":"Cyclops Castle","east":"Elven Camp"},"Description":[{"description":"You're name is Edgar and you're hurt."},{"description":"\nYou are waking up on the valley, where are lots of high grass."},{"description":"\nNear this Elven valley, is a Cyclops castle and Elven Camp."},{"description":"\nArtefacts to find in further game:"},{"description":"\n- The Nimfa's Necklase"},{"description":"\n- The Magic Ring"}]}
        return Location(jsonData)

    def test_initialization(self, location):
        assert location.id == "SA"
        assert location.name == "Elven Valley"
        assert location.items == []
        assert location.allies == []
        assert location.enemies == []
        assert location.near_locations == {"north": "Cyclops Castle", "east": "Elven Camp"}
        assert location.description == [
                {"description": "You're name is Edgar and you're hurt."},
                {"description": "\nYou are waking up on the valley, where are lots of high grass."},
                {"description": "\nNear this Elven valley, is a Cyclops castle and Elven Camp."},
                {"description": "\nArtefacts to find in further game:"},
                {"description": "\n- The Nimfa's Necklase"},
                {"description": "\n- The Magic Ring"}
            ]

    def test_show_details(self, location, capsys):
        location.show_details()
        captured = capsys.readouterr()
        assert captured.out == "\nElven Valley Details:\nItems:\nAllies:\nEnemies:\n"

    def test_get_enemies(self, location):
        assert location.get_enemies() == []


