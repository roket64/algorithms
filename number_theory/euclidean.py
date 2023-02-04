def gcd(x: int, y: int) -> int:
    if (x == y):
        return x
    if (x == 0):
        return y 
    if (y == 0):
        return x

    k = 0
    while (((x | y) & 1) == 0):
        x >>= 1
        y >>= 1
        k += 1

    while (~x & 1):
        x >>= 1

    while (y):

        while (~y & 1):
            y >>= 1

        if (x > y):
            x, y = y, x

        y -= x

    return (x << k)