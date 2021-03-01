def DecToBin(d):
    l = []
    if d == 0:
        l.insert(0, 0)
    while d > 0:
        k = d % 2
        l.insert(0, k)
        d = d // 2
    return l
