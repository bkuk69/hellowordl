from collections import OrderedDict
od = OrderedDict()
od["a"] =1
od["b"] =2
od["c"] =3

print(od)

for kv in od.items():
    print(kv, end=" ")
print()
od1 =dict(a=1, b=2, c=3)
od2 =dict(a=1, c=3, b=2)

print(od1 == od2)

od1 =OrderedDict(a=1, b=2, c=3)
od2 =OrderedDict(a=1, c=3, b=2)

print(od1 == od2)

od1.move_to_end("b")
for kv in od1.items():
    print(kv,end=" ")
print()
od1.move_to_end("b", last=False)
for kv in od1.items():
    print(kv,end=" ")
print()