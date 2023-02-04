def linear_sieve(sz: int = 1000000) -> tuple:
    # spf[i]: smallest prime factor for i
    # phi[i]: euler phi function for i
    # exp[i]: exponent of smallest prime factor for i
    # mob[i]: mobius function for i
    # ret: primes in given interval [2, sz]
    spf = [0 for _ in range(sz + 1)]
    phi = [0 for _ in range(sz + 1)]
    exp = [0 for _ in range(sz + 1)]
    mob = [0 for _ in range(sz + 1)]
    ret = []

    phi[1] = 1
    mob[1] = 1

    for i in range(2, sz + 1):
        if (spf[i] == 0):
            spf[i] = i
            phi[i] = i - 1
            exp[i] = 1
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

    return (spf, phi, exp, mob, ret)
