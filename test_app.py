from app import greet


def test_greet():
    assert greet("Kostya") == "Hello, Kostya!"
