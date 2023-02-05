class disjoint_set:
    def __init__(self, sz :int = 1000000) -> None:
        self.__p = [0 for _ in range(sz + 1)]
        for i in range(sz + 1):
            self.__p[i] = i
    
    def find(self, u: int) -> int:
        while (u != self.__p[u]):
            self.__p[u] = self.__p[self.__p[u]]
            u = self.__p[u]
        return u

    def merge(self, u: int, v: int) -> None:
        u = self.find(u)
        v = self.find(v)
        if (u == v): return
        if (u < v):
            self.__p[v] = u
        else:
            self.__p[u] = v