from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(100, 100) == 200

def test_sub():
    assert sub(3,2) == 1
    assert sub(5,1) == 4
    assert sub(100, 100) == 0
    assert sub(5,6) == -1
