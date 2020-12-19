from missing_element import missing_element

def test1():
    assert missing_element([5,5,7,7],[5,7,7]) == 5

def test2():
    assert missing_element([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5

def test3():
    assert missing_element([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6
