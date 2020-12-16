from largest_continuous_sum import largest_continuous_sum

def test1():
    assert largest_continuous_sum([1,2,-1,3,4,-1]) == 9
    
def test2():
    assert largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]) == 29

def test3():
    assert largest_continuous_sum([-1,1]) == 1
    
def test4():
    assert largest_continuous_sum([-1,1,2,-3,1]) == 3
