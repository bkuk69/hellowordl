class Father:
    def run(self):
        print("so fast!!!!")
class Mother:
    def dive(self):
        print("so deep!!!!")
class Son(Father, Mother):
    def run(self):
        super().run()
        print("So fast, so style")
    def jump(self):
        print("so high!!!")
class Car:
    def __init__(self, id, f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fule(self, f):
        self.fuel += f
    def show_info(self):
        print("id:", self.id)
        print("fuel:", self.fuel)

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c
    def add_cargo(self, c):
        self.cargo += c
    def show_info(self):
        super().show_info()
        print("cargo:", self.cargo)


t =Truck("55라 3012", 0,0)
t.add_fule(100)
t.add_cargo(50)
t.drive()
t.show_info()

tf = isinstance(t, Truck)
print(tf)


s = Son()
s.run()
s.jump()
s.dive()