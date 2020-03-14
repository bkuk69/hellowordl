class SoSimple:
    def mysimple(self):
        return self.i
    
ss = SoSimple()
ss.i = 10
print(ss.mysimple())

ss.hello = lambda :print("Hi")
ss.hello()

class Simple:
    pass

simple2 = Simple
s1 = Simple()
s2 = simple2()
print(s1)
print(s2)