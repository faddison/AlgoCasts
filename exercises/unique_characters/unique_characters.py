# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.
def unique_characters(s):
    dict = {}
    for c in s:
        if c in dict:
            return False
        else:
            dict[c] = 0
    return True

# sort, then track new chars

def unique_characters2(s):
    dict = {}
    for c in s:
        if c in dict:
            return False
        else:
            dict[c] = 0
    return True
    
# 3:46 3/3