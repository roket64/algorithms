from math import sqrt


def naive_sieve(sz: int = 1000000) -> tuple:
    isp = [True for _ in range(sz + 1)]
    spf = [-1 for _ in range(sz + 1)]

    isp[0] = isp[1] = False
    sqrtn = int(sqrt(sz))

    for i in range(2, sqrtn + 1):
        if (isp[i]):
            spf[i] = i

            for j in range(i * i, sz + 1, i):
                isp[j] = False
                if (spf[j] == -1):
                    spf[j] = i

    return (isp, )


def linear_sieve(sz: int = 1000000) -> tuple:
    spf = [0 for _ in range(sz + 1)]
    ret = []

    for i in range(2, sz + 1):
        if (spf[i] == 0):
            spf[i] = i
            ret.append(i)

        for j in ret:
            if (i * j > sz): break
            spf[i * j] = j 
            if (i % j == 0): break

    return (spf, ret)