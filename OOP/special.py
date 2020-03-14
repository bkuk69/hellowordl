class Car:
    def __init__(self,id):
        self.id =id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return "Vehicle Number :" + self.id
    def __iter__(self):
        return iter(self.id)

c = Car("55라 3012")
print(len(c))
print(str(c))

for i in c:
    print (i, end=" ")

