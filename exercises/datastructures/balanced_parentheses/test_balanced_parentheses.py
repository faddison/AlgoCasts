from balanced_parentheses import balanced_parentheses

def test0():
    assert balanced_parentheses('[)') == False

def test1():
    assert balanced_parentheses('[]') == True

def test3():
    assert balanced_parentheses('([])') == True
    
def test4():
    assert balanced_parentheses('([0])') == True
    
def test5():
    assert balanced_parentheses('([]])') == False

def test6():
    assert balanced_parentheses('[](){([[[]]])}(') == False

def test7():
    assert balanced_parentheses('[{{{(())}}}]((()))') == False

def test8():
    assert balanced_parentheses('[[[]])]') == False