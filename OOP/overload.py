class Account:
    def __init__(self, aid, abl):
        self.aid = aid
        self.abl = abl
    def __add__(self, m):
        self.abl += m
        print("__add__")
    def __iadd__(self, m):
        self.abl += m
        print("__iadd__")
        return self
    def __sub__(self, m):
        self.abl -= m
        print("__sub__")
    def __isub__(self, m):
        self.abl -= m
        print("__isub__")
        return self
    def __call__(self):
        print("__call__")
        return str(self.aid) + " : " + str(self.abl)
    def __str__(self):
        return "Account {0} : Balance ={1}".format(self.aid, self.abl)

acnt = Account("James01", 100)
acnt += 100
acnt -= 50
print(acnt)


class Vector:
    def __init__(self, x, y):
        self.x =x
        self.y =y
    def __add__(self, o):
        return Vector(self.x + o.x , self.y + o.y)
    def __call__(self):
        return "Vector({0}, {1})".format(self.x, self.y)
    def __iadd__(self,o):
        self.x += o.x
        self.y += o.y
        return self
    def __str__(self):
        return "Vector({0}, {1})".format(self.x, self.y)

v1 = Vector(3,3)
print(v1)
v2 = Vector(7,7)

print(v2)

v1 += v2
print(v1)

class Simple:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return "Simple({0})".format(self.i)
s = Simple(10)
print(s)
print(s.__str__())

