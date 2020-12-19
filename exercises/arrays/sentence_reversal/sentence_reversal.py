def sentence_reversal(s):
    r =""
    strings = s.strip().split(' ')
    for i in range(len(strings)-1,-1,-1):
        if strings[i] != '':
            r = r + ' ' + strings[i].strip()
    return r[1:len(r)]

    # 2:34 0/4 missed for loop decrement. missed the word tokenization. missed mid string blanks case.
    # 7:56 4/4
