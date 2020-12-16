# assert_equal(sol('AAABCCDDDDDaaa'), 'A3B1C2D5a3')
def string_compression(s):
    compressed = ''
    last = None
    count = 0 
    for i in range(0, len(s)):
        c = s[i]
        if i == len(s)-1:
            count = count + 1
            compressed = compressed + last + str(count)
        elif (c == last or last == None):
            count = count + 1
        else:
            compressed = compressed + last + str(count)
            print(compressed)
            count = 1
        last = c
    return compressed
            
    # 6:49 0/1
            