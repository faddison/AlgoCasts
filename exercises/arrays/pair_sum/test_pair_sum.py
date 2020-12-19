from pair_sum import pair_sum

def test1():
    assert pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) == 6

def test2():
    assert pair_sum([1,2,3,1],3) == 1

def test3():
    assert pair_sum([1,3,2,2],4) == 2