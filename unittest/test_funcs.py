from funcs import even_odd, average, Max, Min
# TODO: 사용자 모듈 import


# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_even():
    assert True == test_even(10)
    assert False == test_even(3)
    assert True == test_even(12)
    assert False == test_even(13)

def test_average():
    assert 3 == average([1, 2, 3, 4, 5])
    assert 19.75 == average([12, 14, 21, 32])
    assert 156 == average([211, 124, 133])

def test_Max():
    assert 15 == Max([1, 12, 15, 13, 14])
    assert 14 == Max([1, 12, 0, 13, 14])
    assert 13 == Max([1, 12, 0, 13, 0])

def test_Min():
    assert 1 == Min([1, 12, 15, 13, 14])
    assert 12 == Min([100, 12, 15, 13, 14])
    assert 13 == Min([100, 100, 15, 13, 14])
