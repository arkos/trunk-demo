from app import greet


def test_greet():
    assert greet("Kostya") == "Hello, Kostya!"


def test_greet_trim_spaces():
    assert greet("  Kostya  ") == "Hello, Kostya!"
