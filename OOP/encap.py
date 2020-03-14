class Person:
    def __init__(self, n, a):
        self._name = n
        self._age =a
    def __str__(self):
        return "{0}:{1}".format(self._name, self._age)
    def add_age(self, a):
        if(a<0):
            print("나이 정보 오류")
        else:
            self._age += a

p = Person("Kavin", 22)
p.len =178
p.adr ="Korea"
print(p.__dict__)
p.__dict__["_name"] ="James"
p.__dict__["_age"] = 40
print(p)