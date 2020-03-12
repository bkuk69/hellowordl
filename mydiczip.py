d = dict([("a",1),("b",2),("c",3)])
print(d)

d = dict(a=1, b=2, c=3)
print(d)

d = dict(zip(["a","b","c"],[1,2,3]))


d["d"]= 4

print(d)

for i in d:
    print(d[i], end=" ")

print()
z = zip(["a", "b","c"],(1,2,3))

for i in z:
    print(i,end=" ")
print()
z = zip(("a","b","c"),(1,3,3))
for i in z:
    print(i,end=" ")
print()
z = zip(("abc"),(1,3,3))
for i in z:
    print(i,end=" ")
print()
z = tuple(zip(("abc"),("567")))
for i in z:
    print(i,end=" ")

z = list(zip("abc",(1,2,3),("one","two","three")))
print(z)  

z = list(zip(("abc"),(1,2,3),("one","two","three")))
print(z) 