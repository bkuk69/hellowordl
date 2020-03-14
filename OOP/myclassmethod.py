class Date:
    def __init__(self, y, m,d):
        self.y = y
        self.m = m
        self.d = d
    def show(self):
        print("{0}, {1}, {2}".format(self.y, self.m, self.d))
    @classmethod
    def nex_day(cls,today):
        return cls(today.y, today.m, today.d+1)
class KDate(Date):
    def show(self):
        print("KOR : {0}, {1}, {2}".format(self.y, self.m, self.d))   
class JDate(Date):
    def show(self):
        print("JPN : {0}, {1}, {2}".format(self.y, self.m, self.d))    
kor = KDate(2025, 4,5)
kor.show()
kor2 = kor.nex_day(kor)
kor2.show()

jpn = JDate(2025, 4,2)
jpn.show()
jpn2 = jpn.nex_day(jpn)
jpn2.show()