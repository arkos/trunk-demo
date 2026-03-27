from app import greet


def test_greet():
    assert greet("Kostya") == "Hi, Kostya!"


def test_greet_trim_spaces():
    assert greet("  Kostya  ") == "Hi, Kostya!"
