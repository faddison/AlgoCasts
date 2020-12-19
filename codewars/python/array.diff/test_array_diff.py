def assert_equals(expected, actual, message):
    assert expected == actual

def test1():
    assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")

def test2():
    assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")

def test3():
    assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")

def test4():
    assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")

def test5():
    assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")