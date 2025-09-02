def even_odd(a):
    if a % 2 == 0:
        a = True
    else:
        a = False
    return a


def average(b):
    ave = sum(b)/len(b)
    return ave

def Max(c):
    max = 0
    for i in c:
        if i > max:
            max = i
        else:
            continue
    return max

def Min(d):
    min = Max(d)
    for i in d:
        if i < min:
            min = i
        else:
            continue
    return min