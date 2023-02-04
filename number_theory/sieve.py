class sieve:
    def __init__(self, sz: int = 1000000) -> None:
        """
        spf[i]: smallest prime factor of i
        phi[i]: euler phi function of i
        exp[i]: exponent of smallest prime factor of i
        mob[i]: mobius function of i
        prime: list of primes in [2, sz]
        """
        self.sz = sz
        self.spf = [0 for _ in range(sz + 1)]
        self.phi = [0 for _ in range(sz + 1)]
        self.exp = [0 for _ in range(sz + 1)]
        self.mob = [0 for _ in range(sz + 1)]
        self.prime = []

        self.linear_sieve()

    def linear_sieve(self):
        self.phi[1] = 1
        self.mob[1] = 1

        for i in range(2, self.sz + 1):
            if (self.spf[i] == 0):
                self.spf[i] = i
                self.phi[i] = i - 1
                self.exp[i] = 1
                self.mob[i] = -1
                self.prime.append(i)

            for p in self.prime:
                pos = i * p
                if (pos > self.sz):
                    break
                self.spf[pos] = p
                self.phi[pos] = self.phi[i] * p
                self.exp[pos] = self.exp[i] + 1
                self.mob[pos] = 0
                if (i % p == 0):
                    break
