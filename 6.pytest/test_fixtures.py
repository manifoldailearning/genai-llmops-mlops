import pytest 

@pytest.fixture
def numbers():
    return [
        (2,3,5),
        (0,0,0),
        (-1,1,0),
        (100,200,300)
    ]

def test_addition(numbers):
    for n1,n2,exp in numbers:
        result = n1+n2 
        assert result == exp

def test_addition2(numbers):
    for n1,n2,exp in numbers:
        result = n1+n2 
        assert result == exp