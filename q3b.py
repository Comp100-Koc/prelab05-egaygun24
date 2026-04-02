def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a, b = a[2:], b[2:]
    res = 0
    for i in range(len(a)):
        res += int(a[len(a)-1-i]) * (2 ** i)
    res2 = 0
    for j in range(len(b)):
        res2 += int(b[len(b)-1-j]) * (2 ** j)
    c = res + res2
    return "0b" + format(c, 'b')
        