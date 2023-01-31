

def saa




def max_nb(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_nb(55, 200, 30))



def count_char(string, char):
    '''count char occurences in string'''
    n = 0
    for c in string:
        if c == char:
            n += 1
    return n

cnt = count_char('Ottawa', 'a')
print(cnt)


def count_char(string, char):
    return string.count(char)