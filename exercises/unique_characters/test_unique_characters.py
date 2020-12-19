from unique_characters import unique_characters

def test1():
    assert unique_characters('') == True

def test2():
    assert unique_characters('goo') == False
    
def test3():
    assert unique_characters('abcdefg') == True

def test4():
    assert unique_characters('abcadefg') == False
