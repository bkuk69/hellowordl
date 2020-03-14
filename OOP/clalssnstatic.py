class Simple:
    count = 0
    def __init__(self):
        Simple.count += 1
    @classmethod
    def get_count(cls):
        return Simple.count
print(Simple.get_count())    
s1 = Simple()
print(Simple.get_count())
s2 = Simple()
print(s2.get_count())
s3 = Simple()
print(s3.get_count())
print(Simple.get_count())

class SM:
    num = 5
    @staticmethod
    def sm(i):
        print("st ~ 5 +{0} = {1}".format(i, SM.num + i))
    @classmethod
    def cm(cls, i):
        print("st ~ 5 +{0} = {1}".format(i, SM.num + i))

SM.sm(3)
SM.cm(3)
s = SM()
s.sm(4)
s.cm(4)

class Natural:
    def __init__(self,n):
        self.n = n
    def getn(self):
        return self.n
    @classmethod
    def add(cls, n1, n2):
        return cls(n1.getn() + n2.getn())
n1 = Natural(1)
n2 = Natural(2)
n3 = Natural.add(n1, n2)
print(n1.getn())
print(n2.getn())
print(n3.getn())
print("{0} + {1} = {2}".format(n1.getn(), n2.getn(),n3.getn()))