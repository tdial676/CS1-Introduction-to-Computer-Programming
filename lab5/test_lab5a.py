"""
Thierno Diallo
Lab5 part A pytest
"""
from lab5a import *

#A1b test random_size function
def test_random_size():
    # Negative inputs
    assert random_size(-1, 2) == None
    assert random_size(-1, -2) == None
    assert random_size(2, -1) == None
    # Odd inputs
    assert random_size(3, 11) == None
    assert random_size(4, 11) == None
    assert random_size(3, 20) == None
    # Argument 1 > Argument 2
    assert random_size(10, 4) == None
    # Equal values
    assert random_size(10, 10) == 10
    # Example case
    for num in range(100):
        assert random_size(100,400) != None
        assert random_size(100,400) % 2 == 0
        assert random_size(100,400) >= 100
        assert random_size(100,400) <= 400


#A2b test random_coords function
def test_random_coords():
    # Negative input
    assert random_coords(100, -50) == None
    assert random_coords(-100, 50) == None
    assert random_coords(-100, -50) == None
    # 0 input
    assert random_coords(100, 0)[1] == 0
    assert random_coords(0, 100)[0] == 0
    # Example
    for num in range(100):
        assert random_coords(250, 677)[0] <= 250
        assert random_coords(250, 677)[1] <= 677
        assert random_coords(250, 677) != None


#A3b test random_color function
def test_random_color():
    for num in range(100):
        assert len(random_color()) == 7
        assert (random_color())[0] == '#'
        for char in (random_color()).replace('#', ''):
            assert char in '0123456789ABCDEF'