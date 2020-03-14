class Simple:
    def __init__(self):
        self.i =0
    def seti(self, i):
        self.i = i

    def geti(self):
        return self.i
    def mytest(self):
        print("without self")
s1 = Simple()
s1.seti(10)
print(s1.geti())

s2 = Simple()
s2.geti()

Simple.n =7
print(Simple.n)
Simple.n += 1
s1.n += 1
print(Simple.n)
print(s1.n)
print(Simple.n)
