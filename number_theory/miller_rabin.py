
def is_prime(n: int, a: int, d: int , s: int) -> bool:
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    
    return False


def miller_rabin(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True

    s: int = 0
    d: int = n - 1
    while ~d & 1:
        s += 1
        d >>= 1

    base_32 = [2, 7, 61]
    base_64 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in base_32:
        if n == a:
            return True
        if not is_prime(n, a, d, s):
            return False
    
    return True
