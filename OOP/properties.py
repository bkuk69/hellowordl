class Natural:
    def __init__(self, n):
        self.__n = n
    
    @property
    def n(self):
        return self.__n

    @n.setter 
    def n(self, n):
        if(n <1):
            self.__n = 1
        else:
            self.__n = n

n1 = Natural(1)
n2 = Natural(2)
n3 = Natural(0)

n3.n = n1.n + n2.n
print(n3.n)

