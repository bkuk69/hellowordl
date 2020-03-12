d =dict(a=1,b=2,c=3)

for k in d.keys():
    print(d[k], end=" ")
print()
for v in d.values():
    print(v,end=" ")

print() 

for kv in d.items():
    print(kv, end=" ")

print() 

for k, v in d.items():
    print(k, v)

vo = d.items()
for kv in vo:
    print(vo,end=" ")
for k, v in vo:
    d[k] += 2
print()
for k, v in d.items():
    print(k, v)
