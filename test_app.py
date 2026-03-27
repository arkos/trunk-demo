from app import greet


def test_greet():
    assert greet("Kostya") == "Hi, KOSTYA!"


def test_greet_trim_spaces():
    assert greet("  Kostya  ") == "Hi, KOSTYA!"
