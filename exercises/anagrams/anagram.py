
def anagrams(s1, s2):
    dict1 = {}
    dict2 = {}
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    print(s1)
    print(s2)
    for c in s1:
        if c in dict1:
            dict1[c] = dict1[c] + 1
        else:
            dict1[c] = 1    
    for c in s2:
        if c in dict2:
            dict2[c] = dict2[c] + 1
        else:
            dict2[c] = 1
    return dict1 == dict2

    # 8:18
    # 8:58 2/5  space removal
    # 13:11 3/5 lower case
    # 13:30 5/5 (wrong tests)
    