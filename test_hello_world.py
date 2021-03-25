import hello_world
import pytest


def test_hello_world():
    city = "Chicago"
    assert "Temperature" in hello_world.hello_world(city)

