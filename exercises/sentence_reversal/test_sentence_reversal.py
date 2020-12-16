from sentence_reversal import sentence_reversal

def test2():
    assert sentence_reversal('    space before') == 'before space'
    
def test3():
    assert sentence_reversal('space after     ') == 'after space'
    
def test4():
    assert sentence_reversal('   Hello John    how are you   ') == 'you are how John Hello' 
    
def test5():
    assert sentence_reversal('1') == '1'
