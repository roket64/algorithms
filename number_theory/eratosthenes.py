from math import sqrt


def naive_sieve(sz: int = 1000000) -> tuple:
    phi = [0 for _ in range(sz + 1)]
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
    spf = [0 for _ in range(sz + 1)]  # spf[i]: smallest prime factor for i
    phi = [0 for _ in range(sz + 1)]  # phi[i]: euler phi function for i
    exp = [0 for _ in range(sz + 1)]  # exp[i]: exponent of smallest prime factor for i
    mob = [0 for _ in range(sz + 1)]  # mob[i]: mobius function for i
    ret = []  # primes in given interval [2, sz]

    phi[1] = 1
    mob[1] = 1

    for i in range(2, sz + 1):
        if (spf[i] == 0):
            exp[i] = 1
            phi[i] = i - 1
            spf[i] = i
            mob[i] = -1
            ret.append(i)

        for j in ret:
            if (i * j > sz):
                break
            spf[i * j] = j
            phi[i * j] = phi[i] * j
            exp[i * j] = exp[i] + 1
            mob[i * j] = 0
            if (i % j == 0):
                break

    return (spf, ret)
