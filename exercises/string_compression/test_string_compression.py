from string_compression import string_compression

def test1():
    assert string_compression('AAABCCDDDDDaaa') == 'A3B1C2D5a3'
    
def test2():
    assert string_compression('') == ''
    
def test3():
    assert string_compression('AABBCC') == 'A2B2C2'
    
def test4():
    assert string_compression('AAABCCDDDDD') == 'A3B1C2D5'
