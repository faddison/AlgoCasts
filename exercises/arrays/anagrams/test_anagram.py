from anagram import anagrams

def test_1():
    assert 'abc','cba' == True

def test_2():
    assert 'hi man','hi     man' == True
    
def test_3():
    assert 'aabbcc','aabbc' == False
    
def test_4():
    assert '123','1 2' == False
